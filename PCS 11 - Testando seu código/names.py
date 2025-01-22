from name_function import get_formatted_name

print(f"Pressione 'q' a qualquer momento para sair.")
while True:
    first = input(f"\nInsira seu primeiro nome: ")
    if first == 'q':
        print(f"Volte sempre!")
        break
    middle = input(f"\nInsira seu nome do meio: ")
    if middle == 'q':
        print(f"Volte sempre!")
        break
    last = input(f"\nInsira seu último nome: ")
    if last == 'q':
        print(f"Volte sempre!")
        break

    formatted_name = get_formatted_name(first, last, middle)
    print(f"Seu nome, elegantemente formatado, é: {formatted_name}.")

