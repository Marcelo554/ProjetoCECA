"""
    Rotas referentes ao módulo usuario
"""

# Ajuste o import conforme necessário
from .forms import Class_Form_Cadastro_Usuario
from flask import flash, request, render_template
import logging
from flask import Blueprint,  redirect, url_for
from sqlalchemy.exc import SQLAlchemyError

from models.models import Usuario, db


from .forms import Class_Form_Cadastro_Usuario


# Define o Blueprint para o módulo de usuário
usuario_blueprint = Blueprint('usuario', __name__, template_folder='templates')


@usuario_blueprint.route('/inserir', methods=['GET', 'POST'])
def inserir():
    """
    Inserir usuario *** ROTA VALIDADA ***
    Template = usuario_incluir.html
    """

    print('============> ENTREI NO FORMULARIO')

    if request.method == 'POST':
        # Pega os dados do formulário
        codigo = request.form.get('codigo', '').strip()
        nome = request.form.get('nome', '').strip().upper()

        # Verifique se os dados foram recebidos corretamente
        print(f"Código recebido: {codigo}, Nome recebido: {nome}")

        try:
            # Insere os dados no banco de dados

            # Criar uma nova instância do usuário
            novo_usuario = Usuario(codigo=codigo, nome=nome)

            print('Tentando inserir usuário no banco de dados...')

            db.session.add(novo_usuario)

            print('Usuário adicionado à sessão. Tentando commit...')

            db.session.commit()  # Isso deve efetivar a inserção no banco de dados

            print(novo_usuario.codigo)
            print(novo_usuario.nome)

            print('Usuário inserido com sucesso!')

            # Redireciona para o mesmo formulário após sucesso
            return redirect(url_for('usuario.inserir'))

        except SQLAlchemyError as e:
            # Em caso de erro, faz rollback
            # Imprime a mensagem de erro
            print('Falha ao inserir o usuário!', str(e))
            db.session.rollback()
            flash(f'Erro ao inserir dados: {str(e)}', 'error')

    # Se for uma requisição GET, exibe o formulário para cadastrar novo usuário
    return render_template('usuario_incluir.html')




@usuario_blueprint.route("/lista2")
def lista2():
    """
    Relação usuarios *** ROTA VALIDADA ***
    Template = usuariolista2.html
    """

    # Update variable name to match the template
    usuarios = Usuario.query.order_by(Usuario.nome.asc()).all()

    # Passe 'usuarios' para o template
    return render_template('usuariolista2.html', usuarios=usuarios)



@usuario_blueprint.route("/consultar_codigo", methods=['GET', 'POST'])
def consultar_codigo():
    form = Class_Form_Cadastro_Usuario()  # Instancie o formulário
    if request.method == 'POST':
        codigo = form.codigo.data  # Obtenha o valor do campo codigo do formulário
        usuario = buscar_usuario_por_codigo(codigo)  # Sua função para buscar o usuário

        if usuario:
            return render_template('seu_template.html', usuario=usuario, form=form)
        else:
            flash('Usuário não encontrado!', 'danger')

    # Retorne o formulário caso seja um GET ou não encontre o usuário
    return render_template('usuario_manutencao_cadastro.html', form=form)


@usuario_blueprint.route("/atualizar/<int:id>", methods=['GET', 'POST'])
def atualizar(id):
    """
    Atualiza dados do usuário.
    """
    usuario = Usuario.query.get_or_404(id)

    if request.method == 'POST':
        usuario.codigo = request.form.get("codigo").strip()
        usuario.nome = request.form.get("nome").strip().upper()

        try:
            db.session.commit()
            flash("Usuário atualizado com sucesso.", "success")
            return redirect(url_for('usuario.consultar_codigo'))
        except SQLAlchemyError as e:
            db.session.rollback()
            flash(f"Erro ao atualizar usuário: {str(e)}", "error")

    return render_template('usuario_manutencao_cadastro.html', usuario=usuario)


@usuario_blueprint.route("/excluir/<int:id>", methods=['POST'])
def excluir(id):
    """
    Exclui usuário do banco de dados.
    """
    usuario = Usuario.query.get_or_404(id)

    try:
        db.session.delete(usuario)
        db.session.commit()
        flash("Usuário excluído com sucesso.", "success")
        return redirect(url_for('usuario.lista2'))
    except SQLAlchemyError as e:
        db.session.rollback()
        flash(f"Erro ao excluir usuário: {str(e)}", "error")
        return redirect(url_for('usuario.lista2'))





def buscar_usuario_por_codigo(codigo):
    # Tenta buscar o usuário no banco de dados pelo código fornecido
    usuario = Usuario.query.filter_by(codigo=codigo).first()
    return usuario