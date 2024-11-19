"""
    Rotas referentes ao módulo usuario
"""

# Ajuste o import conforme necessário
from flask import flash, request, render_template, send_file
import logging
from flask import Blueprint, redirect, url_for, jsonify
from wtforms import StringField, IntegerField, PasswordField, SubmitField
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime
from models.models import Usuario, db

from models.models import mostrar_todos_usuarios

from routes.usuario.forms import Class_Form_Cadastro_Usuario

from fpdf import FPDF
from io import BytesIO


# Define o Blueprint para o módulo de usuário
usuario_blueprint = Blueprint("usuario", __name__, template_folder="templates")


@usuario_blueprint.route("/inserir", methods=["GET", "POST"])
def inserir():
    """
    Inserir usuario *** ROTA VALIDADA ***
    Template = usuario_incluir.html
    """

    print("============> ENTREI NO FORMULARIO")

    if request.method == "POST":
        # Pega os dados do formulário
        codigo = request.form.get("codigo", "").strip()
        nome = request.form.get("nome", "").strip().upper()
        telefone = request.form.get("telefone", "")

        # Verifique se os dados foram recebidos corretamente
        print(f"Código recebido: {codigo}, Nome recebido: {nome}")

        try:
            # Insere os dados no banco de dados

            # Criar uma nova instância do usuário
            novo_usuario = Usuario(codigo=codigo, nome=nome)

            print("Tentando inserir usuário no banco de dados...")

            db.session.add(novo_usuario)

            print("Usuário adicionado à sessão. Tentando commit...")

            db.session.commit()  # Isso deve efetivar a inserção no banco de dados

            print(novo_usuario.codigo)
            print(novo_usuario.nome)

            print("Usuário inserido com sucesso!")

            # Redireciona para o mesmo formulário após sucesso
            return redirect(url_for("usuario.inserir"))

        except SQLAlchemyError as e:
            # Em caso de erro, faz rollback
            # Imprime a mensagem de erro
            print("Falha ao inserir o usuário!", str(e))
            db.session.rollback()
            flash(f"Erro ao inserir dados: {str(e)}", "error")

    # Se for uma requisição GET, exibe o formulário para cadastrar novo usuário
    return render_template("usuario_incluir.html")


@usuario_blueprint.route("/lista2")
def lista2():
    """
    Relação usuarios *** ROTA VALIDADA ***
    """

    # Update variable name to match the template
    usuarios = Usuario.query.order_by(Usuario.nome.asc()).all()

    # Passe 'usuarios' para o template
    return render_template("usuariolista2.html", usuarios=usuarios)


@usuario_blueprint.route("/buscar_usuario_por_codigo", methods=["GET", "POST"])
def buscar_usuario_por_codigo(codigo):
    # Tenta buscar o usuário no banco de dados pelo código fornecido
    usuario = Usuario.query.filter_by(codigo=codigo).first()
    return usuario


@usuario_blueprint.route("/consultar_codigo", methods=["GET", "POST"])
def consultar_codigo():
    form = Class_Form_Cadastro_Usuario()  # Instancie o formulário
    if request.method == "POST":
        codigo = form.codigo.data  # Obtenha o valor do campo codigo do formulário
        usuario = buscar_usuario_por_codigo(codigo)  # Sua função para buscar o usuário

        if usuario:
            return render_template("seu_template.html", usuario=usuario, form=form)
        else:
            flash("Usuário não encontrado!", "danger")

    # Retorne o formulário caso seja um GET ou não encontre o usuário
    return render_template("usuario_manutencao_cadastro.html", form=form)


"""
 ROTINAS AJUSTADAS CADASTRO USUARIO
"""


@usuario_blueprint.route("/rota_exibe_grid_usuarios_cadastrados")
def rota_exibe_grid_usuarios_cadastrados():
    """Rota que exibe na grade os usuarios cadastrados"""
    form = Class_Form_Cadastro_Usuario()
    page = request.args.get("page", 1, type=int)
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
        usuarios=result,  # Passando o objeto para o template
    )


@usuario_blueprint.route("/rota_paginacao_dados_usuarios_cadastrados")
def rota_paginacao_dados_usuarios_cadastrados():
    form = Class_Form_Cadastro_Usuario()
    page = request.args.get("page", 1, type=int)  # Página atual
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
        total=total,  # Total de registros
        page=page,  # Página atual
        per_page=per_page,  # Itens por página
        total_pages=total_pages,  # Total de páginas
    )






@usuario_blueprint.route(
    "/rota_inclusao_manutencao_cadastro_usuario", methods=["GET", "POST"])  #SEM O IDUSUARIO
