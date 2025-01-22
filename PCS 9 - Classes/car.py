"""Classe que pode ser utilizada para representar um carro"""

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

    def __init__(self, battery_size = 40):
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