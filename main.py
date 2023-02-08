class House:
    def __init__(self):
        self.food = 0
        self.mess = 0


class Animal:
    count_of_animal = 0

    def __init__(self, name=None, years=None, description=None):
        self.name = name
        self.years = years
        self.description = description
        Animal.count_of_animal += 1
        print(f"Привіт, я з'явився, я {self.name}")

    def grow(self, years=0.1):
        self.years += 0.1

    #def __str__(self):
    #    return f'я {self.name}, мій зріст {self.years} '

    #def __del__(self):
    #    print(f'Привіт, я {self.name}, {self.description}, мені {self.years} і я пішов гуляти')


Tom = Animal(name='Tom', years=2, description='я кот')



Ashley = Animal(name='Ashley', years=1, description='я кіт')

# Ashley.grow()
print(Animal.count_of_animal, "шт.")
