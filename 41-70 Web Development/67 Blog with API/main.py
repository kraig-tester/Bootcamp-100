from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
import datetime as dt
import bleach


app = Flask(__name__)
app.config['SECRET_KEY'] = 'enter_your_key'
ckeditor = CKEditor(app)
Bootstrap(app)

##CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

    
##CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])   
    submit = SubmitField("Submit Post")


with app.app_context():
    db.create_all()

    
def strip_invalid_html(content):
    allowed_tags = ['a', 'abbr', 'acronym', 'address', 'b', 'br', 'div', 'dl', 'dt',
                    'em', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'hr', 'i', 'img',
                    'li', 'ol', 'p', 'pre', 'q', 's', 'small', 'strike',
                    'span', 'sub', 'sup', 'table', 'tbody', 'td', 'tfoot', 'th',
                    'thead', 'tr', 'tt', 'u', 'ul']
 
    allowed_attrs = {
        'a': ['href', 'target', 'title'],
        'img': ['src', 'alt', 'width', 'height'],
    }
 
    cleaned = bleach.clean(content,
                           tags=allowed_tags,
                           attributes=allowed_attrs,
                           strip=True)
 
    return cleaned


@app.route('/')
@app.route('/index.html')
def home():
    all_posts = db.session.query(BlogPost).all()
    return render_template('index.html', all_posts=all_posts)


@app.route('/new-post', methods=['GET', 'POST'])
def add_new_post():
    form = CreatePostForm()
    if request.method=='POST':
        today=dt.datetime.today()
        new_post = BlogPost(
            title=request.form.get("title"),
            subtitle=request.form.get("subtitle"),
            date=today.strftime("%B %d, %Y"),
            author=request.form.get("author"),
            img_url=request.form.get("img_url"),
            body=strip_invalid_html(request.form.get("body"))
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('home'))    
    return render_template('add.html', form=form)


@app.route('/edit-post/<post_id>', methods=['GET', 'POST'])
def edit_post(post_id):
    post = BlogPost.query.get(post_id)
        
    if request.method=='POST':
        post.title = request.form.get("title")
        post.subtitle = request.form.get("subtitle")
        post.img_url = request.form.get("img_url")
        post.author = request.form.get("author")
        post.body = request.form.get("body")

        db.session.commit()
        return redirect(url_for('home'))

    form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
    )
    return render_template('add.html', form=form)


@app.route('/delete/<post_id>')
def delete_post(post_id):
    post = BlogPost.query.get(post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/about.html')
def about():
    return render_template('about.html')


@app.route('/contact.html', methods=["GET", "POST"])
def contact():
    if request.method=="POST":
        return render_template('contact.html', message="Successfully sent your message!")
    return render_template('contact.html', message="Contact me")


@app.route('/post/<id>.html')
def post(id):
    all_posts = db.session.query(BlogPost).all()
    return render_template('post.html', post=all_posts[int(id)-1])


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)