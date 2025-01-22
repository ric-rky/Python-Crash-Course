try:
    print(5/0)
except ZeroDivisionError:
    print(f"You can't divide by zero!")

print(f"\nIsso é um espaço.\n")

print(f"Give me two numbers and I'll divide them.")
print(f"Press 'q' to quit.")

def divide_two():
    while True:
        n_1 = input(f"First number: ")
        if n_1.lower() == 'q':
            print(f"See you later!")
            break

        try:
            n_1 = int(n_1)
        except ValueError:
            print(f"You must enter a valid integer! Try again.")
            continue

        n_2 = input(f"Second number: ")
        if n_2.lower() == 'q':
            print(f"See you later!")
            break

        try:
            n_2 = int(n_2)
        except ValueError:
            print(f"You must enter a valid integer! Try again.")
            continue

        try:
            result = n_1/n_2
            print(f"The result of your division is {result}.")
        except ZeroDivisionError:
                print(f"You can't divide by zero!")

divide_two()

