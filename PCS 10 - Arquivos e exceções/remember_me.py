from pathlib import Path
import json

def get_stored_user_info(path):
    '''Obtém as informações do usuário armazenadas, se disponíveis'''
    if path.exists():
        contents = path.read_text()
        user_info = json.loads(contents)
        return user_info
    else:
        return None

def get_new_user_info(path):
    '''Solicita novas informações do usuário'''
    username = input("What's your name? ").title()
    age = input("How old are you? ")
    city = input("Which city do you live in? ").title()

    user_info = {
        'username': username,
        'age': age,
        'city': city
    }

    contents = json.dumps(user_info)
    path.write_text(contents)
    return user_info

def greet_user():
    '''Cumprimenta o usuário com base nas informações armazenadas'''

    path = Path('user_info.json')
    user_info = get_stored_user_info(path)

    if user_info:
        username = user_info['username']
        correct_user = input(f"Is your name {username}? (yes/no): ").strip().lower()

        if correct_user == 'yes':
            age = user_info['age']
            city = user_info['city']
            print(f"Welcome back, {username}!")
            print(f"We see that you are {age} years old and live in {city}.")
        else:
            print("Let's update your information.")
            user_info = get_new_user_info(path)
            username = user_info['username']
            print(f"We'll remember you, {username}!")
    else:
        user_info = get_new_user_info(path)
        username = user_info['username']
        print(f"We'll remember you, {username}!")

greet_user()
