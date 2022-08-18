import requests
from plotly.graph_objects import Bar
from plotly import offline

# Hacer una llamada a la api y guardar la respuesta
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Guardar la respuesta de la API en una variable.
response_dict = r.json()
repo_dicts = response_dict['items']
repo_links, stars, labels = [], [], []
for repo_dict in repo_dicts:
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)

    stars.append(repo_dict['stargazers_count'])

    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    label = f"{owner}<br />{description}"
    labels.append(label)


# Hacer la visualizacion de los datos.
data = [{
    'type': 'bar',
    'x': repo_links,
    'y': stars,
    'hovertext': labels,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': '#eee'}
    },
    'opacity': 0.6,
}]
my_layout = {
    'title': 'Número de estrellas de los repositorios Python',
    'titlefont': {'size': 28},
    'xaxis': {
        'title': 'Repositorio',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
        },
    'yaxis': {
        'title': 'Estrellas',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
        },
}
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html')
