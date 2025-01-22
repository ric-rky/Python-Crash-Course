favorite_languages = {
    "muq": "C",
    "kuq": "R",
    "tuq": "C++",
    "luq": "python",
}

language = favorite_languages['muq'].title()
print(f"Muq's favorite language is {language}.")

########

alien_0 = {'color': 'green', 'speed': 'slow'}
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)

# 6.1
momi_chinchilinha = {'Namorado': 'Riri', 'Cidade': 'Ourinhos', 'Profissão': 'Arquiteta', 'Comida Preferida': 'Docinho'}
print(f"A Momi namora o {momi_chinchilinha['Namorado']}, mora em {momi_chinchilinha['Cidade']}, \
trabalha como {momi_chinchilinha['Profissão']} e gosta muito de {momi_chinchilinha['Comida Preferida']}.")
print(momi_chinchilinha.items())

# 6.2
# Definindo o dicionário com nomes e números favoritos
favoritos = {
    'Ana': 7,
    'Bruno': 12,
    'Carla': 3,
    'Diego': 15,
    'Elena': 8
}

# Exibindo o nome de cada pessoa e seu número favorito
for nome, numero in favoritos.items():
    print(f"{nome} tem o número favorito {numero}.")

# 6.3
# Construindo o dicionário com termos
my_dict = {'Python': 
           'Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation',
           'String': 'In computer programming, a string is traditionally a sequence of characters, either as a literal constant or as some kind of variable.',
           'Variable': 'In computer programming, a variable is an abstract storage location paired with an associated symbolic name, which contains some known or unknown quantity of data or object referred to as a value; or in simpler terms, a variable is a named container for a particular set of bits or type of data (like integer, float, string, etc...).',
           'Source code': 'In computing, source code, or simply code or source, is a plain text computer program written in a programming language. A programmer writes the human readable source code to control the behavior of a computer.'
           }
# Exibir a palavra e seu significado:
for termo, significado in my_dict.items():
    print(f"{termo}: {significado}\n")

user_0 = {
    'username': 'efermi', 
    'first': 'enrico',
    'last': 'fermi',
}

for key, item in user_0.items():
    print(f"\n Key: {key},\n Item: {item}.")

# 6.5
rivers = {'nile':'egypt', 'ganges':'india', 'seine':'france', 'po':'italy'}
for river, country in rivers.items():
    print(f"The {river.title()} river crosses {country.title()}.")

# 6.6
favourite_languages = {
    'jen':'python', 
    'sarah':'c',
    'edward':'rust', 
    'phil':'python',
    'carmen':'typescript',
    'vergil':'c#',
    'dante':'sql',
    'dennis':'none'
}

for name, language in favourite_languages.items():
    if name != 'dennis':
        print(f"Hello {name.title()}, I see you like {language.title()}!")
    else:
        print(f"{name.capitalize()}! Stop chainsawing and learn a damn programming language!")
if 'moker' not in favourite_languages:
    print(f"You too, Makima!")

######################################

aliens = []

# Criar 30 alienígenas 
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# Exibir os primeiros 5 alienígenas
for alien in aliens[:5]:
    print(alien)
print('...')

# Exibir quantos alienígenas foram criados
print(f"Total number of aliens: {len(aliens)}")

######################################

pizza = {
    'crust':'thick', 
    'toppings':['mushrooms', 'extra cheese']
}

print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping.title()}")

######################################

favorite_languages_new = {
    'jen':['python','rust'],
    'sarah':['c'],
    'edward':['rust','go'],
    'phill':['python','haskell']
}

for n, l in favorite_languages_new.items():
    print(f"\n{n.title()} favorite languages are:")
    for language in l:
        print(f"{language.title()}")

######################################

users = {
    'aenstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton'
    },

    'mcurie': {
        'first': 'marie',
        'last': 'curie', 
        'location': 'paris'
    }
}

for username, userinfo in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{userinfo['first']} {userinfo['last']}"
    location = f"{userinfo['location']}"

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")

# 6.7
momi_chinchilinha = {
    'Namorado': 'Riri', 
    'Cidade': 'Ourinhos', 
    'Profissão': 'Arquiteta', 
    'Comida Preferida': 'Docinho'
}

riri_panetoninho = {
    'Namorada': 'Momi', 
    'Cidade': 'Ourinhos', 
    'Profissão': 'Matemático e Cientista de Dados', 
    'Comida Preferida': 'Carne'
}

people = [momi_chinchilinha, riri_panetoninho]

for person in people:
    if 'Namorado' in person:
        print(f"{person['Namorado']}'s girlfriend lives in {person['Cidade']}, works as an {person['Profissão']}, and loves {person['Comida Preferida']}.")
    else:
        print(f"{person['Namorada']}'s boyfriend lives in {person['Cidade']}, works as a {person['Profissão']}, and loves {person['Comida Preferida']}.")

# 6.8
sarinha = {
    'nome':'sara',
    'comida preferida':'franguinho e carninha',
    'nome dos donos':'família tatu',
    'idade':'8',
    'cidade':'ourinhos'
}

nivea = {
    'nome':'nivea',
    'comida preferida':'tudo',
    'nome dos donos':'família tatu',
    'idade':'8',
    'cidade':'ourinhos'
}

cachorrinhas = [sarinha,nivea]

for cachorrinha in cachorrinhas:
    nome = cachorrinha['nome'].capitalize()
    idade = cachorrinha['idade']
    comida = cachorrinha['comida preferida']
    cidade = cachorrinha['cidade']
    donos = cachorrinha['nome dos donos'].capitalize()

    print(f"{nome} é uma cachorrinha que tem {idade} anos, gosta de comer {comida}, e mora em {cidade} com a {donos}.")

# 6.9
favorite_places = {
    'momi':['foz do iguaçu', 'são paulo', 'londrina'], 
    'riri':['são paulo', 'londrina', 'europa']
    }

for person in favorite_places:
    print(f"Os lugares favoritos de {person.title()} são:")
    for place in favorite_places[person]:
        print(f"- {place.title()}")
    print()  # Adiciona uma linha em branco para separar cada pessoa

# 6.11
    # Dicionário com as cidades

    cities = {
        'ourinhos': {
            'estado': 'sp',
            'população': '114.352',
            'idh': '0.778'
        },
        'são josé do rio preto': {
            'estado': 'sp',
            'população': '480.439',
            'idh': '0.797'
        },
        'resende': {
            'estado': 'rj',
            'população': '133.244',
            'idh': '0.768'
        }
    }
    
    for city, info in cities.items():
        print(f"A cidade {city.title()}, localizada no estado de {info['estado'].upper()}, possui uma população de {info['população']} habitantes e um IDH de {info['idh']}, considerado alto.")



