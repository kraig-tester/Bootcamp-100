import random
from flask import Flask

# $env:FLASK_APP="main.py" in terminal to set env. var.
app = Flask(__name__)

answer = random.randint(0,9)

@app.route('/')
def hello_world():

    return '<h1>Guess a number between 0 and 9</h1>' \
        '<img src="https://media3.giphy.com/media/123t0dxx3bQdCE/200w.webp?cid=ecf05e47ypovvtggooyoft6i4gb3aeasz8cyzo63uyw4xfqq&rid=200w.webp&ct=g" width=300></img>' \


@app.route('/<int:number>')
def greet(number):
    result = '<h1 style="color: [color]">[text]</h1>'
    img_src = '<img src=[img_src] width=300></img>'
    if number > answer:
        print("too high")
        result = result.replace('[text]', 'Too high, try again!')
        result = result.replace('[color]', '#7b0dc5')
        img_src = img_src.replace('[img_src]', 'https://media0.giphy.com/media/KA3od9qKkvUQ0/200w.webp?cid=ecf05e479ifc13u966gdpt8xf5qm969dwnzv234uw77kxi26&rid=200w.webp&ct=g')
    elif number < answer:
        print("too low")
        result = result.replace('[text]', 'Too low, try again!')
        result = result.replace('[color]', '#c40e17')
        img_src = img_src.replace('[img_src]', 'https://media2.giphy.com/media/58oxPkC3lWuNa/200w.webp?cid=ecf05e479ifc13u966gdpt8xf5qm969dwnzv234uw77kxi26&rid=200w.webp&ct=g')
    else:
        print("perfect")
        result = result.replace('[text]', 'You found me!')
        result = result.replace('[color]', '#009230')    
        img_src = img_src.replace('[img_src]', 'https://media2.giphy.com/media/bI8I9LaRXeN6E/200w.webp?cid=ecf05e47ypovvtggooyoft6i4gb3aeasz8cyzo63uyw4xfqq&rid=200w.webp&ct=g')

    result += img_src 
    return result


if __name__ == "__main__":
    app.run()
