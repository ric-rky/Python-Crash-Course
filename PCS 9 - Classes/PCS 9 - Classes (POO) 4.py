class Car:
    """Simples tentativa de reproduzir um carro"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Retorna um nome descritivo, elegantemente formatado"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Exibe uma frase mostrando a quilometragem do carro, em milhas"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Define a leitura do hodômetro para o valor fornecido."""
        """Rejeita a alteração se houver tentativas de reverter o hodômetro."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print(f"You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Adiciona a quantidade fornecida à leitura do hodômetro"""
        self.odometer_reading += miles

class Battery:
    """Simples tentativa de modelar uma bateria para um carro elétrico"""

    def __init__(self, battery_size):
        """Inicializa os atributos da bateria"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Exibe uma frase descrevendo o tamanho da bateria"""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def foo(self):
        print(f"Esse é um teste.")

    def get_range(self):
        """Exibe frase sobre a distância que o carro percorre com essa bateria"""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

    def update_battery(self):
        if self.battery_size != 65:
            self.battery_size = 65

class ElectricCar(Car):
    """Tentativa de reproduzir um carro elétrico"""

    def __init__(self, make, model, year):
        """Inicializa os atributos da classe-pai"""
        super().__init__(make, model, year)
        self.battery = Battery(10)

my_leaf = ElectricCar('nissan', 'leaf', '2024')
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()

print(f"\nEsse é um espaço.\n")

# 9.6
class Restaurant:
    """Simula um restaurante"""
    def __init__(self, restaurant_name, cuisine_type):
        """Inicializa os atributos de nome de restaurante e tipo de cozinha"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = None

    def describe_restaurant(self):
        """Descreve informações sobre o restaurante"""
        print(f"The restaurant {self.restaurant_name} has cuisine type {self.cuisine_type}.")

    def open_restaurant(self):
        """Diz se o restaurante está aberto"""
        print(f"The restaurant {self.restaurant_name} is open.")

    def set_number_served(self, client_number):
        """Define o número de clientes atendidos"""
        self.number_served = client_number
        print(f"The restaurant {self.restaurant_name} has served {self.number_served} clients.")

    def increment_number_served(self, client_number):
        self.number_served += client_number
        print(f"The restaurant {self.restaurant_name} has now served {self.number_served} clients.")

class IceCreamStand(Restaurant):
    """Criar a classe da sorveteria como sublcasse da classe Restaurant"""

    def __init__(self, restaurant_name, cuisine_type, flavors):
        """Inicializa os atributos da classe-mãe Restaurant (abaixo) e os específicos de IceCreamStand (acima)"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def display_flavors(self):
        print(f"The following flavors are available: ")
        for flavor in self.flavors:
            print(f"- {flavor}")

my_ice_cream = IceCreamStand('Random Restaurant', 'Sweets', ['Vanilla', \
'Chocolate', 'Strawberry', 'Pistacchio'])
print(my_ice_cream.restaurant_name)
print(my_ice_cream.flavors)
print(my_ice_cream.cuisine_type)
my_ice_cream.describe_restaurant()
my_ice_cream.display_flavors()

print(f"\nEsse é um espaço.\n")

class User:
    """Inicia uma classe que armazena informações sobre usuários"""
    def __init__(self, first_name, last_name, age, year, formation, ocupation):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.year = year
        self.formation = formation
        self.ocupation = ocupation
        self.login_attempts = 0

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

    def increment_login_attempts(self, attempts):
        self.login_attempts += attempts
        print(f"Your have {self.login_attempts} login attempts.")

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f"Your login attempts have been reseted to 0.")

class Admin(User):
    """Cria uma classe para o Admin, sublcasse da classe User"""
    def __init__(self, first_name, last_name, age, year, formation, ocupation, privileges = None):
        super().__init__(first_name, last_name, age, year, formation, ocupation)
        # Inicializa privileges como uma lista vazia se nenhum privilégio for passado
        if privileges is None:
            privileges = []
        self.privileges = privileges

    def show_privileges(self):
        """Exibe os privilégios do administrador"""
        if self.privileges:
            print(f"Privilégios do administrador:")
            for privilege in self.privileges:
                print(f"- {privilege}")
        else:
            print(f"Este usuário não tem privilégios de administrador.")

# Exemplo de uso
admin_user = Admin(
    'Ricardo', 'Bertolucci', None, None, \
'Mathematician', 'Data Scientist', ['can do everything he wants']
)

admin_user.show_privileges()

print(f"\nEsse é um espaço.\n")

# 9.8
class Privileges:

    def __init__(self, privileges):
        """Inicializa os privilégios"""
        # Inicializa privileges como uma lista vazia se nenhum privilégio for passado
        if privileges is None:
            privileges = []
        self.privileges = privileges

    def show_privileges(self):
        """Exibe os privilégios do administrador"""
        if self.privileges:
            print(f"Privilégios do administrador:")
            for privilege in self.privileges:
                print(f"- {privilege}")
        else:
            print(f"Este usuário não tem privilégios de administrador.")

class Admin(User):
    """Cria uma classe para o Admin, sublcasse da classe User"""
    def __init__(self, first_name, last_name, age, year, formation, ocupation, privileges = None):
        super().__init__(first_name, last_name, age, year, formation, ocupation)
        # Inicializa privileges como uma lista vazia se nenhum privilégio for passado
        if privileges is None:
            privileges = []
        self.privileges = Privileges()

riri = Admin(
    'Ricardo', 'Bertolucci', '28', '2025', 'Mathematician', \
    'Data Scientist', ['can do everything']
)
riri.privileges.show_privileges()

# 9.9
class Battery:
    """Simples tentativa de modelar uma bateria para um carro elétrico"""

    def __init__(self, battery_size = 75):
        """Inicializa os atributos da bateria"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Exibe uma frase descrevendo o tamanho da bateria"""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def foo(self):
        print(f"Esse é um teste.")

    def get_range(self):
        """Exibe frase sobre a distância que o carro percorre com essa bateria"""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

    def update_battery(self, new_size):
        """Atualiza o tamanho da bateria, se necessário."""
        if self.battery_size != new_size:
            self.battery_size = new_size
            print(f"O tamanho da bateria foi atualizado para {self.battery_size}-kWh.")
        else:
            print("O tamanho da bateria já está no valor desejado.")

class ElectricCar(Car):
    """Tentativa de reproduzir um carro elétrico"""

    def __init__(self, make, model, year):
        """Inicializa os atributos da classe-pai"""
        super().__init__(make, model, year)
        self.battery = Battery()

    def describe_car(self):
        """Descreve o carro."""
        print(f"{self.year} {self.make} {self.model}")

    def describe_battery(self):
        """Utiliza o método da classe Battery para descrever a bateria."""
        self.battery.describe_battery()

my_tesla = ElectricCar('Tesla', 'Model S', 2024)
my_tesla.battery.describe_battery()
print(my_tesla.battery.battery_size)
my_tesla.battery.battery_size = 100
print(my_tesla.battery.battery_size)




