import plotly.express as px
from die import Die

my_die = Die()

# Realiza alguns testes e armazena os resultados numa lista
results = []
for num in range(100):
    result = my_die.roll()
    results.append(result)

# Analisa os resultados, armazenando a quantidade que cada lado foi sorteado num dicionário
frequencies = {}
poss_results = range(1, my_die.num_sides + 1)
for value in poss_results:
    frequency = results.count(value)
    frequencies[value] = frequency

print(frequencies)

# Visualiza os resultados
fig = px.bar(x = poss_results, y = frequencies)
fig.show()

