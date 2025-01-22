def make_pizza(*toppings):
    """Exibe a lista de ingredientes"""
    print(f"\nMaking a pizza with the following ingredients: ")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

def make_pizza(size, *toppings):
    """Exibe a lista de ingredientes da pizza e o tamanho"""
    print(f"\nMaking a {size}-inch pizza with the following ingredients: ")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(12, 'pepperoni', 'extra cheese', 'red pepper')

# *args = passa como uma tupla pela função, **kwargs = passa como um dicionário pela função

def user_build(first, last, **user_info):
    """**user_info cria um dicionário contendo as informações que o usuário adicionar"""
    user_info['first name'] = first
    user_info['last name'] = last
    return user_info

riri = user_build('Ricardo', 'Bertolucci', Location = 'Ourinhos', Profession = 'Data Scientist and Mathematician')
print(riri)

# 8.12
def sandwich_maker(*ings):
    """Exbie os ingredientes do sanduíche"""
    print(f"Your sandwich, with the following ingredients, is being made: ")
    for ing in ings:
        print(f"- {ing.title()}.")

sandwich_maker('pimenta', 'geleia de cebola', 'bacon', 'queijo mussarela', 'hambúrguer angus')

# 8.14
def car_info(manufacturer, name, **general):
    general['manufacturer'] = manufacturer
    general['name'] = name
    return general

car = car_info('honda', 'civic', color = 'black', year = '2024')
print(car)

