from usuarios import User
from priv import Admin

momi = Admin(
    'Momi', 'Chinchilinha', '30', '1994', 'Arquiteta', \
    'Arquiteta da Prefeitura', ['ter muito dinheiro', 'casar com o riri', 'ter filhinhos com o riri chinchilo']
)
momi.privileges.show_privileges()
print(momi.first_name, momi.last_name, momi.age, momi.formation, momi.ocupation)