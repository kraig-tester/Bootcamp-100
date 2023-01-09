from flask import Flask, render_template, request
import requests
import smtplib

app = Flask(__name__)

all_posts = requests.get('https://api.npoint.io/f619c7e8cbfe78f4db57').json()
EMAIL = "test.gmail.com"
PASSWORD = "password"

print(all_posts)
@app.route('/')
@app.route('/index.html')
def home():
    return render_template('index.html', all_posts=all_posts)


@app.route('/about.html')
def about():
    return render_template('about.html')


@app.route('/contact.html', methods=["GET", "POST"])
def contact():
    if request.method=="POST":
        name = request.form['username']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        contents = f"Subject:New message\n\nName: {name}\nEmail: {email}\Phone: {phone}\Message: {message}"
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(EMAIL, PASSWORD)
            connection.sendmail(
                from_addr=EMAIL, 
                to_addrs=EMAIL, 
                msg=contents
            )
        return render_template('contact.html', message="Successfully sent your message!")
    return render_template('contact.html', message="Contact me")


@app.route('/post/<id>.html')
def post(id):
    return render_template('post.html', post=all_posts[int(id)-1])


if __name__ == "__main__":
    app.run()