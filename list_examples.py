list1 = list()
list2 = ['mango', 'lemon', 'cranberry']
list3 = []
x = 'abc'
list4 = list(x)
print(list1, list2, list3, list4)

# iterable: object that can be looped over with a for loop

things = [5, 'abc', 8.9, None, [5, 10, 15]]

cities = ['McKeesport', 'Pittsburgh', 'Sewickley']
cities.insert(0, 'Apex')
cities.insert(3, 'Chapel Hill')
print("cities: {}".format(cities))

cities.append('Greensburg')
cities.append('Beaver Falls')

print("cities: {}".format(cities))

more_cities = ['Rochester', 'Boston', 'Columbus']

cities.extend(more_cities)
print("cities: {}".format(cities))

#  cities.insert(pos, obj)   cities.append(obj)   cities.extend(iterable)

print("cities[6]: {}".format(cities[6]))
del cities[6]   #  del OBJ
print("cities: {}".format(cities))
print("cities[6]: {}".format(cities[6]))
cities.remove('Boston')
print("cities: {}".format(cities))

city = cities.pop()
print("city: {}".format(city))
print("cities: {}".format(cities))

city = cities.pop(3)
print("city: {}".format(city))
print("cities: {}".format(cities))

#   del cities[pos]    obj = cities.pop(pos=-1)    cities.remove(value)

print("cities[2]: {}".format(cities[2]))
print("cities[5]: {}".format(cities[5]))
print("cities[-1]: {}".format(cities[-1]))
print("cities[len(cities)-1]: {}".format(cities[len(cities)-1]))

print("cities[0:3]: {}".format(cities[0:3]))
#   [start:stop]  [:stop]  [start:] [:]   [start:stop:step]
print("cities[1:4]: {}".format(cities[1:4]))
print("cities[:3]: {}".format(cities[:3]))
print("cities[4:]: {}".format(cities[4:]))
print("cities[2:99]: {}".format(cities[2:99]))

x = "H3e$l(l#o"
print("x[:3]: {}".format(x[:3]))
print("x[-4:]: {}".format(x[-4:]))
print("x[::2]: {}".format(x[::2]))

for city in cities:
    # city = cities[0]
    # city = cities[1]
    # city = cities[2]
    # ...
    print(city.upper())
print()

# for VAR in ITERABLE:
#    code ....