import requests
from operator import itemgetter

# Faz uma chamada de API e armazena a resposta.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Código de status: {r.status_code}")

# Processa informações sobre cada submissão.
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:5]:
    # Faz uma nova chamada de API para cada submissão.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    # Cria um dicionário para cada artigo.
    submission_dict = {
        'title': response_dict['title'],
        'link': f"http://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict.get('descendants', 0)
    }
    submission_dicts.append(submission_dict)

# Ordena as submissões pelo número de comentários.
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

# Exibe as submissões mais populares.
for submission_dict in submission_dicts:
    print(f"\nTítulo: {submission_dict['title']}")
    print(f"Link de discussão: {submission_dict['link']}")
    print(f"Comentários: {submission_dict['comments']}")
