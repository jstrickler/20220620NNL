
#immutable
a = "apple"
b = "banana"

print(a + b)

actor = "Chris Hemsworth"

print(type(actor), len(actor), list(actor))

c = actor.upper()
print("c: {}".format(c))
print("actor.upper(): {}".format(actor.upper()))
print("actor: {}".format(actor))

#  func(obj)    obj.method()
print("actor.count('h'): {}".format(actor.count('h')))
print("actor.lower().count('h'): {}".format(actor.lower().count('h')))

print("actor.count('Chris'): {}".format(actor.count('Chris')))
print("actor.count('Liam'): {}".format(actor.count('Liam')))
print("\U0001F92F")


print("actor.startswith('Chris'): {}".format(actor.startswith('Chris')))
print("actor.startswith('Liam'): {}".format(actor.startswith('Liam')))

print("'Hem' in actor: {}".format('Hem' in actor))
print("'Haw' in actor: {}".format('Haw' in actor))

print("actor.find('Hem'): {}".format(actor.find('Hem')))
print("actor.find('Haw'): {}".format(actor.find('Haw')))

data = "123"
print("data.isalnum(): {}".format(data.isalnum()))
print("data.isdigit(): {}".format(data.isdigit()))
print("data.isalpha(): {}".format(data.isalpha()))
print("data.isnumeric(): {}".format(data.isnumeric()))

data = "123 456"
print("data.isdigit(): {}".format(data.isdigit()))
print("data.replace(' ','').isdigit(): {}".format(data.replace(' ','').isdigit()))
print("actor.replace('Chris', 'Liam'): {}".format(actor.replace('Chris', 'Liam')))

state = 'Missippippi'
print("state.replace('i', 'x'): {}".format(state.replace('i', 'x')))
print("state.replace('i', 'x', 2): {}".format(state.replace('i', 'x', 2)))

s = "      All my exes live in Texas      "
print(s + "|")
print(s.lstrip() + "|")
print(s.rstrip() + "|")  #   raw_line.rstrip()
print(s.strip() + "|")
print()

s = "xyxxyyxxxxxxxyyyyyyyyxyyyxxyxAll my exes live in Texasyyyyyyyyyyyyyyyyyyyyyx"
print(s + "|")
print(s.lstrip("xy") + "|")
print(s.rstrip("xy") + "|")  #   raw_line.rstrip()
print(s.strip("xy") + "|")
print()




