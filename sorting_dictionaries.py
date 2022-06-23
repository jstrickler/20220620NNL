airports = {
    'EWR': 'Newark',
    'YYZ': 'Toronto',
    'MCI': 'Kansas City',
    'SFO': 'San Francisco',
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'MCO': 'Orlando',
    'YCC': 'Calgary',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SMF': 'Sacramento',
    'YOW': 'Ottawa',
    'IAD': 'Dulles',
}

for code, name in airports.items():
    print(code, name)
print('-' * 60)

for code, name in sorted(airports.items()):
    print(code, name)
print('-' * 60)

def by_value(dict_element):
    return dict_element[1], dict_element[0]

for code, name in sorted(airports.items(), key=by_value):
    print(code, name)
print('-' * 60)