file_path = "DATA/mary.txt"

mary_in = open(file_path, "r")
# read file here....
mary_in.close()

with open(file_path, "r") as mary_in:
    print("reading file...")
print('-' * 60)

with open(file_path) as mary_in:
    for raw_line in mary_in:    #   mary_in.readline() ...
        line = raw_line.rstrip()  # remove \n from line
        print(line)
print('-' * 60)

with open(file_path) as mary_in:
    contents = mary_in.read()   # read entire file into one string
    print("RAW:")
    print(repr(contents))
    print("NORMAL:")
    print(contents)
print('-' * 60)

# read 1 char at a time
with open(file_path) as file_in:
    while True:
        next_char = file_in.read(1)
        if next_char == '':
            break
        print(next_char, end='/')
print("\n")
print('-' * 60)

# read file into array of lines WITH newlines
with open(file_path) as mary_in:
    all_lines_with_nl = mary_in.readlines()
    print(all_lines_with_nl)
print('-' * 60)

# read file into array of lines WITHOUT newlines
with open(file_path) as mary_in:
    all_lines_without_nl = mary_in.read().splitlines()
    print(all_lines_without_nl)
print('-' * 60)



