from random import choice

class RandomWalk:
    """Classe para gerar passeios aleatórios"""

    def __init__(self, num_points = 5000):
        """Inicializa os atributos de um passeio"""
        self.num_points = num_points

        # Todos os passeios começam no ponto (0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Calcula todos os pontos do passeio"""

        # Continua dando passos até que o passeio atinja o comprimento desejado

        while len(self.x_values) < self.num_points:

            #Decide qual direção tomar, e até onde ir
            x_direction = choice([1, - 1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, - 1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # Rejeita movimentos que não vão a lugar algum
            if x_step == 0 and y_step == 0:
                continue

            # Calcula a nova posição
            x = self.x_values[- 1] + x_step
            y = self.y_values[- 1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

    def get_step(self):
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4])
        step = direction * distance

        return step









