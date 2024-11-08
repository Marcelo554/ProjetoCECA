"""Modelo de dados usando SQLAlchemy"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # Instância do SQLAlchemy

class Usuario(db.Model):
    __tablename__ = 'TabUsuarios'

    idUsuario = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(50), nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    senha = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return f'<Usuario {self.nome}>'

# # Funções CRUD usando SQLAlchemy
# def inserir_usuario(session, usuario: Usuario):
#     """Insere um modelo no banco de dados SQLAlchemy"""
#     session.add(usuario)
#     session.commit()


def mostrar_todos_usuarios():
    usuarios = Usuario.query.all()  # Consulta todos os registros da tabela Usuario
    return [
        {"codigo": usuario.codigo, "nome": usuario.nome, "senha": usuario.senha}
        for usuario in usuarios
    ]


# def deletar_usuario(session, idUsuario: int):
#     """Busca um usuário por ID e deleta o registro"""
#     usuario = session.query(Usuario).get(idUsuario)
#     if usuario:
#         session.delete(usuario)
#         session.commit()
#     else:
#         print("Usuário não encontrado")

# def atualizar_usuario(session, idUsuario: int, novo_usuario: Usuario):
#     """Atualiza um usuário existente no banco de dados"""
#     usuario = session.query(Usuario).get(idUsuario)
#     if usuario:
#         usuario.codigo = novo_usuario.codigo
#         usuario.nome = novo_usuario.nome
#         usuario.senha = novo_usuario.senha
#         session.commit()
#     else:
#         print("Usuário não encontrado")

def contar_usuarios(session):
    """Conta todos os usuários no banco de dados"""
    return session.query(Usuario).count()
