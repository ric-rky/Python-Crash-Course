from pathlib import Path

# 10.4
# Função que, ao inserir um nome, cria um arquivo .txt com esse nome
def guest_name_text():
    name = input("Diga seu nome e criarei um arquivo contendo-o: ")

    # Verifica se o nome não é vazio
    if name == '':
        print("Seu nome não pode ser vazio!")
    else:
        # Cria o arquivo com o nome 'guest.txt'
        guest_name = Path('guest.txt')
        guest_name.write_text(name)
        print(f"Arquivo 'guest.txt' foi criado com o nome '{name}'.")

guest_name_text()

# 10.5
def guests_names_text():
    '''Função que solicita vários nomes de convidados e escreve em um arquivo guest_book.txt'''
    path = Path('guest_book.txt')

    guest_names = []

    while True:
        name = input("Diga seu nome e criarei um arquivo contendo-o ('q' para sair): ")

        # Verifica se o usuário deseja sair
        if name == 'q':
            print("Processo concluído com sucesso. Volte sempre!")
            break

        # Verifica se o nome não é vazio
        if name == '':
            print("Seu nome não pode ser vazio!")
        else:
            guest_names.append(name)

    # Cria a string com os nomes e adiciona uma nova linha para cada convidado
    file_string = ''
    for name in guest_names:
        file_string += f"{name}\n"
    #    Escreve os nomes no arquivo
    path.write_text(file_string)

guests_names_text()





