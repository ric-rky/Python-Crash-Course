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