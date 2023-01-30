from math import *


def func(d):
    return sqrt(d ** 2 / 2)


d = int(input('Введіть діаметр диску в мм, '))
rez = func(d)
print('Сторона коробки =', round(rez, 2), 'MM')

###
def func(c, m, t1, t2):
    return c * m * (t2 - t1)


c = int(input('Введіть питому теплоємність речовини, '))
m = int(input('Введіть масу тіла, '))
t1 = int(input('Введіть початкову температуру тіла, '))
t2 = int(input('Введіть кінцеву температуру тіла, '))
rez = func(c, m, t1, t2)
print('Необхідна кількість теплоти =', round(rez, 2))

###
def func(s, h, a, b):
    return s / ((a + b) / 2 * h)


s = int(input('Введіть площу доріжки в парку, '))
a = int(input('Введіть довжину сторони плитки а= '))
b = int(input('Введіть довжину сторони плитки b= '))
h = int(input('Введіть вистоу плитки h= '))
rez = func(s, h, a, b)
print('Kiлькiсть плиток =', round(rez, 2), 'шt.')

###
def func(x1, y1, x2, y2):
    return sqrt(x2 - x1) ** 2 + (y2 - y1) ** 2


def func1(AB, BC, AC):
    return AB + BC + AC


def func2(AB, AC):
    return AB * AC


x1 = int(input('Введіть координату х вершини А, '))
y1 = int(input('Введіть координату у вершини А, '))
x2 = int(input('Введіть координату х вершини В, '))
y2 = int(input('Введіть координату у вершини В, '))
x3 = int(input('Введіть координату x вершини С, '))
y3 = int(input('Введіть координату у вершини С, '))
AB = func(x1, y1, x2, y2)
BC = func(x2, y2, x3, y3)
AC = func(x1, y1, x3, y3)
rez1 = func1(AB, BC, AC)
print('Периметр трикутника =', round(rez1, 2))
rez2 = func2(AB, AC)
print('Плoшa прямокутника =', round(rez2, 2))
