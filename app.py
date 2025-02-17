from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html", title="Hello")

@app.route("/hello")
def hello():
    return "<p>hello2</p>"

@app.route("/count/<name>")
def profile(name):
    return str(len(name))

@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/sum", methods=['POST'])
def _sum():
    x = int(request.form['x'])
    y = int(request.form['y'])
    result = x + y
    return str(result)