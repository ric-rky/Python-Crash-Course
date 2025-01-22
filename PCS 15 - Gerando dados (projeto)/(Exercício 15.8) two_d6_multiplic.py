import plotly.express as px

from die import Die

# Cria dois dados D6
die_1 = Die()
die_2 = Die()

# Realiza alguns testes e armazena os resultados numa lista
results = []
for roll_num in range(50000 + 1):
    result = die_1.roll() * die_2.roll()
    results.append(result)

# Analisa os resultados
frequencies = {}
max_result = die_1.num_sides * die_2.num_sides
poss_results = range(1, max_result + 1)
for value in poss_results:
    frequency = results.count(value)
    frequencies[value] = frequency

# Visualiza os resultados
title = "Results of Multiplying Two D6 Dice 50000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x = poss_results, y = frequencies, title = title, labels = labels)

# Personaliza ainda mais o gráfico
fig.update_layout(xaxis_dtick = 1)

fig.show()