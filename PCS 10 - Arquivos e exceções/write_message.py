from pathlib import Path

# Definir o caminho do arquivo
path = Path('programming.txt')

# Escrever o texto inicial no arquivo
path.write_text('I love programming and I will get rich with it!\n')

# Ler e imprimir o arquivo
my_text = path.read_text()
print(my_text)

# Adicionar mais texto
my_text += 'I will succeed and I will become a Data Analyst/Scientist!\n'
my_text += 'And I will make my parents proud!\n'
my_text += 'I also love working with data.\n'

# Escrever o texto atualizado no arquivo
path.write_text(my_text)

#Ler e imprimir o conteúdo atualizado do arquivo
updated_text = path.read_text()
print(updated_text)