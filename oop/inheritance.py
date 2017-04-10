class Animal(object):
    def __init__(self):
        print('Animal Created')

    def whoAmI(self):
        print('Animal')

    def eat(self):
        print('Eating')

a = Animal()
print(a)       

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print('Dog Created')

    def whoAmI(self):
        print('Dog')

    def bark(self):
        print('Woof')

d = Dog()
print(d.whoAmI())
print(d.eat())
print(d.bark())