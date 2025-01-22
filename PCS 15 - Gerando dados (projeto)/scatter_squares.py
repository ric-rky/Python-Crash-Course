import matplotlib.pyplot as plt

x_values = [x for x in range(1, 1001)]
y_values = [x ** 2 for x in x_values]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c = y_values, cmap = plt.cm.Blues, s = 1)

# Define o título do gráfico e os eixos do rótulo
ax.set_title("Square numbers", fontsize = 24)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Square of value", fontsize = 14)

# Define o tamanho dos rótulos de marcação de escala
ax.tick_params(labelsize = 14)

# Define o intervalo para cada eixo
ax.axis([0, 1100, 0, 1_100_000])
ax.ticklabel_format(style = 'plain')

plt.show()