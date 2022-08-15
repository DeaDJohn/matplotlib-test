from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

#Crear un dado de seis caras
die_1 = Die(12)
die_2 = Die(12)

# Hace algunas tiradas y guarda los resultados en una lista.
results = []
for roll_num in range(5_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)


# Analiza los resultados.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range (2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

print (frequencies)

# Visualizar los resultados
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Resultado', 'dtick': 1}
y_axis_config = {'title': 'Frecuencia'}
my_layout = Layout(title='Resultados de 1000 tiradas de un dado de seis caras', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6.html')

