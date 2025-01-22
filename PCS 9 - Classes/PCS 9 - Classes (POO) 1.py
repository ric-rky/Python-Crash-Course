class Dog:
    """Simples tentativa de modelar um cachorro"""
    def __init__(self, name, age):
        """Inicializa os atributos de nome e imagem"""
        self.name = name
        self.age = age

    def sit(self):
        """Simula um cachorro sentando em resposta a um comando"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simula um cachorro rolando em resposta a um comando"""
        print(f"{self.name} rolled over!")

sarinha = Dog('Sara', 8)
nivea = Dog('Nivea', 8)

print(f"Nossa cachorrinha {sarinha.name} tem {sarinha.age} anos, e nossa cachorrinha {nivea.name} também.")
sarinha.sit()
nivea.sit()
sarinha.roll_over()
nivea.roll_over()

# 9.1
class Restaurant:
    """Simula um restaurante"""
    def __init__(self, restaurant_name, cuisine_type):
        """Inicializa os atributos de nome de restaurante e tipo de cozinha"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Descreve informações sobre o restaurante"""
        print(f"The restaurant {self.restaurant_name} has cuisine type {self.cuisine_type}.")

    def open_restaurant(self):
        """Diz se o restaurante está aberto"""
        print(f"The restaurant {self.restaurant_name} is open.")

restaurant = Restaurant('La Parrilla', 'Argentine')
restaurant.describe_restaurant()
restaurant.open_restaurant()

# Se Class é uma classe arbitrária, com __init__(self, x_1, x_2, ..., x_n), então:
# my_instance = Class(a_1, a_2, ..., a_n) é uma INSTÂNCIA da classe Class;
# self.x_i = x_i dentro de um método da classe é equivalente a my_instance.x_i = x_i fora da classe;
# chamar arbitrary_class_function(self) dentro de um método da classe é a mesma coisa que
# my_instance.arbitrary_class_function() fora da classe, onde self é a referência a my_instance.

# 9.2
restaurant_1 = Restaurant('La Parrilla', 'Argentine')
restaurant_2 = Restaurant('Burger King', 'Fast Food')
restaurant_3 = Restaurant('Oliva Bistrô', 'Italian')
#Chamar o método describe_restaurant para os 3 restaurantes:
restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()

# 9.3
class User:
    """Inicia uma classe que armazena informações sobre usuários"""
    def __init__(self, first_name, last_name, age, year, formation, ocupation):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.year = year
        self.formation = formation
        self.ocupation = ocupation

    def greet_user(self):
        print(f"Saudações, {self.first_name.title()}!")

    def describe_user(self):
        """Retorna um dicionário com as informações do usuário"""
        user_dict = {
            'first_name': self.first_name.title(),
            'last_name': self.last_name.title(),
            'age': self.age,
            'year': self.year,
            'formation': self.formation.title(),
            'ocupation': self.ocupation.title()
        }

        print(f"Aqui está um resumo sobre você: \n {user_dict}")

riri = User('ricardo', 'filho', '28', '1996', 'mathematician', \
'data scientist')
momi = User('milena', 'bertolucci', '30', '1994', 'arquiteta', \
'arquitetinha chinchilinha')
pai = User('ricardo', 'pai', '58', '1965', 'advogado', \
'consultor de negócios')
mãe = User('denise', 'mamãe', '60', '1964', 'letras', \
'pesquisadora e professora')
riri.greet_user()
riri.describe_user()
momi.greet_user()
momi.describe_user()
pai.greet_user()
pai.describe_user()
mãe.greet_user()
mãe.describe_user()


