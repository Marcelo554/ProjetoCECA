"""
    Rotas referentes ao módulo usuario
"""

# Ajuste o import conforme necessário
from .forms import Class_Form_Cadastro_Usuario
from flask import flash, request, render_template, send_file
import logging
from flask import Blueprint,  redirect, url_for, jsonify
from sqlalchemy.exc import SQLAlchemyError

from models.models import Usuario, db

from models.models import mostrar_todos_usuarios

from routes.usuario.forms import Class_Form_Cadastro_Usuario

from fpdf import FPDF
from io import BytesIO


class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Relatório de Usuários', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(10)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()




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







# @usuario_blueprint.route("/atualizar/<int:id>", methods=['GET', 'POST'])
# def atualizar(id):
#     """
#     Atualiza dados do usuário.
#     """
#     usuario = Usuario.query.get_or_404(id)

#     if request.method == 'POST':
#         usuario.codigo = request.form.get("codigo").strip()
#         usuario.nome = request.form.get("nome").strip().upper()

#         try:
#             db.session.commit()
#             flash("Usuário atualizado com sucesso.", "success")
#             return redirect(url_for('usuario.consultar_codigo'))
#         except SQLAlchemyError as e:
#             db.session.rollback()
#             flash(f"Erro ao atualizar usuário: {str(e)}", "error")

#     return render_template('usuario_manutencao_cadastro.html', usuario=usuario)


# @usuario_blueprint.route("/excluir/<int:id>", methods=['POST'])
# def excluir(id):
#     """
#     Exclui usuário do banco de dados.
#     """
#     usuario = Usuario.query.get_or_404(id)

#     try:
#         db.session.delete(usuario)
#         db.session.commit()
#         flash("Usuário excluído com sucesso.", "success")
#         return redirect(url_for('usuario.lista2'))
#     except SQLAlchemyError as e:
#         db.session.rollback()
#         flash(f"Erro ao excluir usuário: {str(e)}", "error")
#         return redirect(url_for('usuario.lista2'))


# def buscar_usuario_por_codigo(codigo):
#     # Tenta buscar o usuário no banco de dados pelo código fornecido
#     usuario = Usuario.query.filter_by(codigo=codigo).first()
#     return usuario







"""
        === ROTINAS AJUSTADAS CADASTRO USUARIO ===
"""

@usuario_blueprint.route("/rota_exibe_grid_usuarios_cadastrados")
def rota_exibe_grid_usuarios_cadastrados():
    """ Rota que exibe na grade os usuarios cadastrados """
    form = Class_Form_Cadastro_Usuario()
    page = request.args.get('page', 1, type=int)
    per_page = 10  # Número de itens por página

    # Pegue os primeiros 'per_page' itens para a página atual
    start = (page - 1) * per_page
    end = start + per_page
    result = mostrar_todos_usuarios()[start:end]

    total_cadastrado = len(mostrar_todos_usuarios())

    return render_template(
        "usuario_tela_base.html",
        form=form,
        result=result,  # Passa os itens da página
        total=total_cadastrado,
        usuarios=result  # Passando o objeto para o template
    )



