import csv

fruits = ["pomegranate", "cherry", "apricot", "Apple",
"lemon", "Kiwi", "ORANGE", "lime", "Watermelon", "guava",
"Papaya", "FIG", "pear", "banana", "Tamarind", "Persimmon",
"elderberry", "peach", "BLUEberry", "lychee", "GRAPE", "date" ]

f1 = sorted(fruits)
print("f1: {}\n".format(f1))

name = "Genghis Khan"
print(str.lower(name), '\n')   # compare to name.lower()

f2 = sorted(fruits, key=str.lower)
print("f2: {}\n".format(f2))

f3 = sorted(fruits, key=len)
print("f3: {}\n".format(f3))

def sort_by_len_and_name(fruit):
    return len(fruit), fruit.lower()

f4 = sorted(fruits, key=sort_by_len_and_name)
print("f4: {}\n".format(f4))

def wacky(element):
    return element[-1]

f5 = sorted(fruits, key=wacky)
print("f5: {}\n".format(f5))

nums = [800, 80, 1000, 32, 255, 400, 5, 5000]

n1 = sorted(nums)
print("n1: {}\n".format(n1))

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

for person in sorted(people):
    print(person)
print('-' * 60)

def by_dob(person):
    return person[-1]

for person in sorted(people, key=by_dob):   # key=lambda p: p[-1]
    print(person)
print('-' * 60)

file_path = 'DATA/city-of-chicago-salaries.csv'
with open(file_path) as city_in:
    rdr = csv.reader(city_in)
    header = next(rdr)
    records = []
    for row in rdr:
        row[-1] = float(row[-1].lstrip('$'))
        records.append(row)

def by_salary(row):
    return row[-1]

for record in sorted(records[:100], key=by_salary, reverse=True):
    print(record)
print('-' * 60)

for record in sorted(records[:100], key=lambda e: e[-1], reverse=True):
    print(record)
print('-' * 60)





