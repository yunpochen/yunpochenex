from flask import current_app
from flask_login import UserMixin  #需要用戶登入認證  需要導入UserMixin
from app import db , login
import jwt  #加密避免讓回傳PASSWORD後被發現



@login.user_loader   #要使用此字串確認不然容易造成DB GET 出錯
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()


class User(db.Model , UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80), unique=True , nullable=False)
    password = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), unique=True , nullable=False)

    def __repr__(self):
        return 'User %r' % self.username


    def generate_reset_password_token(self):
        return jwt.encode({'some': 'payload'}, current_app.config['SECRET_KEY'], algorithm='HS256')
    def check_reset_passworf_token(self , token):
        try:
            data = jwt.decode(token , current_app.config['SECRET_KEY'], algorithms=['HS256'])
            
        except:
            return
        
