from pathlib import Path

#my_book_path = Path('this_does_not_exist.txt')

#try:
    #my_book = my_book_path.read_text()
#except:
    #print(f"Sorry, the file {my_book_path} does not exist.")

print(f"\nIsso é um espaço.\n")

def word_count(my_book_path):
    '''Conta o número de palavras num arquivo'''
    try:
        my_book_contents = my_book_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Sorry, the file {my_book_path} does not exist.")

    else:
        #Conta o número de palavras num arquivo
        words = my_book_contents.split()
        word_number = len(words)
        print(f"The file {my_book_path} has about {word_number} words.")

#my_book_path = Path("romeo_and_juliet.txt")
#word_count(my_book_path)

print(f"\nIsso é um espaço.\n")

book_list = [
    'romeo_and_juliet.txt',
    'frankenstein.txt',
    'pride_and_prejudice.txt',
    'elements_of_euclid.txt'
]

for book in book_list:
    my_book_path = Path(book)
    word_count(my_book_path)






