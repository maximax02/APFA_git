from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo

class RegisterForm(FlaskForm):
    num_socio = StringField('Numero de socio', validators=[DataRequired("Campo obligatorio")], render_kw={'class':'input', 'placeholder':' '})
    nombre = StringField('Nombre', validators=[DataRequired("Campo obligatorio")], render_kw={'class': 'input', 'placeholder': ' '})
    apellido = StringField('Apellido', validators=[DataRequired("Campo obligatorio")], render_kw={'class': 'input', 'placeholder': ' '})
    email = StringField('Email', validators=[DataRequired("Campo obligatorio"), Email()], render_kw={'class':'input', 'placeholder':' '})
    password = PasswordField('Contraseña', validators=[DataRequired("Campo obligatorio")], render_kw={'class':'input', 'placeholder':' '})
    password2 = PasswordField('Repita contraseña', validators=[DataRequired("Campo obligatorio"), EqualTo('password', 'Las contraseñas no coinciden')], render_kw={'class':'input', 'placeholder':' '})
    submit = SubmitField('Registro', render_kw={'class':'submit'})
