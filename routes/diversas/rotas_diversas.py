"""
    Rotas diversas
"""
from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.models import Usuario, db

# Define o Blueprint para o módulo de usuário
diversas_blueprint = Blueprint('diversas', __name__, template_folder='templates')


@diversas_blueprint.route('/home')
def home():
    return render_template('menu/menuprincipal.html')


@diversas_blueprint.route('/contatos')
def contatos():
    # Renderiza a página de contatos
    return render_template('contatos.html')

@diversas_blueprint.route('/modulocadastros')
def modulocadastros():
    # Renderiza a página de contatos
    return render_template('menu/menumodcadastros.html')

@diversas_blueprint.route('/modulo_usuario')
def modulo_usuario_view():
    # Renderiza a página do módulo de usuário
    return render_template('menu/menumodusuario.html')

@diversas_blueprint.route('/usuario_inserir')
def incluirusuario():
    print('entrei na rota INCLUIR usuario')
    return render_template('cadastros/usuario/usuarioincluir.html')

# ROTA NÃO DEFINIDA

@diversas_blueprint.route('/menu/<int:module_id>')
def module(module_id):
    # Lógica para renderizar diferentes módulos se necessário
    return f"Módulo selecionado: {module_id}"  # Apenas para exemplo
