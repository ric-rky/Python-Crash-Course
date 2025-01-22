from name_function import get_formatted_name


def test_first_last_name():
    """Nomes como 'Janis Joplin' funcionam?"""
    formatted_name = get_formatted_name('Janis', 'Joplin')
    assert formatted_name == 'Janis Joplin'

def test_first_last_middle_name():
    """Nomes como 'Wolfgang Amadeus Mozart' funcionam?"""
    formatted_name = get_formatted_name(
        'wolfgang', 'mozart', 'amadeus'
    )
    assert formatted_name == 'Wolfgang Amadeus Mozart'
