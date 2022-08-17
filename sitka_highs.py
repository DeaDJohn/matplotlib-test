import csv

import matplotlib.pyplot as plt

from datetime import datetime

# Tiempo de Julio
#filename = 'weather_data/sitka_weather_07-2018_simple.csv'
# Tiempo del año
filename = 'weather_data/sitka_weather_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    #for index, column_header in enumerate(header_row):
    #   print(index, column_header)

    # Obtener las fechas y  las temperaturas máximas de cada día.

    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        low = int(row[6])
        dates.append(current_date)
        highs.append( high )
        lows.append( low )
    print(highs)

# Trazar las temperaturas máximas.
plt.style.use( 'seaborn' )
fig,ax = plt.subplots()
ax.plot(dates, highs, c='red')
ax.plot(dates, lows, c='blue')
plt.fill_between( dates, highs, lows, facecolor='blue', alpha=0.1 )
# Dar formato al trazado.
plt.title('Temperaturas maximas y minimas', fontsize=24)
plt.xlabel('Días', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperatura (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()