from flask import Flask

app= Flask(__name__)


@app.route("/shriyansh") #decorator
def hello():
    return "hello World"

@app.route("/") #decorator
def hello1():
    return "Welcome to home"



app.run(debug=True)