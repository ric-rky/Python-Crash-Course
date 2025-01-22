"""Conjunto de classes que pode ser usado para representar carros elétricos"""

from car import Car
from car import ElectricCar as EC #<- cria um alias EC para ElectricCar

my_mustang = Car('ford', 'mustang', 2025)
my_leaf = EC('nissan', 'leaf', 2025)

print(my_mustang.get_descriptive_name())
print(my_leaf.get_descriptive_name())