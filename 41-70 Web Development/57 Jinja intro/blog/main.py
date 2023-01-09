from flask import Flask, render_template
import datetime as dt
import requests
from post import Post

app = Flask(__name__)


response = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
response.raise_for_status()
data = response.json()
all_posts = []
for post in data:
    post = Post(post)
    all_posts.append(post)

@app.route('/')
def home():
    
    return render_template("index.html", all_posts=all_posts)


@app.route('/post/<id>')
def get_post(id):
    post = all_posts[int(id)-1]
    return render_template("post.html", post = post)


if __name__ == "__main__":
    app.run(debug=True)
