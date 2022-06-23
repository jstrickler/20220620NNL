person = 'Art Vandalay'
city = 'Quebec'
value = 34.4279472947924293829

print(person, city, value)
# str(person) + ' ' + str(city) + ' ' + str(value)  + '\n'
print(person, city, value, sep="#")
print(person, city, value, sep="//")
print(person, city, value, sep="")

print(person, city, value, end=" ")
print("Done.")

print(person, "lives in", city)
print(f"{person} lives in {city}")  # f-string DO THIS!
print("{} lives in {}".format(person, city))  # old-fashioned
print("%s lives in %s" % (person, city))  # older-fashioned

print(f"value is {value}")
print(f"value is {value:.2f}")
print("value is {:.2f}".format(value))

#   f"   {expr}   {expr:fmt}  {expr}    "
a = 2
b = 5
print(f"a + b is {a + b}")


