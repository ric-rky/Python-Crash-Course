import plotly.express as px
from die import Die

# Cria dois dados D8
d_1 = Die(8)
d_2 = Die(8)

# Realiza alguns 1000 lançamentos e os armazena numa lista
results = []
max_range = 10 ** 8
for roll_num in range(max_range + 1):
    result = d_1.roll() + d_2.roll()
    results.append(result)

# Analisa os resultados
frequencies = {}
max_result = d_1.num_sides + d_2.num_sides
poss_results = range(2, max_result + 1)
for value in poss_results:
    frequency = results.count(value)
    frequencies[value] = frequency

# Visualiza os resultados
title = f"Results of Rolling Two D6 Dice {max_range} Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x = poss_results, y = frequencies, title = title, labels = labels)

# Personaliza ainda mais o gráfico
fig.update_layout(xaxis_dtick = 1)

fig.show()