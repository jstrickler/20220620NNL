# while <EXPR>:
#     code ....

# while loop use cases:
#  1. services (network, especially)
#  2. user input

#  break -- exit loop
#  continue -- jump to top

i = 0
while i < 3:
    print(i)
    i += 1
print()

while True:
    movie = input("Enter a movie name (or q to quit): ")
    if movie == 'q':
        break
    if movie == '':
        print("please enter a movie name")
        continue
    if movie == 'Young Frankenstein':
        print("Loved it")
        continue
    print("I hated", movie)

while True:
    answer = input("What is the answer? ")

