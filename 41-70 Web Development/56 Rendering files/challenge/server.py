from flask import Flask, render_template

# $env:FLASK_APP="server.py" in terminal to set env. var.
app = Flask(__name__)


# rendering index page
@app.route('/')
def render_index():
    return render_template('index.html')


# starting up server
if __name__ == "__main__":
    app.run()