from random import randint

class Die:
    """Simula um único dado"""
    def __init__(self, num_sides = 6):
        """Gera um dado com 6 lados"""
        self.num_sides = num_sides

    def roll(self):
        """Retorna um valor aleatório entre 1 e o número de lados do dado"""
        return randint(1, self.num_sides)