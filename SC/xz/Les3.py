class Animal:
    count_of_animal = 0

    def __init__(self, name=None, years=0, description=None, height=150):
        self.name = name
        self.years = years
        self.height = height
        self.description = description
        Animal.count_of_animal += 1
        print("Привіт, я з'явився")

    def grow(self, years=0.1):
        self.years += years

    def __str__(self):
        return f'я {self.name}, мій зріст {self.years} см'

    def __del__(self):
        print(f'Привіт, я {self.name}, {self.description}, мені {self.years} і я пішов гуляти')


Tom = Animal(name='Tom', years=21, description='я людина', height=189)
print(Tom.years)
print(Tom.name)
print(Tom.description)


Ashley = Animal(name='Ashley', years=19, description='я людина', height=183)
print(Ashley.years)
print(Ashley.name)
print(Ashley.description)

#Ashley.grow()
print(Animal.count_of_animal)