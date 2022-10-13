from flask import Flask
from flask_wtf import FlaskForm
from wtfforms import StringField, SubmitField
from wtfforms.validators import DataRequired


class NameForm(FlaskForm):
    name = StringField("What is your name?", validators=[DataRequired()])
    submit = SubmitField("Submit")


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
