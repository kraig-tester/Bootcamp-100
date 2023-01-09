from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from random import choice

API_KEY = "enter_your_key"

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    
    def to_dict(self):
        return {column.name : getattr(self, column.name) for column in self.__table__.columns}


with app.app_context():
    db.create_all()

    
@app.route("/")
def home():
    return render_template("index.html")


## HTTP GET - Read Record
@app.route("/random")
def get_random_cafe():
    cafes = db.session.query(Cafe).all()
    random_cafe = choice(cafes)
    print(random_cafe)
    cafe_json = jsonify(cafe = random_cafe.to_dict())
    return cafe_json


@app.route('/all')
def get_all_cafes():
    all_cafes = db.session.query(Cafe).all()
    cafes_json = jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])
    return cafes_json


@app.route('/search')
def get_cafes_by_location():
    loc = request.args.get("loc").capitalize()
    cafe = db.session.query(Cafe).filter_by(location=loc).first()
    if cafe:
        cafes_json = jsonify(cafes = cafe.to_dict())
    else: 
        cafes_json = jsonify(error=
            {
                "Not Found": "Sorry, we don't have a cafe at that location."
            }
        )
    return cafes_json


## HTTP POST - Create Record
@app.route('/add', methods=["POST"])
def add_cafe():
    print(request.form)
    new_cafe = Cafe(
        name = request.form.get("name"),
        map_url = request.form.get("map_url"),
        img_url = request.form.get("img_url"),
        location = request.form.get("location"),
        seats = request.form.get("seats"),
        has_toilet = bool(request.form.get("has_toilet").capitalize()),
        has_wifi = bool(request.form.get("has_wifi").capitalize()),
        has_sockets = bool(request.form.get("has_sockets").capitalize()),
        can_take_calls = bool(request.form.get("can_take_calls").capitalize()),
        coffee_price = request.form.get("coffee_price")   
    )
    
    try:
        db.session.add(new_cafe)
        db.session.commit()
        response = jsonify(
            response={
                "id": new_cafe.id,
                "success": "Successfully added the new cafe."
            }
        )
    except:
        response = jsonify(
            response={
                "error": "Invalid data for the new cafe provided."
            }
        )

    return response


## HTTP PUT/PATCH - Update Record
@app.route('/update-price/<cafe_id>', methods=["PATCH"])
def update_cafe(cafe_id):
    cafe_to_update = Cafe.query.get(cafe_id)

    if cafe_to_update == None:
        return jsonify(
            response={
                "error": "Cafe with this id was not found in database."
            }
        )
    
    cafe_to_update.coffee_price = request.args.get("new_price")
    db.session.commit() 

    return jsonify(
        response={
            "success": "Successfully updated he price."
        }
    )


## HTTP DELETE - Delete Record
@app.route('/report-closed/<cafe_id>', methods=["DELETE"])
def delete_cafe(cafe_id):
    if request.args.get("api_key") != API_KEY:
        return jsonify(
            response={
                "error": "Sorry, that's not allowed. Make sure you have the correct api_key."
            }
        )

    cafe_to_delete = Cafe.query.get(cafe_id)
    if cafe_to_delete == None:
        return jsonify(
            response={
                "error": "Sorry a cafe with that id was not found in the database."
            }
        )
    db.session.delete(cafe_to_delete)
    db.session.commit()
    
    return jsonify(
        response={
            "success": "Successfully deleted cafe from the database."
        }
    )

if __name__ == '__main__':
    app.run()
