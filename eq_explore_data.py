import json
from datetime import datetime
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline


# Explora la estructura de los datos.
filename = 'weather_data/1.0_month.json'
with open(filename) as f:
    all_eq_data = json.load(f)

all_eq_data = all_eq_data['features']

mags, lons, lats, hover_text, dates = [], [], [], [], []
for eq_dict in all_eq_data:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    title = eq_dict['properties']['title']
    try:
        date = datetime.fromtimestamp(eq_dict['properties']['time']/ 1000)
        #date = datetime.strptime(date, '%d-%m-%Y-T%H:%M:%S.%fZ')
    except:
        print (f"{eq_dict['properties']['time']} is missing a date")
    else:
        dates.append(date)
    
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_text.append(f"{date} \n {title}")

print(dates[:10])
redeable_file = 'weather_data/readable_eq_data.json'
with open(redeable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4)

# Mapea los terremotos.
data = [{
    'type': 'scattergeo',
    'lon':lons, 
    'lat':lats,
    'text': hover_text,
    'marker': {
        'size': [5*mag for mag in mags],
        'color': mags,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Magnitud'},
    },
    }]
my_layout = Layout(title='Terremotos del 1.0')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='terremotos_del_1.0.html')