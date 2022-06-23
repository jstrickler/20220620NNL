import sys

# stdio   stdout stderr stdin

def myprint(*args):
    for arg in args[:-1]:
        sys.stdout.write(str(arg) + ' ')
    sys.stdout.write(str(args[-1]) + '\n')

x = 5
y = 34.343
z = "wombat"
myprint(x, y, z)

print("Houston, we have a problem", file=sys.stderr)

