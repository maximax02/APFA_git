from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import InputRequired, Length, Email, AnyOf

class LoginForm(FlaskForm):
    opcion = SelectField('Opción de logueo', choices=[('0', 'Email'), ('1', 'Número de socio')], render_kw={'onchange':'displayDiv()'})
    email = StringField('Email')
    num_socio = StringField('Numero de Socio')
    password = PasswordField('Password', validators=[InputRequired()])
    remember_me = BooleanField('Recuerdame')
    submit = SubmitField('Login')