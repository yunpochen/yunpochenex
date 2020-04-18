#routes
from flask import  render_template ,flash ,url_for , redirect ,request  #導入函數render_template 為網頁放置位置
from flask_login import login_user , login_required , current_user , logout_user
from app import app ,bcrypt , db
from app.forms import RegisterForm , LoginForm ,PasswordResetRequestForm
from app.models import User


@app.route('/')
@login_required
def index():
       
    return render_template('index.html' )
#網頁內的文字相當HTML的寫法
#return 'hello flsk '


@app.route('/register', methods = ['GET', 'POST'])
def register():
    if current_user.is_authenticated:      #如果已經是登入狀態就回到INDEX
        return redirect(url_for( 'index' ))
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = bcrypt.generate_password_hash(form.password.data)
        user = User(username = username, email = email , password = password)#將資料輸入資料庫到對應欄位
        db.session.add(user)
        db.session.commit()
        flash('register successful' , category = 'success')
        return redirect(url_for('index'))
    return render_template('register.html' , title = 'Home' , form = form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:       #如果已經是登入狀態就回到INDEX
        return redirect(url_for( 'index' ))
    form = LoginForm()
    if form.validate_on_submit():
        
        username = form.username.data   #取得資料庫的DATA
        password = form.password.data   #取得資料庫的DATA
        remember = form.remember.data
        user = User.query.filter_by(username = username).first()
        if user and bcrypt.check_password_hash(user.password, password):
                  #將取得的資料進行比對
            login_user(user, remember = remember)
            flash('login secuss' , category = 'info')
            if request.args.get('next'):
                next_page = request.args.get('next')
                return redirect(next_page)
            return redirect(url_for('index'))
            
        flash('User does not exsit or password incorect' , category = 'danger' )

    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/send_password_reset_request' , methods=['GET', 'POST'])   #忘記密碼 提取參數
def send_password_reset_request():
    if current_user.is_authenticated:       #如果已經是登入狀態就回到INDEX
        return redirect(url_for( 'index' ))
    form = PasswordResetRequestForm()
    return render_template('send_password_reset_request.html', form=form)
