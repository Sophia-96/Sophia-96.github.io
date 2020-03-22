############# Flask Modules Setup ##############

from flask import Flask, render_template, url_for, redirect, request, make_response, Response, jsonify
from flask_login import LoginManager, login_user, current_user, logout_user, login_required, UserMixin
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import requests
import jwt

############ Initialize Flask App ##############

app = Flask(__name__)

#### MySQL SQLAlchemy Object Relations Mapping #####

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://sophia0236:databasepassword@sophia0236.mysql.pythonanywhere-services.com/sophia0236$rankings'
app.config['SECRET_KEY'] = "mysecret"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class rec(db.Model):
    __tablename__ = 'records'
    recordID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(40))
    Ranking = db.Column(db.Integer)
    Nation = db.Column(db.String(2))
    SP = db.Column(db.Float)
    FS = db.Column(db.Float)
    Total = db.Column(db.Float)

############## Login Manager Setup ###############

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
app.config['SECRET_KEY'] = "lkkajdghdadkglajkgah"


@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

class User(UserMixin):
  def __init__(self,id):
    self.id = id

############ Web Page Routes Setup ###############

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/login")
def login():
    if current_user.is_authenticated:
        return redirect(url_for("list_record"))
    message = 'Hello, please login in first.'
    return render_template('login.html', message=message)

@app.route("/form_auth",methods=['POST'])
def form_auth():
    username = request.form['email']
    password = request.form['pwd']
    if username == "Sophia@assign.com" and password == "upupup":
        login_user(User(1))
        # message = "Dear " + username + ", welcome to Sophia's website. Your login has been granted."
        return redirect(url_for("list_record"))
    else:
        message = 'Sorry, wrong password!'
        return render_template('login.html',message=message)

@app.route("/list_record")
@login_required
def list_record():
    dataset = []
    record_list = rec.query.all()
    for record in record_list:
        dataset.append({'recordID': record.recordID, 'Name': record.Name, 'Ranking': record.Ranking, 'Nation': record.Nation,
                       'SP': record.SP, 'FS': record.FS, 'Total': record.Total})
    return render_template('list_record.html', entries=dataset)

@app.route('/album')
def album():
    page_num = 1
    records = rec.query.paginate(per_page=9, page=page_num, error_out=True)
    return render_template('record_paging.html', records=records)

@app.route('/album/<int:page_num>')
def album_paging(page_num):
    records = rec.query.paginate(per_page=6, page=page_num, error_out=True)
    return render_template('record_paging.html', records=records)

@app.route("/add_record",methods=['POST'])
@login_required
def add_record():
    Name = request.form['Name']
    Ranking = request.form['Ranking']
    Nation = request.form['Nation']
    SP = float(request.form['SP'])
    FS = float(request.form['FS'])
    Total = float(request.form['Total'])
    record = rec(Name=Name,Ranking=Ranking,Nation=Nation,SP=SP,FS=FS,Total=Total)
    db.session.add(record)
    db.session.commit()
    dataset = []
    record_list = rec.query.all()
    for record in record_list:
        dataset.append({'recordID': record.recordID, 'Name': record.Name, 'Ranking': record.Ranking, 'Nation': record.Nation,
                       'SP': record.SP, 'FS': record.FS, 'Total': record.Total})
    return render_template('list_record.html', entries=dataset)

@app.route("/update_record",methods=['POST','PUT'])
@login_required
def update_record():
    # add record_id
    record_id = request.form['record_id']
    record = rec.query.filter_by(recordID=record_id).first()
    record.Name = request.form['Name']
    record.Ranking = request.form['Ranking']
    record.Nation = request.form['Nation']
    record.SP = float(request.form['SP'])
    record.FS = float(request.form['FS'])
    record.Total = float(request.form['Total'])
    db.session.commit()
    dataset = []
    record_list = rec.query.all()
    for record in record_list:
        dataset.append({'recordID': record.recordID, 'Name': record.Name, 'Ranking': record.Ranking, 'Nation': record.Nation,
                       'SP': record.SP, 'FS': record.FS, 'Total': record.Total})
    return render_template('list_record.html', entries=dataset)

@app.route("/delete_record",methods=['POST','DELETE'])
@login_required
def delete_record():
    record_id = request.form['record_id']
    record = rec.query.filter_by(recordID=record_id).first()
    db.session.delete(record)
    db.session.commit()
    dataset = []
    record_list = rec.query.all()
    for record in record_list:
        dataset.append({'recordID': record.recordID, 'Name': record.Name, 'Ranking': record.Ranking, 'Nation': record.Nation,
                       'SP': record.SP, 'FS': record.FS, 'Total': record.Total})
    return render_template('list_record.html', entries=dataset)

@app.route('/api')
def api():
    result = db.engine.execute('select * from records')
    final_result = [list(i) for i in result]
    dataset=[]
    dict={}
    for i in final_result:
        dict['recordID'] = i[0]
        dict['Name'] = i[1]
        dict['Ranking'] = i[2]
        dict['Nation'] = i[3]
        dict['SP'] = i[4]
        dict['FS'] = i[5]
        dict['Total'] = i[6]
        # print(i)
        # print(dict)
        dataset.append(dict.copy()) #markers.append(fld.copy())
    return jsonify({'Album': dataset})

@app.route('/logout/')
@login_required
def logout():
    logout_user()
    message = 'Thanks for visiting my website.'
    return render_template('login.html',message=message)

@app.errorhandler(500)
def internal_error(error):
    message = 'Sorry, wrong password!'
    return render_template('login.html',message=message),500

######### API Endpoints ##########


######### Run Flask Web App at Port 90xx ##########

if __name__ == '__main__':
    app.run(debug=True)