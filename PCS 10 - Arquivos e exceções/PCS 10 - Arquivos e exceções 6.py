from pathlib import Path

# 10.6
def num_sum():
    '''Pede dois números e retorna sua soma'''
    while True:
        try:
            first_num = input(f"Insira um número inteiro: ")
            n_1 = int(first_num) # Tenta converter a primeira entrada
            break # Sai do loop se a conversão for bem-sucedida
        except ValueError:
            print(f"A entrada deve ser um número inteiro! Tente novamente. ")
    while True:
        try:
            second_num = input(f"Insira o segundo número inteiro: ")
            n_2 = int(second_num) # Tenta converter a segunda entrada
            break # Sai do loop se a conversão for bem-sucedida
        except ValueError:
            print(f"A entrada deve ser um número inteiro! Tente novamente.")

    # Se ambos os números forem válidos, imprime a soma
    print(f"A soma dos dois números que você digitou, {n_1} e {n_2}, é {n_1 + n_2}.")

num_sum()

# 10.8
# Cria um arquivo com nomes de cachorros
#dog_path = Path('dogs.txt')
#dog_path.write_text('Salma, Sara, Nivea, Lolla')
# Cria um arquivo com nomes de gatos
#cat_path = Path('cats.txt')
#cat_path.write_text('Pablito, Pantrinho, Gorduchinha, Pelúcio')

dog_path = Path('dogs.txt')
cat_path = Path('cats.txt')

def pet_reader():
    '''Função que tenta ler os arquivos acima'''
    try:
        dog_content = dog_path.read_text()
        cat_content = cat_path.read_text()
    except FileNotFoundError:
        pass
        #print(f"Desculpe, não consegui encontrar os arquivos {dog_path} e {cat_path}. Tente novamente.")
    else:
        print(f"Os nomes de cães e gatos registrados são, respectivamente, {dog_content} e {cat_content}.")

pet_reader()

# 10.10
def word_count():
    '''Lê uma determinada palavra nas strings de um livro'''

    # Caminhos dos arquivos dos livros
    book_1 = Path('frankenstein.txt')
    book_2 = Path('romeo_and_juliet.txt')
    book_3 = Path('pride_and_prejudice.txt')

    words_1 = book_1.read_text(encoding='utf-8').lower().split()
    words_2 = book_2.read_text(encoding='utf-8').lower().split()
    words_3 = book_3.read_text(encoding='utf-8').lower().split()

    # Solicita a palavra que será contada
    word = input("Digite a palavra que deseja contar: ").lower()

    # Conta a ocorrência da palavra em cada livro
    count_1 = words_1.count(word)
    count_2 = words_2.count(word)
    count_3 = words_3.count(word)

    # Exibe o resultado
    print(f"A palavra '{word}' aparece {count_1} vezes em 'Frankenstein'.")
    print(f"A palavra '{word}' aparece {count_2} vezes em 'Romeu e Julieta'.")
    print(f"A palavra '{word}' aparece {count_3} vezes em 'Orgulho e Preconceito'.")

    return

word_count()




