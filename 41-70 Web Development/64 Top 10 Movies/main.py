from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = 'enter_your_key'
TMDB_URL_SEARCH = "https://api.themoviedb.org/3/search/movie"
TMDB_URL_GET = "https://api.themoviedb.org/3/movie"
TMDB_IMG_URL = "https://image.tmdb.org/t/p/w185"
TMDB_API_KEY = "enter_your_tmdb_key"

Bootstrap(app)

# CREATING DATABASE
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies_collection.db"
db = SQLAlchemy(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description  = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(500), nullable=True)


class RateMovieForm(FlaskForm):
    rating = StringField('Your rating out of 10 e.g. 7.5', validators=[DataRequired()])
    review = StringField('Your review', validators=[DataRequired()])
    submit = SubmitField("Done")


class AddMovieForm(FlaskForm):
    title = StringField('Movie Title', validators=[DataRequired()])
    submit = SubmitField("Add Movie")


with app.app_context():
    db.create_all()

# # Test movie
# new_movie = Movie(
#     title="Phone Booth", 
#     year=2002, 
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's \
#         sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller \
#         leads to a jaw-dropping climax.",
#     rating=7.3, ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://upload.wikimedia.org/wikipedia/en/thumb/c/c4/Phone_Booth_movie.jpg/220px-Phone_Booth_movie.jpg"
# )

# db.session.add(new_movie)
# db.session.commit()


@app.route("/")
def home():
    # all_movies = Movie.query.order_by(Movie.rating).all()
    all_movies = db.session.query(Movie).order_by(Movie.rating).all()
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i

    # For further reflection in database.
    db.session.commit()
    
    return render_template("index.html", all_movies=all_movies)


@app.route("/add", methods=["GET", "POST"])
def add_movie():
    form = AddMovieForm()
    if form.validate_on_submit():
        print(form.title.data)
        return redirect(url_for('select_movie', movie_title=form.title.data))
    return render_template('add.html', form=form)


@app.route("/select")
def select_movie():
    params = {
        "api_key": TMDB_API_KEY,
        "query": request.args.get("movie_title")
    }
    movies_found = requests.get(url=TMDB_URL_SEARCH, params=params).json()['results']
    print(movies_found)
    return render_template('select.html', movies_found=movies_found)


@app.route("/commit")
def commit_add_movie():
    movie_id = request.args.get("movie_id")
    params = {
        "api_key": TMDB_API_KEY
    }
    print(f"{TMDB_URL_GET}/{str(movie_id)}")
    movie_response = requests.get(url=f"{TMDB_URL_GET}/{str(movie_id)}", params=params).json()
    print(movie_response)
    new_movie = Movie(
        title=movie_response['title'], 
        year=int(movie_response['release_date'].split('-')[0]),
        description=movie_response['overview'],
        img_url=movie_response['poster_path'] if movie_response['poster_path'] is None else TMDB_IMG_URL+movie_response['poster_path']
        )
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for('rate_movie', id=new_movie.id))


@app.route("/edit", methods=["GET", "POST"])
def rate_movie():
    form = RateMovieForm()
    movie_id = request.args.get("id")
    movie = Movie.query.get(movie_id)
    if form.validate_on_submit():
        movie.rating = form.rating.data
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', movie=movie, form=form)


@app.route('/delete', methods=["GET", "POST"])
def delete_movie():
    movie_id = request.args.get("id")
    movie_to_delete = Movie.query.get(movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


# testing purposes
def update_img_url():
    new_img_url = "https://upload.wikimedia.org/wikipedia/en/thumb/c/c4/Phone_Booth_movie.jpg/220px-Phone_Booth_movie.jpg"
    movie_to_edit = Movie.query.get(1)
    movie_to_edit.img_url = new_img_url
    db.session.commit()

if __name__ == '__main__':
    app.run()
