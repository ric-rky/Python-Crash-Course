def make_pizza(size, *toppings):
    """Exibe a lista de ingredientes da pizza e o tamanho"""
    print(f"\nMaking a {size}-inch pizza with the following ingredients: ")
    for topping in toppings:
        print(f"- {topping}")

