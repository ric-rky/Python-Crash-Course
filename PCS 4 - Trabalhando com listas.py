# 4.1
pizza_list = ['pepperoni', 'bacon', 'milho com mussarela', 'atum']
for pizza in pizza_list:
    print(f"Gosto muito da pizza de {pizza}!")
print("Amo pizzas! :D")

# 4.3
num_list = [x for x in range(1, 21)]
print(num_list)

# 4.4
mil_list = list(range(1, 10 ** 6 + 1))
for x in mil_list:
    print(x)
    break

# 4.5
mil_list = list(range(1, 10 ** 6 + 1))
min_value = min(mil_list)
max_value = max(mil_list)

print(min_value, max_value)

# 4.6
odd_list = list(range(1, 20, 2))
for x in odd_list:
    print(x)

# 4.7
my_list = []
for value in range(3, 31):
    if value % 3 == 0:
        my_list.append(value)
        print(value)

# 4.8 e 4.9
cube_list = [n ** 3 for n in range(1, 11)]
print(cube_list)

players = ['charles', 'michael', 'florence', 'eli']
print(players[-3:])

# 4.10
my_list = list(range(3, 1772))
n = len(my_list)
middle_index = n//2
start_index = middle_index-1
end_index=middle_index+2
print(f"Os 3 primeiros elementos da lista são: {my_list[0:3]}.")
print(f"Os 3 elementos do meio da lista são: {my_list[start_index:end_index]}.")
print(f"Os 3 últimos elementos da lista são: {my_list[-3:]}.")

# 4.11
pizza_list = ['pepperoni', 'bacon', 'milho com mussarela', 'atum']
friend_pizzas = pizza_list[:]

pizza_list.append('carne seca')
friend_pizzas.append('frango')
for pizza in pizza_list:
    print(f"Minhas pizzas favoritas são: {pizza}.")
for pizza in friend_pizzas:
    print(f"As pizzas favoritas do meu amigo são: {pizza}.")

# 4.13
# Criação da tupla com cinco refeições simples
refeicoes_simples = ('macarrão com queijo', 'sanduíche de presunto e queijo', 'sopa de legumes', 'salada de frango', 'omelete')

# Imprimir cada refeição da tupla
for refeicao in refeicoes_simples:
    print(refeicao)
