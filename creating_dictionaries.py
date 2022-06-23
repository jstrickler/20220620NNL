d1 = dict()
d2 = {'a': 18, 'm': 9, 'z': 31, 'e': 5}
print("d2.keys(): {}".format(d2.keys()))
print("d2.values(): {}".format(d2.values()))
print("d2.items(): {}".format(d2.items()))
d2['r'] = 75
d2['r'] = 98
d2['x'] = 1
print("d2: {}".format(d2))
print("d2.items(): {}".format(d2.items()))
print("d2['e']: {}".format(d2['e']))
print("d2['x']: {}".format(d2['x']))
# print("d2['p']: {}".format(d2['p']))
print("'p' in d2: {}".format('p' in d2))
print("d2.get('p'): {}".format(d2.get('p')))
print("d2.get('p', 42): {}".format(d2.get('p', 42)))
del d2['m']
print("d2: {}".format(d2))
print("d2.setdefault('q', 47): {}".format(d2.setdefault('q', 47)))
print("d2: {}".format(d2))
print("d2.setdefault('z', 99): {}".format(d2.setdefault('z', 99)))
print("d2: {}".format(d2))
print()

for letter, number in d2.items():
    print(letter, number)
print()
print("d2.items(): {}".format(d2.items()))



