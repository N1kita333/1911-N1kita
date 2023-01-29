class Student:
    count_of_Student = 0

    def __init__(self, name=None, height=160):
        self.name = name
        self.height = height
        Student.count_of_Student += 1
        print('Привіт я з,явился')

    def grow(self, height=1):
        self.height += height

    def __str__(self):
        return f'я {self.name}, мій зріст {self.height} см'

    def __del__(self):
        print(f'Привіт, я {self.name}, і я пішов ((')


serg = Student(height=180)
print(serg)

Artur = Student(name='Artur', height=165)
