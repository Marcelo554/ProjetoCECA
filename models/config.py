"""
config.py
# Conexão com o banco de dados
"""

class Config:
    """Classe de conexão ao banco dados"""
    SQLALCHEMY_DATABASE_URI = (
        'postgresql://bdcata2_user:TsOTypBaqcJQKCnx2b40e1nL6qwZlAhB@'
        'dpg-csh3bg3tq21c73e2m510-a.oregon-postgres.render.com/bdcata2'
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False
