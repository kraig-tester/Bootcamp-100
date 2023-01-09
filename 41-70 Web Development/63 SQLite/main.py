from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# CREATING DATABASE
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new_books_collection.db"
db = SQLAlchemy(app)

# CREATING TABLE
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250))
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'\ntitle: {self.title}\nauthor: {self.author}\nrating: {self.rating}\n'

with app.app_context():
    db.create_all()

all_books = []

@app.route('/')
def home():
    all_books = db.session.query(Book).all()
    print(all_books)
    return render_template('index.html',all_books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    error_message = ""
    if request.method == 'POST':
        try:
            new_book = Book(title=request.form['title'], author=request.form['author'], rating=float(request.form['rating']))
            db.session.add(new_book)
            db.session.commit()
            all_books.append(new_book)
        except:
            error_message = "Book already exists."
    return render_template('add.html', error_message=error_message)


# Using routing
@app.route('/edit/<book_id>', methods=['GET', 'POST'])
def edit_rating(book_id):
    
    book_to_edit = Book.query.get(book_id)
    error_message = ""
    if request.method == 'POST':
        try:
            book_to_edit = Book.query.get(book_id)
            book_to_edit.rating = request.form['rating']
            db.session.commit() 
        except:
            error_message = "Invalid rating format."
    return render_template('edit.html', id=book_id, book_to_edit=book_to_edit, error_message=error_message)

# # Using hidden field
# @app.route("/edit", methods=["GET", "POST"])
# def edit():
#     if request.method == "POST":
#         book_id = request.form["id"]
#         book_to_update = Book.query.get(book_id)
#         book_to_update.rating = request.form["rating"]
#         db.session.commit()
#         return redirect(url_for('home'))
#     book_id = request.args.get('id')
#     book_selected = Book.query.get(book_id)
#     return render_template("edit.html", book=book_selected)


if __name__ == "__main__":
    app.run()

