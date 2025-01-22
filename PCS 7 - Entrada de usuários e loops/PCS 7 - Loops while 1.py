current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

prompt = "\nTell me something and I will repeat it back to you."
prompt += "\nEnter 'quit' to enter the program."

something = ""
while something != 'quit':
    something = input(prompt)

    if something != 'quit':
        print(something)

prompt = f"\nEnter the name of a city you visited: "
prompt += f"\nEnter 'quit' to stop."

while True:
    city = input(prompt)

    if city == 'quit'.lower():
        break
    else:
        print(f"{city.title()} is a nice city!")

init_number = 0

while init_number <= 10:
    if init_number % 2 == 0:
        init_number += 1
        continue
    else:
        print(init_number)
        init_number += 1

# 7.4
#Input do pedido
pizza_order = "\nPlease, enter the ingredients of your pizza: "
pizza_order += "\nEnter 'quit' to finish."

ingredients = []

while True:

    pizza = input(pizza_order)

    if pizza.lower() == 'quit':
        break

    ingredients.append(pizza)

print(f"\nYour pizza is being made!")
print(f"\nYour pizza will have the following ingredients: ")
for ingredient in ingredients:
    print(f"- {ingredient}")


# 7.5
age_prompt = "\nWhat's your age? "
age_prompt += "\nEnter 'quit' to finish."

while True:
    age_input = input(age_prompt)

    if age_input.lower() == 'quit':
        break

    try:
        cinema_age = int(age_input)
    except ValueError:
        print("Please enter a valid age or 'quit' to exit.")
        continue

    if cinema_age < 3:
        print("Your ticket is free.")
    elif 3 <= cinema_age <= 12:
        print("Your ticket's price is US$ 10.")
    else:
        print("Your ticket's price is US$ 15.")

print("Thank you for using the cinema ticketing system.")



















