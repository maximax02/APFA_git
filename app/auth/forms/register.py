from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo

class RegisterForm(FlaskForm):
    num_socio = StringField('Numero de socio', validators=[DataRequired()])
    nombre_usuario = StringField('Nombre de usuario', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    password2 = PasswordField('Repita contraseña', validators=[DataRequired(), EqualTo('password', 'Las contraseñas no coinciden')])
    submit = SubmitField('Registro')
