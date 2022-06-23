
person = 'Bill', 'Gates', 'Microsoft', '1955-10-24'   # no [] or {}

print(person[0], person[1])

first_name, last_name, product, dob = person  # iterable unpacking
print(first_name, last_name)

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
print("type(people[0]): {}".format(type(people[0])))
print("people[0]: {}".format(people[0]))
print("people[0][0]: {}".format(people[0][0]))
print("people[0][0][0]: {}".format(people[0][0][0]))
print()

for first_name, last_name, product, dob in people:
    print(first_name, last_name)
print()

my_data = [
    ('Bob', 5),
    ('Mary', 10),
    ('Ebenezer', 22),
]

for name, value in my_data:
    print(name, value, value ** .5)
print()
