#Flaskとrender_template（HTMLを表示させるための関数）をインポート
from flask import Flask,render_template

# flask_httpauth のインポート
from flask_httpauth import HTTPBasicAuth

#Flaskオブジェクトの生成
app = Flask(__name__)

# 認証機能を変数に代入
auth = HTTPBasicAuth()

# 認証に使用するユーザ名とパスワードを設定
users = {
    "test_user": "test_password"
}

# 認証関数
@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None

#「/」へアクセスがあった場合に、"Hello World"の文字列を返す
@app.route("/")

#　基本認証を通過したユーザーに"Hello World!"と返す
@auth.login_required
def hello():
    return "Hello World!"

#「/index」へアクセスがあった場合に、「index.html」を返す
@app.route("/index")
def index():
    # 基本認証を通過したユーザーに"Hello (ユーザー名)!"と返す
    return "Hello, %s!" % auth.username()