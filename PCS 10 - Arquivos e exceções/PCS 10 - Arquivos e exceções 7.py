from pathlib import Path
import json

numbers = [2, 3, 5, 7, 11, 13]

path = Path('numbers.json')
contents = json.dumps(numbers)
path.write_text(contents)

# 10.11
path = Path('fav_number.json')

# Verifica se o arquivo existe antes de tentar lê-lo
if path.exists():
    contents = path.read_text()
    fav_num = json.loads(contents)
    print(f"Eu sei seu número favorito! É {fav_num}.")
else:
    print("Parece que você ainda não tem um número favorito salvo...")

