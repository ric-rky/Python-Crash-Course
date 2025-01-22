# 9.13
from random import randint, choice, sample

class Die:
    """Uma classe que simula um lançamento de um dado"""
    def __init__(self, sides):
        """Inicializa o dado com o número de lados especificado"""
        self.sides = sides

    def roll_die(self):
        """Simula o lançamento do dado e exibe o resultado"""
        result = randint(1, self.sides)
        print(f"Você jogou o dado! O número da face após seu lançamento é {result}.")

#Dado de 6 lados
my_die = Die(6)
my_die.roll_die()

#Lança o dado 10 vezes
for launch in range(1, 11):
    my_die.roll_die()

print(f"\nIsso é um espaço.\n")

#Dado de 10 lados
my_second_die = Die(10)

#Lança o dado 10 vezes
for launch in range(1, 11):
    my_second_die.roll_die()

print(f"\nIsso é um espaço.\n")

#Dado de 20 lados
my_third_die = Die(20)

#Lança o dado 10 vezes
for launch in range(1, 10):
    my_third_die.roll_die()

# 9.14
# Criação da lista contendo 10 números e 5 letras
items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

# Seleção aleatória de 4 itens da lista
selected_items = sample(items, 4)

# Exibição da mensagem
print(f"Parabéns! O bilhete vencedor é:")
print(selected_items)

print(f"\nIsso é um espaço.")

# 9.15
# Gera 6 números aleatórios entre 1 e 60 e os ordena em ordem crescente
def generate_ticket():
    """Gera um bilhete com 6 números aleatórios entre 1 e 60"""
    ticket = sample(range(1, 61), 6)
    ticket.sort()
    return ticket

def find_winning_ticket(my_ticket):
    """Gera bilhetes vencedores até encontrar uma correspondência com o bilhete do usuário"""
    attempts = 0
    while True:
        winning_ticket = generate_ticket()
        attempts += 1
        if winning_ticket == my_ticket:
            return winning_ticket, attempts

# Gera o bilhete do usuário
my_ticket = generate_ticket()

# Encontra o bilhete vencedor
winning_ticket, attempts = find_winning_ticket(my_ticket)

# Imprime os resultados
print(f"Bilhete do usuário: {my_ticket}")
print(f"Bilhete vencedor: {winning_ticket}")
print(f"Número de tentativas: {attempts}")











