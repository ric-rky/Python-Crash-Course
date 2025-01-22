import plotly.express as px
from die import Die

# Cria 3 dados D6
die_1 = Die()
die_2 = Die()
die_3 = Die()

# Lança os três dados 1000 vezes e armazena os resultados numa lista
results = []
for roll_num in range(1001):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)

# Analisa os resultados
frequencies = {}
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
poss_results = range(3, max_result + 1)
for value in poss_results:
    frequency = results.count(value)
    frequencies[value] = frequency

# Visualiza os resultados
title = "Results of Rolling Three D6 Dice 1000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x = poss_results, y = frequencies, title = title, labels = labels)

# Personaliza ainda mais o gráfico
fig.update_layout(xaxis_dtick = 1)

fig.show()