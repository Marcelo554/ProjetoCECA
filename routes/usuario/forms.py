# routes/usuario/forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class Class_Form_Cadastro_Usuario(FlaskForm):
    codigo = StringField('Codigo', validators=[DataRequired()])
    nome = StringField('Nome', validators=[DataRequired()])
    senha = StringField('Senha', validators=[DataRequired()])
    submit = SubmitField('Enviar')