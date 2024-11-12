"""Modelo de dados usando SQLAlchemy"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # Instância do SQLAlchemy

class Usuario(db.Model):
    __tablename__ = 'TabUsuarios'

    idusuario = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    telefone = db.Column(db.String(14), nullable=True)
    senha = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return f'<Usuario {self.nome}>'

# class Livro(db.Model):
#     _tablename_ = 'livros'

    # id = db.Column(Integer, primary_key=True)
    # isbn = db.Column(String(20))
    # titulo = db.Column(String(255))
    # autores = db.Column(ARRAY(String))
    # editora = db.Column(String(255))
    # data_publicacao = db.Column(Date)
    # descricao = db.Column(String(100))


def mostrar_todos_usuarios():
    usuarios = Usuario.query.all()  # Consulta todos os registros da tabela Usuario
    return [
        {"codigo": usuario.codigo, "nome": usuario.nome, "senha": usuario.senha}
        for usuario in usuarios
    ]


def contar_usuarios(session):
    """Conta todos os usuários no banco de dados"""
    return session.query(Usuario).count()
