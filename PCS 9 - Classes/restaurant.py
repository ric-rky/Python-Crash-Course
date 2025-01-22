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