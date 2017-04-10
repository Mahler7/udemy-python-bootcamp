class Sample(object):
    pass

x = Sample()
print(type(x))

class Dog(object):
    #Class Object Attribute
    species = 'mammal'
    number_of_legs = 4
    def __init__(self, breed, name, size):
        self.breed = breed
        self.name = name
        self.size = size

sam = Dog(breed='lab', name='Sammy', size='large')
print(sam)
print(sam.breed)
print(sam.name)
print(sam.size)
print(sam.species)
print(sam.number_of_legs)
