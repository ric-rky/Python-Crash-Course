bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])
print(bicycles[0].title())

família_tatu = ['riri', 'momi chinchilinha', 'mamãe denise', 'papai ricardo']
print(f"Os integrantes da Família Tatu são: {família_tatu[0], família_tatu[1], família_tatu[2], família_tatu[3]}.".title())

motorcycles = ['honda', 'yahama', 'suzuki']
motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
motorcycles.append('ducati')

motorcycles = []
motorcycles.insert(0, 'honda')
motorcycles.insert(1, 'yamaha')
motorcycles.insert(2, 'suzuki')
print(motorcycles)

#deletar elementos de uma lista
motorcycles = ['honda', 'yahama', 'suzuki']
del motorcycles[0]
print(motorcycles)

#remover elementos com pop
motorcycles = ['honda', 'yahama', 'suzuki']
popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")
print(motorcycles)

#Exercícios - pág. 77
#3.4
math_areas = ['Analysis', 'Topology', 'Geometry', 'Algebra']
print(f"I love you all, {math_areas[0], math_areas[1], math_areas[2], math_areas[3]}!")

#3.5
convidados = ['Kaluk', 'Pouk', 'Tut', 'Kouk', 'Koune', 'Luq']
print(f"Kouk não poderá comparecer ao jantar.")
del convidados[3]
print(convidados)

#3.6
convidados = ['Kaluk', 'Pouk', 'Tut', 'Kouk', 'Koune', 'Luq']
convidados.insert(0, 'Puq')
convidados.insert(1, 'Tut')
convidados.insert(2, 'Nuq')
convidados.insert(3, 'Kouk')
convidados.insert(4, 'Gux')
convidados.insert(5, 'Yug')
print(convidados)
convidados.append('Tuluq')
print(convidados)
for x in convidados:
    print(f"Seja bem-vindo ao jantar, {x}!")

#3.7
print(convidados)
popped_first = convidados.pop(0)
print(convidados, f"Lamentamos pelo inconveniente, {popped_first}.")
print(convidados)
for x in convidados[:]:
    if x != 'Pouk' and x != 'Tut':
        popped = convidados.pop(convidados.index(x))
        print(convidados, f"Lamentamos pelo inconveniente, {popped}.")



