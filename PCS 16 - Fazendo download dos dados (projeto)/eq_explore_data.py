from pathlib import Path
import json

# Lê os dados como uma string e os converte em um objeto Python
path = Path('eq_data\\eq_data_1_day_m1.geojson')
contents = path.read_text(encoding = 'utf-8')

all_eq_data = json.loads(contents)

# Cria uma versão mais legível do arquivo de dados
path = Path('eq_data\\readable_eq_data.geojson')
readable_contents = json.dumps(all_eq_data, indent = 4)
path.write_text(readable_contents)

# Examina todos os terremotos no conjunto de dados
all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))

# Extrai todas as magnitudes e as coordenadas dos terremotos e armazena tais informações numa lista
mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict["properties"]["mag"]
    lon = eq_dict["geometry"]["coordinates"][0]
    lat = eq_dict["geometry"]["coordinates"][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

print(mags[:10], lons[:10], lats[:10], sep = "\n")



