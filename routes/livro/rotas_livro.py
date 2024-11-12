# import requests

# def buscar_livro_por_isbn(isbn):
#     url = f"https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}"
#     response = requests.get(url)

#     if response.status_code == 200:
#         dados_livro = response.json()
#         if dados_livro['totalItems'] > 0:
#             primeiro_resultado = dados_livro['items'][0]['volumeInfo']
#             return {
#                 'titulo': primeiro_resultado['title'],
#                 'autor': primeiro_resultado['authors'][0] if primeiro_resultado.get('authors') else 'Não encontrado',
#                 'editora': primeiro_resultado['publisher'] if primeiro_resultado.get('publisher') else 'Não encontrado',
#                 # Adicione outros campos conforme necessário
#             }
#         else:
#             return "Livro não encontrado."
#     else:
#         return "Erro ao buscar o livro."


# # Exemplo de uso:
# isbn_a_buscar = "978-8573280124"  # Substitua pelo ISBN desejado
# resultado = buscar_livro_por_isbn(isbn_a_buscar.replace('-',''))
# print(resultado)


""" Open Library"""
import requests

def buscar_livro_google_books(isbn):
    url = f"https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if 'items' in data:
            livro = data['items'][0]['volumeInfo']
            return {
                'titulo': livro['title'],
                'datapublicacao': livro['publishedDate'],
                'autores': livro['authors'],
                # 'editora': livro['publisher'],
                'numeropaginas': livro['pageCount'],
                'link': livro['infoLink'],
                'descricao': livro['description']
                # ... outros dados
            }
        else:
            return None
    else:
        return None

# Exemplo de uso
isbn = '9788581320359'
x = isbn.replace("-","")
print(x)

resultado = buscar_livro_google_books(x)
print(resultado)




def buscar_isbn_por_titulo(titulo):
    titulo = 'Evangelho'
    url = f"https://www.googleapis.com/books/v1/volumes?q={titulo}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if 'items' in data:
            livro = data['items'][0]['volumeInfo']
            if 'industryIdentifiers' in livro:
                for identifier in livro['industryIdentifiers']:
                    if identifier['type'] == 'ISBN_13':
                        return identifier['identifier']
    return None

print('----------- por titulo')
xxx == ""
xxx = buscar_isbn_por_titulo('kardec')
print(xxx)