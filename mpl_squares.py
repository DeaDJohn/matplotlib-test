import matplotlib.pyplot as plt

input_values =[1, 2, 3, 4, 5]
squares = [1, 4 ,9, 16, 25]

plt.style.use('fivethirtyeight')
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

# Eestablece el tamaño de las etiquetas de los puntos de los ejes.
ax.set_title("Números cuadrados")
ax.set_xlabel("Valor", fontsize=14)
ax.set_ylabel("Valor al cuadrado", fontsize=14)

# Establece el tamaño de las etiquetas de los puntos de los ejes.
ax.tick_params(axis='both', labelsize=8)

plt.show()