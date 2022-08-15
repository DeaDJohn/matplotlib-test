import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds , s=10)

# Establece el título del gráfico y las etiquetas de los ejes.
ax.set_title("Números al cuadrado", fontsize=24)
ax.set_xlabel("Valor", fontsize=14)
ax.set_ylabel("Valor al cuadrado", fontsize=14)

# Establece el tamaño de las etiquetas de los puntos de los ejes.
ax.tick_params(axis='both', labelsize=14)

# Establece el rango de cada eje.
ax.axis([0, 1100, 0, 1100000])

plt.show()