#form.py

from flask_wtf import FlaskForm
from wtforms import StringField , PasswordField , SubmitField , BooleanField #導入用途是為了建立表單
from wtforms.validators import DataRequired, Length , Email , EqualTo , ValidationError #導入用途是為了建立表單 ValidationError是檢視重複輸入
from app.models import User



class RegisterForm(FlaskForm):


    username = StringField('Username', validators = [DataRequired(), Length(min = 6 , max = 20)])#監控用長度監控
    password = PasswordField('Password', validators = [DataRequired(), Length(min = 8 , max = 20)])#監控用長度監控
    confirm = PasswordField('Repeat Password', validators = [DataRequired(), EqualTo('password')])#監控相等於密碼監控
    email = StringField('E-MAIL', validators = [DataRequired(), Email()])#監控用EMAIL
    submit = SubmitField('Register')

    def validate_username(self, username): #導入用途是為了建立表單 ValidationError是檢視重複輸入

        user = User.query.filter_by(username = username.data).first()
        if user:
            raise ValidationError('Username already token')

    def validate_email(self, email):

        mail = User.query.filter_by(email = email.data).first()
        if mail:
            raise ValidationError('email already token')


class LoginForm(FlaskForm):


    username = StringField('Username', validators = [DataRequired(), Length(min = 6 , max = 20)])#監控用長度監控
    password = PasswordField('Password', validators = [DataRequired(), Length(min = 8 , max = 20)])#監控用長度監控
    remember = BooleanField('Remember')
    submit = SubmitField('sign in')
    
class PasswordResetRequestForm(FlaskForm):

    email = StringField('E-MAIL', validators = [DataRequired(), Email()])
    submit = SubmitField('sent')
    def validate_email(self, email):
        mail = User.query.filter_by(email = email.data).first()
        if not email:
            raise ValidationError('email does not exsit')

    
