from restaurant import Restaurant
import user

# 9.10

my_restaurant = Restaurant('La Parrilla', 'Argentino')
my_restaurant.describe_restaurant()
print(my_restaurant.cuisine_type)

# 9.11
riri = user.Admin('Ricardo', 'Bertolucci', '28', '2025', 'Mathematician', \
                          'Data Scientist', ['can do everything he wants'])
riri.show_privileges()