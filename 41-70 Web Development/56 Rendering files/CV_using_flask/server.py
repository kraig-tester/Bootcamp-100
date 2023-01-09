from flask import Flask, render_template

# $env:FLASK_APP="main.py" in terminal to set env. var.
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


if __name__ == "__main__":
    app.run()