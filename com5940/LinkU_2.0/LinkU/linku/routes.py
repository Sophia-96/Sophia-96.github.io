import os
import secrets
import json
import requests
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort
from linku import app, db, bcrypt, mail
from linku.forms import (RegistrationForm, LoginForm, UpdateAccountForm,CommentForm, MoneyForm,AddressForm,ActForm,
                             PostForm, RequestResetForm, ResetPasswordForm)
from linku.models import User, Post, Comment, Address, Act
from flask_login import login_user, current_user, logout_user, login_required
from flask_mail import Message

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


@app.route("/")
def home():
    return render_template('footer.html')

##机遇
@app.route("/chance")
def chance():
    headers = {
        'Authorization':'Bearer keygwX4DioRe1fgA2',
    }
    params = (
    ('view', 'Grid view'),
    )

    r = requests.get('https://api.airtable.com/v0/appFNoeGf8A6J96z7/activity?api_key=keygwX4DioRe1fgA2', headers=headers, params=params)
    dict = r.json()
    dataset = []
    
    for i in dict['records']:
         dict = i['fields']
         dataset.append(dict)
    return render_template('chance.html',dataset=dataset)

@app.route("/detail/<int:act_id>", methods=['GET', 'POST'])
@login_required
def detail(act_id):
    headers = {
        'Authorization':'Bearer keygwX4DioRe1fgA2',
    }
    params = (
    ('view', 'Grid view'),
    )

    r = requests.get('https://api.airtable.com/v0/appFNoeGf8A6J96z7/activity?api_key=keygwX4DioRe1fgA2', headers=headers, params=params)
    dict1 = r.json()
    dict2 = {}
    dataset2 = []
    result = []
    
    for i in dict1['records']:
        dict2 = i['fields']
        dataset2.append(dict2)
    for r in dataset2:
        if r['act_id'] == act_id:
            result.append(r)
    form = ActForm()
    forbid = 0
    if Act.query.filter_by(user_id=current_user.id,act_id=act_id):
        forbid = 1
        flash('您已申请过该任务，请勿重复申请。', 'success')
    else:
        if form.validate_on_submit():
            act = Act(act_id = act_id, u_act = current_user)
            db.session.add(act)
            db.session.commit()
            flash('成长值+1！您的申请将在2天内完成审核，请耐心等待喔！', 'success')
            return redirect(url_for('chance'))
    return render_template('detail.html',dataset2 = result, act_id = act_id, form=form, forbid=forbid)


@app.route("/bibi")
def bibi():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('bibi.html', posts=posts)


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
        flash('账号注册成功！你现在可以登陆。', 'success')
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


@app.route("/money", methods=['GET', 'POST'])
@login_required
def money():
    form = MoneyForm()
    if form.validate_on_submit():
        current_user.realname=form.name.data
        current_user.alipay=form.alipay.data
        current_user.bank_account = form.bank_account.data
        current_user.bank_open = form.bank_open.data
        current_user.bank_open_sub = form.bank_open_sub.data
        db.session.commit()
        flash('保存成功！', 'success')
        return redirect(url_for('money'))
    elif request.method == 'GET':
        form.name.data = current_user.realname
        form.alipay.data = current_user.alipay
        form.bank_account.data = current_user.bank_account
        form.bank_open.data = current_user.bank_open
        form.bank_open_sub.data = current_user.bank_open_sub
    return render_template('money.html', form=form)


@app.route("/address/new", methods=['GET', 'POST'])
@login_required
def new_address():
    form = AddressForm()
    if form.validate_on_submit():
        address = Address(contact = form.name.data, mobile = form.mobile.data,
                          fulladdress = form.fulladdress.data, code = form.code.data, u_address=current_user)
        db.session.add(address)
        db.session.commit()
        flash('保存成功！', 'success')
        return redirect(url_for('address'))
    return render_template('create_address.html', title='新建地址',
                           form=form)


@app.route("/address")
@login_required
def address():
    page = request.args.get('page', 1, type=int)
    addresses = Address.query.filter_by(user_id=current_user.id).paginate(page=page)
    return render_template('address.html', title='收货地址', addresses=addresses)


