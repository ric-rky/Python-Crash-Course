from city_functions import city_and_country


def test_city_country():
    correct_format = city_and_country('ourinhos', 'brasil')
    assert correct_format == 'Ourinhos, Brasil.'

def test_city_country_population():
    correct_format = city_and_country('ourinhos', 'brasil', 120000)
    assert correct_format == 'Ourinhos, Brasil - Population 120000.'