from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from linku import db, login_manager, app
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(30), nullable=False, default='default.jpg')
    intro = db.Column(db.String(200), default='')
    password = db.Column(db.String(60), nullable=False)
    ##收款信息##
    realname = db.Column(db.String(20), nullable=False, default='')
    alipay = db.Column(db.String(100), nullable=False, default='')
    bank_account = db.Column(db.String(100), nullable=False, default='')
    bank_open = db.Column(db.String(100), nullable=False, default='')
    bank_open_sub = db.Column(db.String(100), nullable=False, default='')
    ##其他table##
    posts = db.relationship('Post', backref='author', lazy=True)
    comments = db.relationship('Comment', backref='commenter', lazy=True)
    addresses = db.relationship('Address', backref='u_address', lazy=True)
    acts = db.relationship('Act', backref='u_act', lazy=True)

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    contact = db.Column(db.String(20), nullable=False, default='')
    mobile = db.Column(db.String(20), nullable=False, default='')
    fulladdress = db.Column(db.String(200), nullable=False, default='')
    code = db.Column(db.String(20), nullable=False, default='')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    content_image = db.Column(db.String(30), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    comments = db.relationship('Comment', backref='reply', lazy=True)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    
    
class Act(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_applied = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    act_id = db.Column(db.Integer, unique=True, nullable=False)
    check_status = db.Column(db.String(20), nullable=False, default='审核中')
    progress_status = db.Column(db.String(20), nullable=True, default='')
    complete_status = db.Column(db.String(20), nullable=True, default='')
    status_change_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)