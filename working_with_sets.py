s1 = set()
x = ['a', 'b', 'c', 'c', 'd', 'a', 'm', 'a']
s2 = set(x)
s3 = {5, 9, 14, 2, 7, 8, 1, 4, 9, 5, 5}
print("s1: {}".format(s1))
print("s2: {}".format(s2))
print("s3: {}".format(s3))

fruits1 = ['apple', 'boysenberry', 'grape', 'lemon', 'lime', 'kiwi', 'persimmon']
fruits2 = ['grape', 'plum', 'lychee', 'cantelope', 'lime', 'lemon', 'grape', 'apple']

f1 = set(fruits1)
f2 = set(fruits2)
f1.add('grape')
f1.add('orange')
f2.add('kiwi')
print("f1: {}".format(f1))
print("f2: {}".format(f2))
print()

for fruit in 'grape', 'cranberry', 'lemon', 'cherry':
    print(fruit, fruit in f1, fruit in f2)
print()

print("common:", f1 & f2)  # intersection
print("not common:", f1 ^ f2)  # xor
print("combined:", f1 | f2)  # union
print("f1 only:", f1 - f2)
print("f2 only:", f2 - f1)

breakfast_items = set()
file_path = 'DATA/breakfast.txt'
with open(file_path) as breakfast_in:
    for raw_food in breakfast_in:
        food = raw_food.rstrip()
        breakfast_items.add(food)
print("breakfast_items: {}".format(breakfast_items))


