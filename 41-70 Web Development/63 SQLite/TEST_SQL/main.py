from flask import Flask
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
        return '<title %r>' % self.title


with app.app_context():
    db.create_all()

    # CREATE RECORD
    # harry_book = Book(title="Harry Potter 35", author="J. K. Rowling", rating=9.3)
    # db.session.add(harry_book)
    # db.session.commit()

    # READ ALL RECORDS
    all_books = db.session.query(Book).all()
    print(all_books)

    # READ A PARTICULAR RECORD
    book = Book.query.filter_by(title="Harry Potter").first()
    print(book)
    
    # UPDATE A PARTICULAR RECORD
    # book_to_update = Book.query.filter_by(title="Harry Potter").first()
    # book_to_update.title = "Harry Potter and the Chamber of Secrets"
    # db.session.commit() 

    # # UPDATE BY PRIMARY KEY
    # book_id = 1
    # book_to_update = Book.query.get(book_id)
    # print(book_to_update)
    # book_to_update.title = "Harry Potter and the Goblet of Fire"
    # db.session.commit()  

# DELETE A RECORD BY PRIMARY KEY
# book_id = 1
# book_to_delete = Book.query.get(book_id)
# db.session.delete(book_to_delete)
# db.session.commit()

# import sqlite3

# db = sqlite3.connect("books-collection.db")

# cursor = db.cursor()

# # cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")

# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()
