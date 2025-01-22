from usuarios import User

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
    def __init__(self, first_name, last_name, age, year, formation, ocupation, privileges):
        super().__init__(first_name, last_name, age, year, formation, ocupation)
        # Inicializa privileges como uma lista vazia se nenhum privilégio for passado
        self.privileges = Privileges(privileges)