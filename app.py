from unittest.mock import AsyncMockMixin
from flask import Flask
from flask_login import LoginManager
from flask import request
from flask import redirect
import json
from flask import render_template
from flask import session


app = Flask(
    __name__,
    static_folder="static",  # 靜態檔案的資料夾名稱,
    static_url_path="/")  # 靜態檔案對應的網址路徑

# 所有在 static 資料夾底下的檔案，都對應到網址路徑/檔案名稱


# @app.route("/getSum")
# def getSum():
#     maxNumber = request.args.get("max", 100)
#     maxNumber = int(maxNumber)
#     minNumber = request.args.get("min", 1)
#     minNumber = int(minNumber)
#     result = 0
#     for n in range(minNumber, maxNumber+1):
#         result += n
#     return "結果:" + str(result)
app.secret_key = "123456"  # 設定 Sessopm 密要


@app.route("/")
def index():
    return render_template("login.html")


@app.route("/hello")
def hello():
    name = request.args.get("name", "")
    session["username"] = name
    return "你好 ，" + name


@app.route("/talk")
def talk():
    name = session["username"]
    return name+"很高興見到你"


@app.route("/show")
def show():
    name = request.args.get("n", "")
    return "歡迎光臨," + name


@app.route("/page")
def page():
    return render_template("page.html")


@app.route("/data")
def handleData():
    return "My Data"


@app.route("/user/<username>")
def handleUser(username):
    return "Hello "+username


app.run(port=3000)
