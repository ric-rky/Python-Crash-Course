from pathlib import Path
import json

def get_fav_number():
    '''Pergunta qual o número favorito do usuário'''
    while True:
        try:
            fav_num = int(input(f"What's your favorite number? "))
            break
        except ValueError:
            print(f"Please enter a valid integer.")

    path = Path('fav_number.json')
    contents = json.dumps(fav_num)
    path.write_text(contents)
    print(f"Your favorite number {fav_num} has been saved.")

get_fav_number()