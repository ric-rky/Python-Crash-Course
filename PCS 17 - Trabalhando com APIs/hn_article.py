import requests
import json

# Cria uma chamada de API e armazena a resposta
url = "https://hacker-news.firebaseio.com/v0/item/31353677.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Explora a estrutura dos dados
response_dict = r.json()
response_string = json.dumps(response_dict, indent = 4)
print(response_string, response_dict['url'])