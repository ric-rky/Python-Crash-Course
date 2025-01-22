import cmath


def quad_eq_coef():
    """Assimila os coeficientes da equação quadrática ax^2 + bx + c e calcula o discriminante"""
    a = float(input("Insira aqui o coeficiente do termo x^2 da equação quadrática: "))

    # O coeficiente dominante 'a' deve ser não-nulo
    while a == 0:
        print("O coeficiente dominante deve ser não-nulo! Tente novamente.")
        a = float(input("Insira aqui o coeficiente do termo x^2 da equação quadrática: "))

    b = float(input("Insira aqui o coeficiente do termo x da equação quadrática: "))
    c = float(input("Insira aqui o coeficiente do termo independente da equação quadrática: "))

    return a, b, c


def quad_eq_solver(a, b, c):
    """Resolve a equação quadrática de coeficientes a, b e c"""
    D = b ** 2 - 4 * a * c

    if D > 0:
        # Duas raízes reais x1 e x2
        x1 = (-b + cmath.sqrt(D)) / (2 * a)
        x2 = (-b - cmath.sqrt(D)) / (2 * a)
        return x1.real, x2.real  # As raízes são reais, então pegamos apenas a parte real
    elif D == 0:
        # Uma única raiz real
        x = - b / (2 * a)
        return x
    else:
        # Raízes complexas
        x1 = (-b + cmath.sqrt(D)) / (2 * a)
        x2 = (-b - cmath.sqrt(D)) / (2 * a)
        return x1, x2

# Imprime as raízes da equação
a, b, c = quad_eq_coef()
rts = quad_eq_solver(a, b, c)
if isinstance(rts, tuple):
    print(f"As raízes da equação são {rts[0]} e {rts[1]}.")
else:
    print(f"A raiz da equação é {rts}.")
