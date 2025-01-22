from pathlib import Path
import json
import plotly.express as px

# Lê os dados como uma string e os converte em um objeto Python
path = Path('eq_data\\eq_data_30_day_m1.geojson')
contents = path.read_text(encoding = 'utf-8')

all_eq_data = json.loads(contents)

# Cria uma versão mais legível do arquivo de dados
path = Path('eq_data\\readable_eq_data.geojson')
readable_contents = json.dumps(all_eq_data, indent = 4)
path.write_text(readable_contents)

# Examina todos os terremotos no conjunto de dados
title = all_eq_data['metadata']['title']
all_eq_dicts = all_eq_data['features']

# Extrai todas as magnitudes e as coordenadas dos terremotos e armazena tais informações numa lista
mags, lons, lats, eq_titles = [], [], [], []
for eq_dict in all_eq_dicts:
    mags.append(eq_dict['properties']['mag'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    eq_titles.append(eq_dict['properties']['title'])

# Plota o mapa mundi com os terremotos
fig = px.scatter_geo(lat = lats, lon = lons, size = mags, title = title,
                     color = mags,
                     color_continuous_scale = 'Viridis',
                     labels = {'color': 'Magnitude'},
                     projection = 'natural earth',
                     hover_name = eq_titles,
                     )
fig.show()