@usuario_blueprint.route("/rota_paginacao_dados_usuarios_cadastrados")
def rota_paginacao_dados_usuarios_cadastrados():
    form = Class_Form_Cadastro_Usuario()
    page = request.args.get('page', 1, type=int)  # Página atual
    per_page = 10  # Número de itens por página

    # Obtendo todos os usuários de uma vez
    usuarios = mostrar_todos_usuarios()

    # Calculando os índices de início e fim
    start = (page - 1) * per_page
    end = start + per_page

    # Pegando os itens da página
    result = usuarios[start:end]

    # Número total de usuários
    total = len(usuarios)
    # Calculando o número total de páginas
    total_pages = (total // per_page) + (1 if total % per_page > 0 else 0)

    return render_template(
        "usuario_tela_base.html",
        form=form,
        result=result,  # Passando os itens da página
        total=total,     # Total de registros
        page=page,       # Página atual
        per_page=per_page,  # Itens por página
        total_pages=total_pages,  # Total de páginas
    )



@usuario_blueprint.route("/rota_inclusao_manutencao_cadastro_usuario", methods=["GET", "POST"])
def rota_inclusao_manutencao_cadastro_usuario():
    form = Class_Form_Cadastro_Usuario()

    if form.validate_on_submit():
        # Obtendo dados do formulário
        codigo = form.codigo.data
        nome = form.nome.data
        senha = form.senha.data

        # Verificando se o usuário já existe
        usuario_existente = Usuario.query.filter_by(codigo=codigo).first()
        if usuario_existente:
            # Atualizando o usuário existente
            usuario_existente.nome = nome
            usuario_existente.senha = senha
            db.session.commit()
            flash('Usuário atualizado com sucesso!', 'success')
        else:
            # Criando novo usuário
            novo_usuario = Usuario(codigo=codigo, nome=nome, senha=senha)
            db.session.add(novo_usuario)
            db.session.commit()
            flash('Usuário cadastrado com sucesso!', 'success')

        return redirect(url_for('usuario.rota_inclusao_manutencao_cadastro_usuario'))

    # Obtendo todos os usuários ordenados pelo nome
    usuarios = Usuario.query.order_by(Usuario.nome).all()

    # Paginação
    page = request.args.get('page', 1, type=int)
    per_page = 10
    total = len(usuarios)
    start = (page - 1) * per_page
    end = start + per_page
    result = usuarios[start:end]
    total_pages = (total // per_page) + (1 if total % per_page > 0 else 0)

    return render_template(
        "usuario_tela_principal.html",
        form=form,
        result=result,
        total=total,
        page=page,
        per_page=per_page,
        total_pages=total_pages,
        pessoa=[{'codigo': '', 'Nome': '', 'senha': ''}]  # Inicializando o formulário de novo cadastro vazio
    )


@usuario_blueprint.route('/buscar_usuario', methods=['GET'])
def buscar_usuario():
    """Busca idUsuario no banco"""
    print('Oiaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa !!!!!!!!!')
    print('Entrei na rotina buscar_usuario ......')
    id_usuario = request.args.get('idUsuario')
    print(f"Recebido idUsuario: {id_usuario}")

    try:
        id_usuario = int(id_usuario)
    except ValueError:
        return jsonify({"error": "idUsuario inválido"}), 400

    usuario = Usuario.query.filter_by(idUsuario=id_usuario).first()
    if usuario:
        print(f"Usuário encontrado: {usuario.nome}")
        return jsonify({
            'codigo': usuario.codigo,
            'nome': usuario.nome,
            'senha': usuario.senha
        })
    else:
        print("Usuário não encontrado.")
        return jsonify({"error": "Usuário não encontrado"}), 404


@usuario_blueprint.route('/deletar', methods=['POST'])
def deletar_usuario():
    """Deleta um usuário do banco"""
    data = request.get_json()
    if not data or 'idUsuario' not in data:
        print("Dados inválidos recebidos.")
        return jsonify({"error": "Dados inválidos"}), 400

    id_usuario = data['idUsuario']
    print(f"Tentando deletar idUsuario: {id_usuario}")

    try:
        id_usuario = int(id_usuario)
    except ValueError:
        print("idUsuario inválido.")
        return jsonify({"error": "idUsuario inválido"}), 400

    usuario = Usuario.query.filter_by(idUsuario=id_usuario).first()
    if usuario:
        db.session.delete(usuario)
        db.session.commit()
        print(f"Usuário {id_usuario} deletado.")
        return jsonify({"success": True}), 200
    else:
        print("Usuário não encontrado.")
        return jsonify({"error": "Usuário não encontrado"}), 404



@usuario_blueprint.route('/imprimir_cadastro', methods=['GET'])
def imprimir_cadastro():
    usuarios = Usuario.query.all()

    pdf = PDF()
    pdf.add_page()

    # Adicionar título
    pdf.chapter_title('Lista de Usuários')

    # Adicionar dados dos usuários
    for usuario in usuarios:
        body = f"ID: {usuario.idUsuario}\nCódigo: {usuario.codigo}\nNome: {usuario.nome}\n"
        pdf.chapter_body(body)

   # Gera o PDF e obtém o conteúdo como string
    pdf_content = pdf.output(dest='S').encode('latin1')

    # Cria um objeto BytesIO e escreve o conteúdo do PDF nele
    buffer = BytesIO()
    buffer.write(pdf_content)
    buffer.seek(0)

    return send_file(buffer, as_attachment=True, download_name='relatorio_usuarios.pdf', mimetype='application/pdf')