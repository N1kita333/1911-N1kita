import random


class Student:
    def __init__(self, name):
        self.name = name
        self.progress = 0
        self.gladness = 100
        self.alive = True

    def to_study(self):
        print("Я навчаюсь")
        self.progress += 0.1
        self.gladness -= 6

    def to_sleep(self):
        print("я пішов спати")
        self.gladness += 3

    def to_have_fun(self):
        print("я пішов розважатися")
        self.progress -= 0.1
        self.gladness += 5

    def is_alive(self):
        if self.progress < 0:
            print('Вас відраховано від навчального закладу')
            self.alive = False
        if self.progress > 5:
            print('Ура! Я достроково завершив МКА')
            self.alive = False
        if self.gladness < 0:
            print('Все пропало. В мене депрессія')
            self.alive = False
    def end_off_day(self):
        print(f'задоволеність - {self.gladness}')
        print(f'прогрес       - {round(self.progress, 2)}')

    def live(self, day):
        info = f'День{day} з життя {self.name}'
        print(f'{info:=^40}')
        choice = random.randint(1, 3)
        if choice == 1:
            self.to_study()
        elif choice == 2:
            self.to_sleep()
        elif choice == 3:
            self.to_have_fun()

        self.end_off_day()
        self.is_alive()


nikita = Student(name="Микита")
for day in range(365):
    if nikita.alive == False:
        break
    nikita.live(day)
