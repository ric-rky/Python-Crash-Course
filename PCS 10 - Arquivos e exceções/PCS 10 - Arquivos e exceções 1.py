from pathlib import Path

# Lê o arquivo pi_digits.txt
path = Path("C:\\Users\\ricar\\OneDrive\\Documentos\\Python Study Files\\pi_million_digits.txt")
contents = path.read_text().strip()
# print(contents)

# Função que armazena cada dígito de pi em pi_digits.txt e o número de vezes que esse dígito aparece num dict
def digit_count(contents):
    digit_dict = {}
    for digit in contents:
        if digit.isdigit():
            if digit in digit_dict:
                digit_dict[digit] += 1
            else:
                digit_dict[digit] = 1
    return digit_dict

pi_dict = digit_count(contents)
print(pi_dict)

print(f"\nIsso é um espaço.\n")

# Função para checar se uma data de aniversário está no primeiro milhão de dígitos de Pi

def pi_birthday():
    pi_string = ''
    lines = contents.splitlines()
    for line in lines:
        pi_string += line.strip()

    birthday = input(f"Insira sua data de aniversário no formato ddmmaa: ")
    if birthday in pi_string:
        print(f"Seu aniversário aparece nos primeiros 1 milhões de dígitos de Pi!")
    else:
        print(f"Seu aniversário não aparece nos primeiros 1 milhões de dígitos de Pi!")

pi_birthday()











