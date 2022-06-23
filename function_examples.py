from math import pi
import os

def get_message():  # business logic
    return "Hello, NNL world"

m = get_message()

print("m: {}".format(m))

def show_message():  # display logic (AKA GUI, ux, etc)
    message = get_message()
    print(message)

show_message()
result = show_message()
print("result: {}".format(result))

def circle_area(diameter):
    radius = diameter / 2
    area = pi * radius ** 2
    return area

a1 = circle_area(12)
a2 = circle_area(.5)
print("a1: {:.3f}".format(a1))
print("a2: {:.3f}".format(a2))

def square_area(length, width):
    area = length * width
    return area

a3 = square_area(5, 10)
a4 = square_area(9.5, 32)
print("a3: {}".format(a3))
print("a4: {}".format(a4))

def grep(search_term, *file_paths):
    print("file_paths: {}".format(file_paths))
    
    search_term = search_term.lower()
    for file_path in file_paths:
        file_name = os.path.basename(file_path)
        with open(file_path) as file_in:
            for raw_line in file_in:
                if search_term in raw_line.lower():
                    print(file_name, raw_line.rstrip())

grep('pig', 'DATA/alice.txt', 'DATA/words.txt', 'DATA/parrot.txt')
print('-' * 60)
grep('lizard', 'DATA/alice.txt', 'DATA/words.txt')
print('-' * 60)
grep('wombat')

def config(**values):
    print("values: {}".format(values))

config(file_name="wombats.txt", value=42, person="Bela Lugosi")

def spam():
    s = "    THIS IS A TEST   "
    print("s:", s)
    s = ham(s)
    print("new s:", s)

def ham(s):
    return s.strip().lower()

spam()





