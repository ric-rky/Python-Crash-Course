# Definindo um decorator
def meu_decorator(func):
    def wrapper():
        print("Algo que acontece antes da função.")
        func()  # Chamando a função original
        print("Algo que acontece depois da função.")
    return wrapper

# Usando o decorator na função
@meu_decorator
def diga_ola():
    print("Olá!")

# Chamando a função decorada
diga_ola()
