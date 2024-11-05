"""
Este módulo configura e inicializa a aplicação Flask,
inclui a configuração do banco de dados e define as rotas de usuário.
"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # Cria uma instância do SQLAlchemy

class Usuario(db.Model):
    __tablename__ = 'TabUsuarios'

    idUsuario = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(50), nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    senha = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return f'<Usuario {self.nome}>'
