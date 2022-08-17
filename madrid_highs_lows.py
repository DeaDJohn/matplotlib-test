import csv

import matplotlib.pyplot as plt

from datetime import datetime

filename = 'weather_data/madrid_2022.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

    # Obtener las fechas y  las temperaturas máximas de cada día.

    dates, highs, lows,precs = [], [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        print(current_date)

        try:
            high = float(row[5])
            low = float(row[6])
            prec = float(row[3])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append( high )
            lows.append( low )
            precs.append(prec)
    print(highs)

# Trazar las temperaturas máximas.
plt.style.use( 'seaborn' )
fig,ax = plt.subplots()
ax.plot(dates, highs, c='red')
ax.plot(dates, lows, c='blue')
#ax.plot(dates, precs, c='green')
plt.fill_between( dates, highs, lows, facecolor='blue', alpha=0.1 )
# Dar formato al trazado.
plt.title('Temperaturas maximas y minimas - 2022\nMadrid, CA', fontsize=20)
plt.xlabel('Días', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperatura (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()