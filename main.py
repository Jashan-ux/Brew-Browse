from flask import Flask, render_template ,request ,redirect , url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField , TimeField , RadioField , SelectField, URLField
from wtforms.validators import DataRequired , InputRequired , URL
import csv



app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    name = StringField("Cafe Name", validators=[DataRequired()])
    location = URLField("Location URL", validators=[DataRequired()])
    open_time = StringField("Opening Time", validators=[DataRequired()])
    close_time = StringField("Closing Time", validators=[DataRequired()])
    coffee_rating = SelectField(
        "Coffee Rating",
        choices=[("✘","✘"),("☕", "1 ☕"), ("☕☕", "2 ☕☕"), ("☕☕☕", "3 ☕☕☕"), 
                 ("☕☕☕☕", "4 ☕☕☕☕"), ("☕☕☕☕☕", "5 ☕☕☕☕☕")],
        validators=[DataRequired()],
    )
    wifi_rating = SelectField(
        "Wifi Rating",
        choices=[("✘","✘"),("💪", "1 💪"), ("💪💪", "2 💪💪"), ("💪💪💪", "3 💪💪💪"), 
                 ("💪💪💪💪", "4 💪💪💪💪"), ("💪💪💪💪💪", "5 💪💪💪💪💪")],
        validators=[DataRequired()],
    )
    power_rating = SelectField(
        "Power Rating",
        choices=[("✘","✘"),("🔌", "1 🔌"), ("🔌🔌", "2 🔌🔌"), ("🔌🔌🔌", "3 🔌🔌🔌"), 
                 ("🔌🔌🔌🔌", "4 🔌🔌🔌🔌"), ("🔌🔌🔌🔌🔌", "5 🔌🔌🔌🔌🔌")],
        validators=[DataRequired()],
    )
    submit = SubmitField("Add Cafe")

# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")




@app.route('/add' , methods = ['GET' , 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open('cafe-data.csv', mode='a', newline='', encoding='utf-8') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow([
                form.name.data,
                form.location.data,
                form.open_time.data,
                form.close_time.data,
                form.coffee_rating.data,
                form.wifi_rating.data,
                form.power_rating.data
            ])
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)
    


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
        
    return render_template('cafes.html', cafes=list_of_rows)




if __name__ == '__main__':
    app.run(debug=True)
