# 5.1
car = 'subaru'
print(car == 'subaru')

print("\nIs car == 'audi'? I don't think so.")
print(car == 'audi')

# 5.3
alien_color = ['green', 'yellow', 'red']

# Função para solicitar uma cor válida
def solicitar_cor():
    color = input("Please, choose a color between 'green', 'yellow' and 'red'.").lower()
    while color not in alien_color:
        print("Please enter a valid color.")
        color = input("Please, choose a color between 'green', 'yellow' and 'red': ").lower()
    return color

# Solicitar uma cor válida
color = solicitar_cor()

if color == 'green':
    print("Congratulations, you won 5 points!")
elif color == 'yellow':
    print("Congratulations, you won 10 points!")
elif color == 'red':
    print("Congratulations, you won 15 points!")

# 5.7
# Lista de frutas favoritas
fav_fruits = ['kiwi', 'banana', 'morango', 'uva', 'manga']

# Fruta a ser verificada
fruit = input("Digite o nome de uma fruta: ").lower()

# Verificar se a fruta está na lista de frutas favoritas
if fruit in fav_fruits:
    print(f"Sim, eu gosto de {fruit}!")
else:
    print(f"Não, eu não gosto de {fruit}.")

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for item in requested_toppings:
    print(f"Adding {item}!")
print(f"\nYour pizza is done!")

# 5.8
user = input("Enter your name: ").lower()  #Converte a entrada para minúsculas para comparação

user_list = ['tuluk', 'luq', 'admin', 'koune', 'kouk']

#Verifica se o usuário fornecido está na lista
if user in user_list:
    if user == 'admin':
        print(f"Hello admin!")
    else:
        print(f"Hello again {user}.")
else:
    print(f"User {user} not found.")

# 5.9
user = input("Enter your name: ").lower()  # Converte a entrada para minúsculas para comparação

user_list = ['tuluk', 'luq', 'admin', 'koune', 'kouk']

# Verifica se a lista de usuários está vazia
if not user_list:
    print("É necessário encontrar algum usuário!")
else:
    # Verifica se o usuário fornecido está na lista
    if user in user_list:
        if user == 'admin':
            print(f"Hello admin!")
        else:
            print(f"Hello again {user}.")
    else:
        print(f"User {user} not found.")

# 5.10
#lista de usuários
current_users = ['tuluk', 'luq', 'admin', 'koune', 'kouk', 'puq', 'muq']

#lista de novos usuários
new_users = ['luq', 'puq', 'kek', 'qiq', 'batuq']

#converter os nomes da lista para minúsculo
current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Sorry, this user name {new_user} is already in use.")
    else:
        print(f"The user name {new_user} is available.")

# 5.11
num_list = list(range(1,10))
for num in num_list:
    if num == 1:
        print(f"1st number.")
    if num == 2:
        print(f"2nd number.")
    if num == 3:
        print(f"3rd number.")
    if num >= 4:
        print(f"{num}th number.")

        
