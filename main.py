class House:
    def __init__(self, kitchen):
        self.kitchen = kitchen
        self.located = []

    def add_located(self, *animal):
        for located in animal:
            self.located.append(located)

    def print_located(self):
        if self.located == []:
            print('Кухня зараз порожня')
        else:
            print(F'Зараз в {self.kitchen} знаходиться:')
            for located in self.located:
                print(located.name)


class Animal:
    count_of_animal = 0

    def __init__(self, name=None, years=None, description=None):
        self.name = name
        self.years = years
        self.description = description
        Animal.count_of_animal += 1
        print(f"Привіт, я з'явився, я {self.name}")

    #def grow(self, years=0.1):
    #    self.years += 0.1

    #def __str__(self):
    #    return f'я {self.name}, мій зріст {self.years} '

    #def __del__(self):
    #    print(f'Привіт, я {self.name}, {self.description}, мені {self.years} і я пішов гуляти')


#Tom = Animal(name='Tom', years=2, description='я кот')



#Ashley = Animal(name='Ashley', years=1, description='я кіт')

# Ashley.grow()
print(Animal.count_of_animal, "шт.")
Ashley = Animal("Ashley",  years=2, description='я кот')
Tom = Animal("Tom", years=1, description='я кіт')
house = House("кухні")
house.print_located()
house.add_located(Ashley, Tom)
house.print_located()
