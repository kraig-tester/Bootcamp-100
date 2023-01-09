import requests
from flask import Flask

# $env:FLASK_APP="main.py" in terminal to set env. var.
app = Flask(__name__)

print(__name__)
print(requests.__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/bye')
def bye():
    return 'Bye world!'

if __name__ == "__main__":
    app.run()