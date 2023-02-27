
result = []


def divider(a, b):
    try:
        return a / b

    except ZeroDivisionError:
        print("Ви не можете ділити на нуль!")
        return 0

    except TypeError:
        print("Ви не можете ділити нечислові значення!")
        return 0

    except ValueError:
        print("Ви не можете ділити нечислові значення!")
        return 0

    except NameError:
        print("213")
        return 0


data = {10: 2, 2: 5, "123": 4, 18: 0, []: 15, 8: 4}

for key in data:
    res = divider(key, data[key])
    result.append(res)

print(result)



#try:
        for key in data:
            res = divider(key, data[key])
            result.append(res)
    #except (NameError) as error:
    #    print(error)
    #finally:
    #    print("Невідома помилка")
