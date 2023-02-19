class Human:
    height = 170
    age = 30
    gladness = 50


class Student(Human):
    age = 17


class Aspirant(Student):
    height = 180

    def __init__(self):
        print(self.height)
        print(self.age)
        print(self.gladness)

    def _hello(self):
        print("_Hello")

    def __hello(self):
        print("__Hello")


class Worker(Human):
    age = 50


class Hello_Kity:
    hello = "hello"
    _hello = "_hello"
    __hello = "__hello"

    def __init__(self):
        self.kity = "kity"
        self._kity = "_kity"
        self.__kity = "__kity"

    def print(self):
        print(self.hello)
        print(self._hello)
        print(self.__hello)
        print(self.kity)
        print(self._kity)
        print(self.__kity)


class Hi(Hello_Kity):
    def hi_print(self):
        super().__method()
        print(self.hello)
        print(self._hello)
        print(self.__hello)
        print(self.kity)
        print(self._kity)
        print(self.__kity)

    def __method(self):
        print("Method")


class Computer:
    def __init__(self, model, *args, **kwargs):
        self.RAM = "16 Gb"
        self.model = model

    def calc(self):
        print("Calculate.....")


class Monitor:
    def __init__(self):
        super().__init__()
        self.resolution = "1920"

    def display(self):
        print("Print result")


class SmartPhone(Monitor, Computer):
    def info(self):
        print(self.resolution)
        print(self.RAM)
        print(self.model)


#phone = SmartPhone(model =  "Apple 15")
#phone.info()

# hello = Hello_Kity()
# ello.print()


# hi = Hi()
# hi.hi_print()


# asp = Aspirant()
# asp._hello()


# st = Student()
# wr = Worker()
# print(st.age)
# print(wr.age)
