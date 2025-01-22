def city_and_country(city, country, population):
    name = f"{city}, {country} - population {population}.".title()
    return name

ourinhos = city_and_country('Ourinhos', 'Brasil', 120000)
print(ourinhos)