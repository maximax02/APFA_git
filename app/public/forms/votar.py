from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField

class VotarForm(FlaskForm):
    listas = SelectField('Listas disponibles: ')
    submit = SubmitField('Votar')