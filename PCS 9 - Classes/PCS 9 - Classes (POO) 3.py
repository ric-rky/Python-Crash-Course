# 9.4
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


parrilla = Restaurant('La Parrilla', 'Argentine')
parrilla.set_number_served(1000)
parrilla.increment_number_served(3000)

print(f"\nEssa é uma quebra de linha!\n")

# 9.5
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

riri = User('riri', None, None, None, 'Mathematician', \
 'Data Scientist')
riri.login_attempts = 10
riri.increment_login_attempts(1)
riri.reset_login_attempts()

print(f"\nEssa é uma quebra de linha!\n")

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

class ElectricCar(Car):
    """Tentativa de reproduzir um carro elétrico"""
    def __init__(self, make, model, year):
        """Inicializa os atributos da classe-pai"""
        super().__init__(make, model, year)
        self.battery_size = 40

    def describe_battery(self):
        """Exibe uma frase descrevendo o tamanho da bateria"""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def fill_gas_tank(self):
        """Carros elétricos não têm gasolina!"""
        print(f"This car doesn't have a gas tank!")

my_leaf = ElectricCar('nissan', 'leaf', '2024')
print(my_leaf.get_descriptive_name())
my_leaf.describe_battery()
my_leaf.fill_gas_tank()
