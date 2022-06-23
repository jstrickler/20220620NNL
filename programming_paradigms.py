# procedural
dog1 = ['Nellie', 'female', 'English Shepherd', 'yip']
dog2 = ['Andy', 'male', 'mutt', 'woof']

def get_breed(dog):
    return dog[2]

print("get_breed(dog1): {}".format(get_breed(dog1)))
print("get_breed(dog2): {}".format(get_breed(dog2)))

def bark(dog):
    bark_type = dog[-1]
    print(f"{bark_type} {bark_type}")

bark(dog1)
bark(dog2)
#------------------------------------------------------------------------
print('-' * 60)
class Dog:
    def __init__(self, name, sex, breed, bark_type):
        self.name = name
        self.sex = sex
        self.breed = breed
        self.bark_type = bark_type

    def get_breed(self):  # methods
        return self.breed

    def bark(self):
        print(f"{self.bark_type} {self.bark_type} ")
# instance/obj = Class(args)
# instance.method(...)

dog1 = Dog('Nellie', 'female', 'English Shepherd', 'yip')
dog2 = Dog('Andy', 'male', 'mutt', 'arf')

print(dog1.get_breed())
dog2.bark()

