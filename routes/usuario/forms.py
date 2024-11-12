from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class Class_Form_Cadastro_Usuario(FlaskForm):
    idusuario = IntegerField('idusuario')
    nome = StringField('Nome', validators=[DataRequired()])
    telefone = StringField('Telefone')
    senha = PasswordField('Senha', validators=[DataRequired()])
    submit = SubmitField('Enviar')