@usuario_blueprint.route(
    "/rota_inclusao_manutencao_cadastro_usuario/<dusuario>", methods=["GET", "POST"])  #COM O IDUSUARIO
def rota_inclusao_manutencao_cadastro_usuario(idusuario=None):
    """ INCLUSÃO / ALTERAÇÃO """
    print('inicio da rota.................')
    form = Class_Form_Cadastro_Usuario()


    # Converte `idusuario` para string, se existir
    idusuario_str = str(idusuario) if idusuario is not None else None
    print("ID Usuario como string:", idusuario_str)

    # Recupera a lista de todos os usuários para exibir na grid
    usuarios = Usuario.query.all()

    # Se a requisição for GET, verifica se o idusuario foi fornecido
    if request.method == "GET":
        print('Entrei no GET ....')
        idusuario = request.args.get("idusuario")  # Obtém o idusuario da query string (caso editar)
        if idusuario:
            usuario_existente = Usuario.query.get(idusuario)
            if usuario_existente:
                print('Usuario localizado no Get.....')
                # Preenche o formulário com os dados do usuário
                form.idusuario.data = usuario_existente.idUsuario
                form.nome.data = usuario_existente.nome
                form.telefone.data = usuario_existente.telefone
                form.senha.data = usuario_existente.senha
            else:
                flash("Usuário não encontrado.", "warning")

    #INSERINDO O NOVO USARIO SER FOR None ou ""
    if request.method == 'POST':
        print('Entrei no POST ....')
        # Ajustar idusuario antes de validar
        if form.idusuario.data in [None, ""]:
            form.idusuario.data = None
            print('Inserindo novo usuario ...............')

            nome = form.nome.data
            telefone = form.telefone.data
            senha = form.senha.data

            novo_usuario = Usuario(
                nome=nome.upper(), telefone=telefone, senha=senha
            )
            db.session.add(novo_usuario)

            db.session.commit()  # Confirma as alterações
            flash("Usuário atualizado/cadastrado com sucesso!", "success")

    # Se o formulário for submetido
    print('vou validar o formulario.......')
    if form.validate_on_submit():
        print("VALOR TELA IDUSUARIO=",form.idusuario.data)

        idusuario = form.idusuario.data
        nome = form.nome.data
        telefone = form.telefone.data
        senha = form.senha.data

        print('VALOR DE IDUSUARIO (Vindos da tela)=', idusuario, nome)

        try:
            if idusuario:  # Somente tenta busca se `idusuario` tiver um valor válido
                print('ID usuario = ', idusuario)
                usuario_existente = Usuario.query.get(idusuario)
                if usuario_existente:
                    print('alterando usuario existente', usuario_existente)
                    usuario_existente.nome = nome.upper()
                    usuario_existente.telefone = telefone
                    usuario_existente.senha = senha
                    db.session.commit()
                else:
                    flash("Usuário não encontrado.", "warning")
            else:
                # Inserção de novo usuário
                print('Inserindo novo usuario ...............')
                novo_usuario = Usuario(
                    nome=nome.upper(), telefone=telefone, senha=senha
                )
                db.session.add(novo_usuario)
                db.session.commit()  # Confirma as alterações
                flash("Usuário inserido com sucesso!", "success")

            db.session.commit()  # Confirma as alterações
            flash("Usuário atualizado/cadastrado com sucesso!", "success")
        # except Exception as e:
        #     db.session.rollback()  # Desfaz em caso de erro
        #     flash("Ocorreu um erro ao salvar o usuário.", "error")
        #     print(f"Erro ao salvar usuário: {e}")
        finally:
            return redirect(url_for('usuario.rota_inclusao_manutencao_cadastro_usuario'))
    else:
        print("*** Erros de validação do formulario ***")
        # Imprimir os erros para o usuário
        for field, errors in form.errors.items():
            for error in errors:
                print(f"Erro em {field}: {error}")
                flash(f"Erro em {field}: {error}")


    # Obtendo todos os usuários ordenados pelo nome
    usuarios = Usuario.query.order_by(Usuario.nome).all()

    # Paginação ---------------------------------------------------------
    page = request.args.get("page", 1, type=int)
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
        pessoa=[
            {"codigo": "", "Nome": "", "senha": ""}
        ],  # Inicializando o formulário de novo cadastro vazio
    )


