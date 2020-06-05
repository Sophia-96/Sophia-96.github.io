import os
import secrets
import json
import requests
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort
from fitup import app, db, bcrypt, mail
from fitup.forms import (RegistrationForm, LoginForm, UpdateAccountForm, RequestResetForm, ResetPasswordForm)
from fitup.models import User
from flask_login import login_user, current_user, logout_user, login_required
from flask_mail import Message


@app.route("/")
def home():
    return render_template('footer.html')


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html', title='注册', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('登录失败，请确认Email和密码。', 'danger')
    return render_template('login.html', title='登陆', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))



@app.route("/me")
def me():
    if current_user.is_authenticated:
        image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    else:
        image_file = url_for('static', filename='profile_pics/default.jpg')
    return render_template('me.html',image_file=image_file)


@app.route("/about")
def about():
    return render_template('about.html')


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn


#修改个人资料
@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        current_user.intro = form.intro.data
        db.session.commit()
        flash('你的资料已经更新！', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
        form.intro.data = current_user.intro
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', title='账号',
                           image_file=image_file, form=form)


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('重设密码',
                  sender='linku202003@gmail.com',
                  recipients=[user.email])
    msg.body = f'''要重设您的密码，请点击以下链接:
{url_for('reset_token', token=token, _external=True)}

如果您未申请重设密码，请忽略此邮件。
'''
    mail.send(msg)


@app.route("/reset_password", methods=['GET', 'POST'])
def reset_request():
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash('重设密码邮件已发送至您的邮箱，请及时查收。', 'info')
        return redirect(url_for('login'))
    return render_template('reset_request.html', title='重设密码', form=form)


@app.route("/reset_password/<token>", methods=['GET', 'POST'])
def reset_token(token):
    logout_user()
    user = User.verify_reset_token(token)
    if user is None:
        flash('密令错误或已经失效。', 'warning')
        return redirect(url_for('reset_request'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hashed_password
        db.session.commit()
        flash('您的密码已经更新，现在可以前往登陆页面。', 'success')
        return redirect(url_for('login'))
    return render_template('reset_token.html', title='重设密码', form=form)
