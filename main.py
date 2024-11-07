"""
Modulo principal do sistema biblioteca
"""
import logging  # Import padrão'

# Import de terceiros
from flask import Flask,  redirect, url_for, Blueprint
from flask_wtf.csrf import CSRFProtect

from models.config import Config
from models.models import db  # Usar a instância `db` importada de models

# Importando a blueprint
from routes.usuario.rotas_usuario import usuario_blueprint
from routes.diversas.rotas_diversas import diversas_blueprint
from routes.menu.rotas_menu import menu_blueprint

# Inicializando o app corretamente
app = Flask(__name__)

# Registrando a blueprint (usuario)
app.register_blueprint(usuario_blueprint, url_prefix='/usuario')
app.register_blueprint(diversas_blueprint, url_prefix='/diversas')
app.register_blueprint(menu_blueprint, url_prefix='/menu')


app.config.from_object(Config)  # Carrega as configurações do Config
print("Banco de Dados URI:", app.config.get('SQLALCHEMY_DATABASE_URI'))\


# Verifique a configuração do banco de dados
print(app.config['SQLALCHEMY_DATABASE_URI'])  # Debugging

# Configurando o logging
logging.basicConfig(level=logging.INFO)

# Defina a secret_key (use uma chave segura e aleatória)
app.secret_key = 'sua_chave_secreta_aqui'  # Troque por algo mais seguro


# Inicialize CSRF e o banco de dados
csrf = CSRFProtect(app)
db.init_app(app)  # Inicializa o banco de dados com a configuração do Flask


# Chama o menu principal ao iniciar
@app.route('/')
def index():
    """ index """
    return redirect(url_for('menu.home'))


# Cria as tabelas no Banco de Dados se não existirem
if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Cria as tabelas no banco de dados se não existirem
    app.run(debug=True)  # Executa a aplicação em modo de depuração