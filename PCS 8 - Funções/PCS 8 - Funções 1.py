def greet_user(username):
    "Exibe um simples cumprimento."
    print(f"Hello, {username}!")

greet_user("Cake")

# 8.1
def display_message():
    print("I'm learning Python functions!")

display_message()

# 8.2
def favorite_book(book_name):
    print(f"One of my favorite books is {book_name.title()}!")

favorite_book("book name")

def describe_pet(pet_type, pet_name):
    print(f"\nI have a {pet_type}.")
    print(f"My {pet_type}'s name is {pet_name.title()}!")

describe_pet('cachorrinha', 'sara')
describe_pet('cachorrinha', 'nivea')
describe_pet(pet_name='nivea',pet_type='cachorrinha')

def describe_dog(pet_name, pet_type = 'dog'):
    print(f"\nI have a {pet_type} whose name is {pet_name.title()}.")

describe_dog('toq')

# 8.3
def make_shirt(tamanho, texto):
    print(f"\nSua camiseta de tamanho {tamanho}, cuja estampa é '{texto.upper()}', está sendo confeccionada!")
make_shirt('G', 'Data science is cool.')
make_shirt(tamanho = 'G', texto = 'Data science is cool.')

# 8.4
def make_shirt(tamanho = 'G', texto = 'Eu amo Python.'):
    print(f"\nSua camiseta de tamanho {tamanho}, cuja estampa é '{texto.upper()}', está sendo confeccionada!")
make_shirt()

make_shirt()
make_shirt(tamanho = 'M', texto = 'Eu amo Python.')
make_shirt(tamanho = 'P', texto = 'Live to win.')

# 8.5
def describe_city(city_name, country = 'bostil'):
    print(f"\nA cidade {city_name.title()} fica no país {country.title()}.")
describe_city('bostinhos', 'bostil')
describe_city('bostinhos')
describe_city('sp')
describe_city('hell de janegro')
describe_city('New York', 'United States')

def get_formatted_name(first_name, last_name):
    """Retorna nome completo"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

momi = get_formatted_name('momi', 'chinchilinha')
print(momi)

def get_formatted_name(first_name, last_name, middle_name = ""):
    """Retorna nome completo"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

momi = get_formatted_name('momi', 'amorinha', 'chinchilinha')
print(momi)

def build_person(first_name, last_name):
    """Retorna um dicionário de informações sobre a pessoa"""
    # Cria um dicionário com os dados da pessoa
    person = {'first_name':first_name, 'last_name':last_name}

    # Constrói o nome completo
    full_name = f"{first_name} {last_name}".title()

    # Imprime a mensagem de saudação e o dicionário
    print(f"Hello, {full_name}! Here's a dictionary about you: ")
    print(person)

    return person

build_person('momi', 'amorinha')

def sum(a, b):
    print(f"Your sum of a = {a} and b = {b} is equal to: {a + b}.")
    return a + b

def inc_by_one(x):
    print(x + 1)

def greet_user(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    f_name = input(f"Tell me your first name (press 'q' to quit): ")
    if f_name == 'q':
        break  # Sai do loop se o usuário digitar 'q'

    l_name = input(f"Tell me your last name (press 'q' to quit): ")
    if l_name == 'q':
        break  # Sai do loop se o usuário digitar 'q'

    formatted_name = greet_user(f_name, l_name)
    print(f"\nHello, {formatted_name}!")

# 8.7
def make_album(artista, título, faixas = None):
    """Cria uma função que imprime um dicionário sobre o álbum musical"""
    if faixas:
        album = {'Artista': artista.title(), 'Título': título.title(), 'Faixas': faixas}
    else:
        album = {'Artista': artista.title(), 'Título': título.title()}

    return album

guns = make_album('guns', 'appetite for destruction', 12)
print(guns)

# 8.8
def make_album(artist, album):
    album_dict = {'Artist': artist.title(), 'Album': album.title()}
    return album_dict

while True:
    artist_name = input("Enter the artist name ('q' to quit): ")
    if artist_name.lower() == 'q':
        break

    album_name = input("Enter the album name ('q' to quit): ")
    if album_name.lower() == 'q':
        break

    # Create and print the album dictionary
    musical_album_dict = make_album(artist_name, album_name)
    print(musical_album_dict)

# Print the thank you message after the loop ends
print("Thank you for your time.")

def greet_name(users):
    """Exibe um simples hello para cada usuário na lista"""
    for user in users:
        msg = f"Hello, {user}!"
        print(msg)

usernames = ['hannah', 'ty', 'margot', 'tuq']
greet_name(usernames)

# Começa com alguns designs que precisam ser impressos
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Simula a impressão de cada design, até que não reste nenhum
# Passa cada design para completed_models após impressão
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model {current_design}.")
    completed_models.append(current_design)

#Exibe todos os modelos concluídos
print(f"\nThe following models have been printed: ")
for completed_model in completed_models:
    print(completed_model)

def print_models(unprinted_designs, current_design):
    """Simula a impressão de cada design, até que não reste nenhum.
Passa cada design para completed_models após impressão"""
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model {current_design}.")
    completed_models.append(current_design)

def show_completed_models(completed_models):
    """Exibe todos os modelos concluídos"""
    print(f"\nThe following models have been printed: ")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# 8.9
short_msg_list = ['Hi!', 'You will become a Data Scientist soon!', 'You are an excelent mathematician!']
def show_messages(messages):
    for msg in messages:
        print(msg)

show_messages(short_msg_list)

# 8.10
short_msg_list = ['Hi!', 'You will become a Data Scientist soon!', 'You are an excellent mathematician!']
sent_messages = []

def send_messages(short_msg_list, sent_messages):
    while short_msg_list:  # Continua enquanto houver mensagens na lista 'short_msg_list'
        next_msg = short_msg_list.pop()  # Remove e retorna a última mensagem da lista
        sent_messages.append(next_msg)  # Adiciona a mensagem removida à lista 'sent_messages'
    print(short_msg_list, sent_messages)  # Imprime as duas listas

send_messages(short_msg_list, sent_messages)

# Para manter a ordem da lista:

def send_messages(short_msg_list, sent_messages):
    while short_msg_list:
        next_msg = short_msg_list.pop(0)  # Remove e retorna o primeiro elemento da lista
        sent_messages.append(next_msg)  # Adiciona à lista 'sent_messages'
    print(short_msg_list, sent_messages)

send_messages(short_msg_list, sent_messages)

# 8.11
send_messages(short_msg_list[:], sent_messages)












