from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FileField
from flask_wtf.file import FileAllowed
from wtforms.validators import DataRequired

class AgregarListaForm(FlaskForm):
    num_lista = StringField('Número de lista', validators=[DataRequired()], render_kw={'class':'input'})
    presidente = StringField('Presidente', validators=[DataRequired()], render_kw={'class':'input'})
    vicepresidente = StringField('Vicepresidente', validators=[DataRequired()], render_kw={'class':'input'})
    #TODO: Imagen
    imagen = FileField('Imagen del usuario', validators=[FileAllowed(['jpg', 'png'], 'Solo se permiten imágenes')], render_kw={'style': 'width: 100%'})
    submit = SubmitField('Agregar', render_kw={'class':'submit'})