@usuario_blueprint.route("/buscar_usuario", methods=["GET"])
def buscar_usuario():
    """Busca idusuario no banco"""
    print("Oiaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa !!!!!!!!!")
    print("Entrei na rotina buscar_usuario ......")
    id_usuario = request.args.get("idusuario")
    print(f"Recebido idusuario: {id_usuario}")

    try:
        id_usuario = int(id_usuario)
    except ValueError:
        return jsonify({"error": "idusuario inválido"}), 400

    usuario = Usuario.query.filter_by(idusuario=id_usuario).first()
    if usuario:
        print(f"Usuário encontrado: {usuario.nome}")
        return jsonify(
            {
                "idusuario": usuario.idusuario,
                "nome": usuario.nome,
                "telefone": usuario.telefone,
                "senha": usuario.senha,
            }
        )
    else:
        print("Usuário não encontrado.")
        return jsonify({"error": "Usuário não encontrado"}), 404


@usuario_blueprint.route("/deletar", methods=["POST"])
def deletar_usuario():
    """Deleta um usuário do banco"""
    data = request.get_json()
    if not data or "idusuario" not in data:
        print("Dados inválidos recebidos.")
        return jsonify({"error": "Dados inválidos"}), 400

    id_usuario = data["idusuario"]
    print(f"Tentando deletar idusuario: {id_usuario}")

    try:
        id_usuario = int(id_usuario)
    except ValueError:
        print("idusuario inválido.")
        return jsonify({"error": "idusuario inválido"}), 400

    usuario = Usuario.query.filter_by(idusuario=id_usuario).first()
    if usuario:
        db.session.delete(usuario)
        db.session.commit()
        print(f"Usuário {id_usuario} deletado.")
        return jsonify({"success": True}), 200
    else:
        print("Usuário não encontrado.")
        return jsonify({"error": "Usuário não encontrado"}), 404


class PDF(FPDF):
    """Classe FPDF que formata o relatorio"""

    def header(self):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Relatório de Usuários", 0, 1, "C")
        self.set_font("Arial", "I", 10)
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        current_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.cell(0, 10, f"Emissão: {current_time}", 0, 0, "L")
        self.cell(0, 10, f"Página {self.page_no()}", 0, 0, "R")

    def chapter_title(self, title):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, title, 0, 1, "C")
        self.ln(10)

    def chapter_body(self, body):
        self.set_font("Arial", "", 10)
        self.multi_cell(0, 10, body)


@usuario_blueprint.route("/filtrar_usuario", methods=["GET"])
def filtrar_usuario():
    nome = request.args.get(
        "nome", ""
    ).upper()  # Obtém o nome do parâmetro da requisição e converte para maiúsculo
    usuarios = Usuario.query.filter(
        Usuario.nome.like(f"%{nome}%")
    ).all()  # Filtra usuários pelo nome

    # Formata os resultados como uma lista de dicionários
    result = [
        {
            "idusuario": usuario.idusuario,
            "codigo": usuario.codigo,
            "nome": usuario.nome,
            "senha": usuario.senha,
        }
        for usuario in usuarios
    ]

    return jsonify({"result": result})


@usuario_blueprint.route("/imprimir_cadastro", methods=["GET"])
def imprimir_cadastro():
    usuarios = Usuario.query.order_by(Usuario.nome).all()

    pdf = PDF()
    pdf.add_page()

    # Definir cabeçalhos da tabela
    pdf.set_font("Arial", "B", 10)
    pdf.cell(10, 8, "ID", 1)
    pdf.cell(80, 8, "Nome", 1)
    pdf.cell(60, 8, "Telefone", 1)
    pdf.ln()

    # Adicionar dados dos usuários
    pdf.set_font("Arial", "", 8)
    total_usuarios = 0
    for usuario in usuarios:
        pdf.cell(10, 10, str(usuario.idusuario), 1)
        # Usar uma célula fixa para o nome para manter tudo na mesma linha
        pdf.cell(80, 10, usuario.nome, 1)
        telefone = usuario.telefone if usuario.telefone else "Não disponível"
        pdf.cell(60, 10, telefone, 1)
        pdf.ln()  # Quebra a linha após imprimir os dados de cada usuário
        total_usuarios += 1

    # Adicionar total de registros
    pdf.ln(10)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, f"Total de Registros: {total_usuarios}", 0, 1, "L")

    # Gera o PDF e obtém o conteúdo como string
    pdf_content = pdf.output(dest="S").encode("latin1")

    # Cria um objeto BytesIO e escreve o conteúdo do PDF nele
    buffer = BytesIO()
    buffer.write(pdf_content)
    buffer.seek(0)

    # ABRIR O ARQUIVO GERADO
    return send_file(
        buffer, mimetype="application/pdf", download_name="relatorio_usuarios.pdf"
    )
