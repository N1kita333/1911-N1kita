import random


class Human:
    def __init__(self, name, house=None, car=None, job=None):
        self.name = name
        self.house = house
        self.car = car
        self.job = job
        self.money = 100
        self.gladness = 50
        self.satiety = 50

    def eat(self):
        pass

    def work(self):
        pass

    def shopping(self):
        pass

    def cleaning(self):
        pass

    def get_house(self):
        self.house = House()

    def get_car(self):
        self.car = Car(brand_of_cars)

    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)

    def is_alive(self):
        if self.gladness < 0:
            print("Депресія....")
            return False
        if self.satiety < 0:
            print("Помер від голоду...")
            return False
        if self.money < -200:
            print("Банкрот....")
            return False

    def day_info(self, day_number):
        day_str = f"День {day_number}--день з життя {self.name}-а"
        print(f"{day_str:=^50}", "\n")
        human_str = f"Інформація про {self.name}a"
        print(f"{human_str:=^50}", "\n")
        print(f"Задоволення - {self.gladness}")
        print(f"Ситість     - {self.satiety}")
        print(f"Гроші       - {self.money}")
        house_str = f"Інформація про будинок"
        print(f"{house_str:=^50}", "\n")
        print(f"Їжа         - {self.house.food}")
        print(f"Порядок     - {self.house.mess}")
        car_str = "Інформація про авиівку {self.car.brand}"
        print(f"{car_str:=^50}", "\n")
        print(f"Пальне        {self.car.fuel}")
        print(f"CTаH          {self.car.strength}")

    def live(self, day_number):
        if self.is_alive() == False:
            return False
        if self.house is None:
            self.get_house()
            print("Поселилися в будинку")
        if self.car is None:
            self.get_car()
            print(f"Придбав автівку {self.car.brand}")
        if self.job is None:
            self.get_job()
            print(f"Влаштувался на роботу {self.job.job}, із зарплатнею {self.job.salary}$")
        self.day_info(day_number)


brand_of_cars = {"BMV": {"fuel": 100, "strength": 100, "consumption": 6},
                 "Audi": {"fuel": 80, "strength": 80, "consumption": 7},
                 "Mercedes": {"fuel": 100, "strength": 90, "consumption": 5},
                 "Запорожець": {"fuel": 50, "strength": 50, "consumption": 8}}


class Car:
    def __init__(self, brand_of_cars):
        self.brand = random.choice(list(brand_of_cars))
        self.fuel = brand_of_cars[self.brand]["fuel"]
        self.strength = brand_of_cars[self.brand]["strength"]
        self.consumption = brand_of_cars[self.brand]["consumption"]

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print("нема пального або машина зламалась")
            return False


class House:
    def __init__(self):
        self.food = 0
        self.mess = 0


job_list = {"Розробник на Python": {"salary": 100, "gladness_less": 10},
            "Викладач на Python": {"salary": 80, "gladness_less": 2},
            "Водій": {"salary": 60, "gladness_less": 5},
            "Продавець": {"salary": 50, "gladness_less": 8}}


class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]["salary"]
        self.gladness_less = job_list[self.job]["gladness_less"]


nikita = Human("Микита")
for day in range(1, 366):
    if nikita.live(day) == False:
        break
