from pathlib import Path
import csv

# Caminho para o arquivo CSV
path = Path("sitka_weather_07-2021_simple.csv")
my_file = path.read_text()

# Dividindo o conteúdo em linhas
lines = my_file.splitlines()

# Usando csv.reader para processar o arquivo
reader = csv.reader(lines)

# Convertendo o iterador para uma lista
data = list(reader)

# Acessando a linha desejada, por exemplo, a segunda linha (índice 2)
print(data[:4])  # Lembre-se que a indexação começa em 0, então [2] é a terceira linha

grid = \
[['.', '.', '.', '.', '.', '.'],
 ['.', 'O', 'O', '.', '.', '.'],
 ['O', 'O', 'O', 'O', '.', '.'],
 ['O', 'O', 'O', 'O', 'O', '.'],
 ['.', 'O', 'O', 'O', 'O', 'O'],
 ['O', 'O', 'O', 'O', 'O', '.'],
 ['O', 'O', 'O', 'O', '.', '.'],
 ['.', 'O', 'O', '.', '.', '.'],
 ['.', '.', '.', '.', '.', '.']]

for j in range(6):
    for i in range(9):
        print(grid[i][j], end = '')
    print()

print(len(grid))
