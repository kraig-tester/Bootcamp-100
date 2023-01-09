from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)

app.config['SECRET_KEY'] = 'enter_your_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

login_manager = LoginManager()
login_manager.init_app(app)

db = SQLAlchemy(app)
    
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    name = None
    if current_user.is_authenticated:
        name = current_user.name 
    return render_template("index.html", logged_in=current_user.is_authenticated, name=name)


@app.route('/register', methods=["GET", "POST"])
def register():
    global curr_user
    if request.method == "POST":
        
        user_found = User.query.filter_by(email=request.form.get("email")).first()

        if user_found != None:
            flash("Email already exists.")
            return render_template("register.html")

        new_user = User(
            email = request.form.get("email"),
            name = request.form.get("name"),
            password = generate_password_hash(password=request.form.get("password"),salt_length=8)
        )
        # name = new_user.name
        db.session.add(new_user)
        db.session.commit()

        login_user(new_user)

        return redirect('secrets.html')

    return render_template("register.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    error_message = ""

    if request.method=="POST":
        email = request.form.get('email')
        password = request.form.get('password')

         #Find user by email entered.
        user = User.query.filter_by(email=email).first()

        if user == None:
            flash("User does not exist.")
        elif check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('secrets'))
        else:
            flash("Incorrect password.")

    return render_template("login.html", error_message=error_message)


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html", name=current_user.name, logged_in=current_user.is_authenticated)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))
 

@app.route('/download')
@login_required
def download_file():
    return send_from_directory('static', 'files/cheat_sheet.pdf')


if __name__ == "__main__":
    app.run()
