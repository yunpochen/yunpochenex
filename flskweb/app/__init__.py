#__init__

from flask import Flask, render_template ,flash   #導入函數render_template 為網頁放置位置
from flask_bootstrap import Bootstrap #使用Boo satrap 建立CCS~1 需要PIP Bootstrap
from flask_sqlalchemy import SQLAlchemy  #導入資料庫系統Flask 內建的
from flask_bcrypt import Bcrypt #導入密碼加密
from flask_login import LoginManager #導入登入的原件
from config import Config #為了不套用內定得CONFIG 後續自訂一項CONFIG參數


app = Flask(__name__)
app.config.from_object(Config)#

bootstrap = Bootstrap(app) #使用Boo satrap 建立CCS~2
db = SQLAlchemy(app) #輸入資料庫
bcrypt = Bcrypt(app)
login = LoginManager(app) #導入登入的原件
login.login_view = 'login' #登入介面是什麼位置
login.login_message = 'you must login to access this page'
login.login_message_category = 'info'



#flskwb.config['SECRET_KEY'] = 'any secret string'
app.config['SECRET_KEY'] = 'SECRET_KEY'

#from app import routes
from app.routes import *
