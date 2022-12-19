from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FileField
from flask_wtf.file import FileAllowed
from wtforms.validators import DataRequired

class AgregarListaForm(FlaskForm):
    num_lista = StringField('Número de lista', validators=[DataRequired()])
    presidente = StringField('Presidente', validators=[DataRequired()])
    vicepresidente = StringField('Vicepresidente', validators=[DataRequired()])
    #TODO: Imagen
    imagen = FileField('Imagen del usuario', validators=[FileAllowed(['jpg', 'png'], 'Solo se permiten imágenes')], render_kw={'style': 'width: 50%'})
    submit = SubmitField('Agregar')
