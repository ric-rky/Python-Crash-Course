import car

my_new_car = car.Car('Audi', 'a5', '2024')
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 20
my_new_car.read_odometer()

my_new_car.year = 2025
print(my_new_car.year)

my_mustang = car.Car('Ford', 'Mustang', 2025)
print(my_mustang.get_descriptive_name())
my_leaf = car.ElectricCar('nissan', 'leaf', 2025)
print(my_leaf.get_descriptive_name())



