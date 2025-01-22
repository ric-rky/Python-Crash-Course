import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Continua criando passeios novos, desde que o programa esteja ativo
while True:
    # Cria um random walk
    rw = RandomWalk()
    rw.fill_walk()

    # Plota os pontos no passeio
    plt.style.use('classic')
    fig, ax = plt.subplots()
    ax.scatter(rw.x_values, rw.y_values, s=15)
    ax.set_aspect('equal')
    plt.show()

    keep_running = input(f"Make another walk? (y/n): ")
    if keep_running == 'n':
        break

