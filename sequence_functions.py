#  list, tuple, str, bytes (binary str)

nums = [800, 80, 1000, 32, 255, 400, 5, 5000]

colors = ['red', 'green', 'purple', 'orange', 'brown',
          'black', 'olive', 'navy', 'white', 'black',
          'pink', 'chartreuse']

name = "Bert Smith"

print(len(nums), min(nums), max(nums), sum(nums), sorted(nums), '\n')
print(len(colors), min(colors), max(colors), sorted(colors), '\n')
print(len(name), min(name), max(name), sorted(name), '\n')

print("colors: {}".format(colors))
rcolors = reversed(colors)
print("rcolors: {}".format(rcolors))
for color in rcolors:
    print(color)
print()

notes = 'do', 're', 'mi'
n = reversed(notes)
print("n: {}".format(n))
for note in n:
    print(note)
print()

for note in reversed(notes):
    print(note, end=" ")
print()

names = ('Bob', 'Roberto', 'Beatrix', 'Amy', 'Katie', 'Jeff', 'Seth', 'Taleisha',
'Ali', 'Srini', 'Audrey', 'Monty', 'Pedro', 'Dorothy', 'Immanuel', 'Potsie', 'Frank')

combo = zip(names, colors)
print("combo: {}".format(combo))
for name, color, in combo:
    print(name, color)

items = list(zip(names, colors))
print("items: {}".format(items), '\n')

print("colors: {}".format(colors), '\n')

for i, color in enumerate(colors):
    print(i, color)
print()

print("list(enumerate(colors)): {}".format(list(enumerate(colors))), '\n')

for i in range(3):
    print(i)
print()


#  range(stop)  range(start, stop)  range(start, stop, step)

for i in range(1, 11):
    print(i)
print()

for i in range(5, 101, 5):
    print(i, end=' ')
print('\n')

#  +  *
print('foo' + 'bar')
print('foo' * 10)

flags = [False] * 10
print("flags: {}".format(flags))






