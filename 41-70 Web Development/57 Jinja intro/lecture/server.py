from flask import Flask, render_template
import random
import datetime as dt
import requests

app = Flask(__name__)


@app.route('/')
def home():
    random_number = random.randint(0,9)
    curr_year = dt.datetime.now().year
    return render_template('index.html', num=random_number, curr_year=curr_year)


@app.route('/guess/<name>')
def guess(name):
    agify_url = "https://api.agify.io"
    genderize_url = "https://api.genderize.io"
    params = {
        "name": name
    }

    a_response = requests.get(url=agify_url, params=params)
    a_response.raise_for_status()
    # print(a_response.text)
    age = a_response.json()["age"]

    g_response = requests.get(url=genderize_url, params=params)
    g_response.raise_for_status()
    # print(response.text)
    gender = g_response.json()["gender"]
    return render_template('guess.html', name=name, age = age, gender=gender)


@app.route('/blog/<num>')
def get_blog(num):
    blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'
    response = requests.get(url=blog_url)
    response.raise_for_status()
    all_posts = response.json()
    return render_template('blog.html', posts = all_posts, num = int(num))


if __name__ == '__main__':
    app.run()