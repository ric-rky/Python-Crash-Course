import random

familia_tatu = ['Ricardinho', 'Momi', 'Mamãe Denise', 'Papai Ricardo']

membros_sorteados = random.sample(familia_tatu, len(familia_tatu))

for member in membros_sorteados:
    print(member)
