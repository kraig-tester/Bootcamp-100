from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL, Length
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = 'KJklnmsdfkjSDF934rSFDFmlgknh'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Cafe location', validators=[DataRequired(), URL()])
    opening_time = StringField('Opening time e.g. 8AM', validators=[DataRequired(), Length(0, 10)])
    closing_time = StringField('Closing time e.g. 5PM', validators=[DataRequired(), Length(0, 10)])
    rating = StringField('Coffee rating', validators=[DataRequired(), Length(0, 10)])
    wifi_rating = StringField('WIFI strength rating', validators=[DataRequired(), Length(0, 10)])
    power = StringField('Power outlet availability', validators=[DataRequired(), Length(0, 10)])
    submit = SubmitField('Submit')

# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")

@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    # https://www.google.com/maps/place/Coffee+Shake/@45.0178921,39.0371922,19.46z/data=!4m12!1m6!3m5!1s0x40f04551a3b84e6d:0xb5f6ec15aa89403e!2sZatsepi+Kofe!8m2!3d45.0548421!4d39.017079!3m4!1s0x40f0512e33950691:0x5562661c5cd54392!8m2!3d45.0176446!4d39.0374696
    form = CafeForm()
    if form.validate_on_submit():
        print("True")
        with open('cafe-data.csv', newline='\n', encoding='utf8', mode='a') as csv_file:
            csv_file.write(f'\n{form.cafe.data},{str(form.location.data).replace(",", "@@;@@")},{form.opening_time.data},{form.closing_time.data},\
                {form.rating.data},{form.wifi_rating.data},{form.power.data}\n')
        
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='\n', encoding='utf8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
        print(list_of_rows)

    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run()
