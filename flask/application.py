# To run the application
'''
export FLASK_APP=application.py
export FLASK_DEB=True
export FLASK_ENV=development
flask run
'''
from flask import Flask, render_template, request, session
from flask_session import Session
import datetime

app = Flask(__name__)

app.config["SESSION_PERMANENT"] =  False
app.config["SESSION_TYPE"] = 'filesystem'
Session(app)


# / default page of the website
# When go to the '/' run the function
@app.route("/", methods=["GET", "POST"])
def index():
    if session.get("notes") is None:
        session["notes"] = []
    now = datetime.datetime.now()
    new_year = now.month == 1 and now.day == 1
    # new_year = True
    # return "Hello, world!"
    headline = "Hi there."
    # index.html 存在 ./templates里面
    # 将headline这个变量,传给index.html
    names = ["Jack", "Peter", "Dylan"]

    if request.method == "POST":
        note = request.form.get("note")
        session["notes"].append(note)

    return render_template("index.html", headline=headline, \
        new_year=new_year, names=names, notes=session["notes"] )

# @app.route("/jack")
# def jack():
#     return "Hello, Jack!"

# 一个通用的打招呼的 这样就不用单独写了
# 只需要修改python文件就可以改网页
# @app.route("/<string:name>")
# def hello(name):
#     # 首字母变大写
#     name = name.capitalize()
#     return f"<h1>Hello, {name}</h1>"

@app.route("/bye")
def bye():
    headline = "Goodbye!"
    return render_template("index.html", headline=headline)

@app.route("/more")
def more():
    return render_template("more.html")

@app.route("/hello", methods=["GET", "POST"])
def hello():
    # 用户直接输入的网址
    if request.method == "GET":
        return "Please submit the form instead."
    else:
        name = request.form.get("name")
        return render_template("hello.html", name=name)