@app.route("/address/<int:address_id>", methods=['GET', 'POST'])
@login_required
def update_address(address_id):
    address = Address.query.get_or_404(address_id)
    if address.u_address != current_user:
        abort(403)
    form = AddressForm()
    if form.validate_on_submit():
        address.contact = form.name.data
        address.mobile = form.mobile.data
        address.fulladdress = form.fulladdress.data
        address.code = form.code.data
        db.session.commit()
        flash('地址已经更新！', 'success')
        return redirect(url_for('address'))
    elif request.method == 'GET':
        form.name.data = address.contact
        form.mobile.data = address.mobile
        form.fulladdress.data = address.fulladdress
        form.code.data = address.code
    return render_template('create_address.html', title='Update Address',
                           form=form)


def save_contentimg(form_contentimg):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_contentimg.filename)
    contentimg_fn = random_hex + f_ext
    contentimg_path = os.path.join(app.root_path, 'static/contentimg', contentimg_fn)

    output_size = (800, 800)
    i = Image.open(form_contentimg)
    i.thumbnail(output_size)
    i.save(contentimg_path)

    return contentimg_fn

@app.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    content_image = None
    if form.validate_on_submit():
        if form.contentimg.data:
            content_imgfile = save_contentimg(form.contentimg.data)
            content_image = content_imgfile
        post = Post(title=form.title.data, content=form.content.data, author=current_user, content_image=content_image)
        db.session.add(post)
        db.session.commit()
        flash('发布成功！', 'success')
        return redirect(url_for('bibi'))
    return render_template('create_post.html', title='发布内容', form=form)

##原来的
#@app.route("/post/<int:post_id>")
#def post(post_id):
#    post = Post.query.get_or_404(post_id)
#    return render_template('post.html', title=post.title, post=post)

@app.route("/post/<int:post_id>",methods=['GET', 'POST'])
@login_required
def post(post_id):
    form = CommentForm()
    post = Post.query.get_or_404(post_id)
    page = request.args.get('page', 1, type=int)
    comments = Comment.query.filter_by(post_id = post_id).paginate(page=page)
    if form.validate_on_submit():
        comment = Comment(content=form.content.data, commenter=current_user,reply=post)
        db.session.add(comment)
        db.session.commit()
        flash('发布成功！', 'success')
        comments = Comment.query.filter_by(post_id = post_id).paginate(page=page)
        return redirect(url_for('post',post_id=post_id))
    else:
        return render_template('post.html', title=post.title, post=post,comments=comments,form=form,post_id=post_id)

##更新帖子内容##
#@app.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
#@login_required
#def update_post(post_id):
#    post = Post.query.get_or_404(post_id)
#    if post.author != current_user:
#        abort(403)
#    form = PostForm()
#    if form.validate_on_submit():
#        post.title = form.title.data
#        post.content = form.content.data
#        db.session.commit()
#        flash('内容已经更新！', 'success')
#        return redirect(url_for('post', post_id=post.id))
#    elif request.method == 'GET':
#        form.title.data = post.title
#        form.content.data = post.content
#    return render_template('create_post.html', title='Update Post',
#                           form=form, legend='Update Post')


@app.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('内容已删除！', 'success')
    return redirect(url_for('bibi'))

##删除回复
#@app.route("/post/<int:post_id>/<int:comment_id>/delete", methods=['POST'])
#@login_required
#def delete_comment(post_id,comment_id):
#    post = Post.query.get_or_404(post_id)
#    comment = Comment.query.get_or_404(comment_id)
#    if comment.commenter != current_user:
#        abort(403)
#    db.session.delete(comment)
#    db.session.commit()
#    flash('已删除！', 'success')
#    return redirect(url_for('/post/<int:post_id>'))


@app.route("/user/<string:username>")
def user_posts(username):
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    posts = Post.query.filter_by(author=user)\
        .order_by(Post.date_posted.desc())\
        .paginate(page=page, per_page=5)
    return render_template('user_posts.html', posts=posts, user=user)

#我的贴子
#@app.route("/user/myposts")
#def my_posts():
#    page = request.args.get('page', 1, type=int)
#    user = User.query.filter_by(username=current_user.username).first_or_404()
#    posts = Post.query.filter_by(author=user)\
#        .order_by(Post.date_posted.desc())\
#        .paginate(page=page, per_page=5)
#    return render_template('my_posts.html', posts=posts, user=user)


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
