import requests
from bs4 import BeautifulSoup

# URL da página de pesquisa do arXiv
url = "https://arxiv.org/search/?searchtype=all&query=math&abstracts=show&size=50&order="

# Faz a requisição para a página
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Verifica se a requisição foi bem-sucedida
if r.status_code == 200:
    # Faz o parsing do conteúdo HTML usando BeautifulSoup
    soup = BeautifulSoup(r.content, 'html.parser')

    # Encontra todos os títulos dos artigos
    titles = soup.find_all('p', class_='title is-5 mathjax')

    # Mostra os títulos dos primeiros 5 artigos
    for i, title in enumerate(titles[:5]):
        print(f"Artigo {i + 1}: {title.text.strip()}")
else:
    print("Erro ao acessar a página.")
