"""
    Rotas menu
"""

from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.models import Usuario, db

# Define o Blueprint para o módulo de usuário
menu_blueprint = Blueprint('menu', __name__, template_folder='templates')


@menu_blueprint.route('/home')
def home():
    """home"""
    print('rota menu home - vou chamar o menu pricipal')
    return render_template('menu_principal.html')


@menu_blueprint.route('/menu_modulo_cadastros_gerais')
def menu_modulo_cadastros_gerais():
    print('rota modulo cadastros gerais')
    # Renderiza a página de menumodcadastros
    return render_template('menu_modulo_cadastros_gerais.html')


@menu_blueprint.route('/menu_opcoes_cadastro_usuario')  # Menu Opcoes Usuario
def menu_opcoes_cadastro_usuario():
    print('rota opcao_cadastro_usuario')
    # Renderiza a página de menumodcadastros
    return render_template('menu_opcoes_cadastro_usuario.html')
