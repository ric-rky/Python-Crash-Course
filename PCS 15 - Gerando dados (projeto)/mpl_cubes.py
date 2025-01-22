import matplotlib.pyplot as plt

# 15.1
x_values = [x for x in range(1, 5001)]
y_values = [x ** 2 for x in x_values]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c = y_values, cmap = plt.cm.Blues, s = 1)

# Define o título do gráfico e os eixos do rótulo
ax.set_title("Cube numbers", fontsize = 24)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Cube of value", fontsize = 14)

# Define o tamanho dos rótulos de marcação de escala
ax.tick_params(labelsize = 14)

# Define o intervalo para cada eixo
#ax.axis([0, 5000, 0, 1000000])
#ax.ticklabel_format(style = 'plain')

plt.show()