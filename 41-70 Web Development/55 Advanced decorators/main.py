import requests
from flask import Flask

# $env:FLASK_APP="main.py" in terminal to set env. var.
app = Flask(__name__)

print(__name__)
print(requests.__name__)


def make_bold(func):
    def wrapper():
        return "<b>" + func() + "</b>"
    return wrapper


def make_emphasis(func):
    def wrapper():
        return "<em>" + func() + "</em>"
    return wrapper


def make_underline(func):
    def wrapper():
        return "<u>" + func() + "</u>"
    return wrapper


@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
        '<p>This is a paragraph.</p>' \
        '<img src="https://image.winudf.com/v2/image1/Y29tLndhbGxwYXBlci53YWxscGFwZXJzLktpdHRlbnNDYXRzQ3V0ZVdhbGxwYXBlcnNhbmRCYWNrZ3JvdW5kc19zY3JlZW5fMTNfMTU5ODIzNDYxNF8wMDA/screen-5.jpg?fakeurl=1&type=.jpg" width=200></img>' \
        '<br>' \
        '<img src="https://media4.giphy.com/media/g7YDlrD5YLqfe/giphy.gif" width=200></img>' \


@app.route('/bye')
@make_bold
@make_emphasis
@make_underline
def bye():
    return 'Bye world!'


@app.route('/username/<int:number>/<name>')
def greet(name,number):
    return f"Hello there, {name}. Your num is {number}"


if __name__ == "__main__":
    app.run()
