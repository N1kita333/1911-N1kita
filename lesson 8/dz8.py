import kem as kem

result = []


def divider(a, b):
    if type(key) != int:
        raise TypeError

    if a < b:
        raise ValueError
    if b > 100:
        raise IndexError
    return a / b


data = {10: 2, 2: 5, "123": 4, 18: 0, []: 15, 8: 4}

try:
    try:
        for key in data:
            res = divider(key, data[key])
            result.append(res)
            if type(key) != int:
                raise TypeError
    except (NameError) as error:
        print(error)

except:
    print("Невідома помилка")

try:
    print(result)
except:
    print("Невідома помилка")
