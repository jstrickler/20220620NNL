#  builtin, global, nonlocal, local

x = 100  # global

def spam():
    person = "Fay Wray"  # local
    print("in spam(): x is", x)

spam()
# print("person: {}".format(person))   # print() is builtin

def outer():
    name = "Bob"  # name is local to outer()
    print(name)

    def inner():
        print(name)  # name is nonlocal to inner()

