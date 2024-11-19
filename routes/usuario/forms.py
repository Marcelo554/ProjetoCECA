from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Optional


class Class_Form_Cadastro_Usuario(FlaskForm):
    idusuario =  IntegerField('idusuario')
    nome = StringField('Nome')
    telefone = StringField('Telefone')
    senha = PasswordField('Senha')
    submit = SubmitField('Enviar')

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.idusuario.data = ""  # Define o valor inicial como string vazia
    #     self.idusuario.nome = ""  # Define o valor inicial como string vazia

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

