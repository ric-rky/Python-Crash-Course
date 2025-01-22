name = input(f"Please, enter your name: ")
print(f"\nHello, {name}!")

prompt = "If you share your name, we can personalize the messages you see."
prompt += "What's your first name?"

name = input(prompt)
print(f"Hello, {name}!")

age = input("How old are you? ")
age = int(age)
if age >= 18:
    print(f"Your age is {age}.")
else:
    print(f"You need to be at least 18 years old. Try again.")
    age

number = input("Enter a number: ")
number = int(number)

list = []

if number % 2 == 0:
    list.append(number)
    list.append(number).append(number)
    list.append(number).append(number).append(number)
    print(f"Your number ({number}) is even, and the list with the next 3 numbers after it is: {list}")
else:
    list.append(number)
    list.append(number).append(number)
    list.append(number).append(number).append(number)
    print(f"Your number ({number}) is odd, and the list with the next 3 numbers after it is: {list}")





