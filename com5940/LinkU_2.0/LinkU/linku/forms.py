from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from linku.models import User


class RegistrationForm(FlaskForm):
    username = StringField('用户名',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('密码', validators=[DataRequired()])
    confirm_password = PasswordField('确认密码',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('注册')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('用户名已存在，请重新输入。')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email已存在，请重新输入。')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('密码', validators=[DataRequired()])
    remember = BooleanField('记住我')
    submit = SubmitField('登陆')


class UpdateAccountForm(FlaskForm):
    username = StringField('用户名',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    picture = FileField('上传头像', validators=[FileAllowed(['jpg', 'png','jpeg', 'png', 'gif'])])
    intro = StringField('个人简介',validators=[Length(min=2, max=200)])
    submit = SubmitField('更新资料')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('用户名已存在，请重新输入。')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Email已存在，请重新输入。')


class PostForm(FlaskForm):
    title = StringField('标题', validators=[DataRequired(), Length(min=2, max=80)])
    content = TextAreaField('内容', validators=[DataRequired()])
    contentimg = FileField('上传图片', validators=[FileAllowed(['jpg', 'png','jpeg', 'png', 'gif'])])
    submit = SubmitField('发布')

class CommentForm(FlaskForm):
    content = TextAreaField('评论', validators=[DataRequired()])
    submit = SubmitField('发布')
    
    
class MoneyForm(FlaskForm):
    name = StringField('收款人姓名',
                           validators=[DataRequired(), Length(min=2, max=20)])
    alipay = StringField('支付宝账户',
                           validators=[DataRequired(), Length(min=2, max=20)])
    bank_account = StringField('银行账户',
                           validators=[DataRequired(), Length(min=15, max=22)])
    bank_open = StringField('开户行',
                           validators=[DataRequired(), Length(min=2, max=30)])
    bank_open_sub = StringField('开户支行',
                           validators=[DataRequired(), Length(min=2, max=100)])
    submit = SubmitField('保存')
    
    
class AddressForm(FlaskForm):
    name = StringField('联系人姓名',
                           validators=[DataRequired(), Length(min=2, max=20)])
    mobile = StringField('手机号码',
                           validators=[DataRequired(), Length(min=8, max=22)])
    fulladdress = StringField('详细地址',
                           validators=[DataRequired(), Length(min=2, max=200)])
    code = StringField('邮政编码',
                           validators=[DataRequired(), Length(min=4, max=10)])
    submit = SubmitField('保存')
    

class RequestResetForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    submit = SubmitField('重设密码')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('该Email尚未注册。请先注册。')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('密码', validators=[DataRequired()])
    confirm_password = PasswordField('确认密码',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('重设密码')

    
class ActForm(FlaskForm):
    submit = SubmitField('我要申请')