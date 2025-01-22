pets = ['dog', 'cat', 'fish', 'dog', 'rabbit', 'cat', 'bird', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)

responses = {}
# Define uma flag para sinalizar que a pesquisa está ativa
polling_active = True

# Solicita o nome e a resposta do participante
while polling_active:
    name = input(f"\nWhat is your name?")
    response = input(f"\nWhich mountain would you like to climb today?")

    #Armazena a resposta no dicionário
    responses[name] = response

    #Detecta se mais alguém participará da pesquisa
    repeat = input(f"Would you like to let another person respond? (yes/no)").lower()
    if repeat == 'no':
        polling_active = False
        print(f"Ending poll.")
    elif repeat == 'yes':
        polling_active = True

#A pesquisa está completa. Mostra os resultados.
print(f"\n --- Poll results: ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")

# 7.8
# Lista com sanduíches
sandwich_orders = [
    "BLT (Bacon, Lettuce, and Tomato)",
    "Ham and Cheese",
    "Turkey Club",
    "Grilled Cheese",
    "Chicken Salad",
    "Egg Salad",
    "Tuna Salad",
    "Reuben",
    "French Dip",
    "Italian Sub",
    "Philly Cheesesteak",
    "Meatball Sub",
    "Pulled Pork",
    "Veggie",
    "Caprese",
    "Cuban",
    "Roast Beef",
    "Muffuletta",
    "Falafel",
    "Shrimp Po' Boy"
]

finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    finished_sandwiches.append(current_sandwich)
    print(f"Seu sanduíche {current_sandwich} está sendo preparado!")

print(f"Os seguintes sanduíches foram preparados: ")
for sandwich in finished_sandwiches:
    print(sandwich.title())

# 7.9
sandwich_orders = [
    "BLT (Bacon, Lettuce, and Tomato)",
    "Ham and Cheese",
    "Turkey Club",
    "Grilled Cheese",
    "Chicken Salad",
    "Egg Salad",
    "Pastrami",
    "Tuna Salad",
    "Reuben",
    "French Dip",
    "Italian Sub",
    "Philly Cheesesteak",
    "Meatball Sub",
    "Pulled Pork",
    "Veggie",
    "Caprese",
    "Cuban",
    "Pastrami",
    "Roast Beef",
    "Muffuletta",
    "Falafel",
    "Pastrami",
    "Shrimp Po' Boy"
]

while "Pastrami" in sandwich_orders:
    sandwich_orders.remove("Pastrami")
print(f"Sorry, we've run out of Pastrami.")

finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    finished_sandwiches.append(current_sandwich)
    print(f"Seu sanduíche {current_sandwich} está sendo preparado!")

print(f"Os seguintes sanduíches foram preparados: ")
for sandwich in finished_sandwiches:
    print(sandwich.title())

# 7.10
responses = {}

trip_poll = True
while trip_poll:
    name = input(f"What is your name?")
    response = input(f"Which place in the world would you like to visit?")

    responses[name] = response

    # Detecta se mais alguém participará da pesquisa
    repeat = input(f"Would you like to let another person respond? (yes/no)").lower()
    if repeat == 'no':
        trip_poll = False
        print(f"Ending poll.")
    elif repeat == 'yes':
        trip_poll = True

# A pesquisa está completa. Mostra os resultados.
print(f"\n --- Poll results: ---")
for name, response in responses.items():
    print(f"{name.title()} would like to visit {response.title()}.")
