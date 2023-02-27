import requests
import math

print("Введіть кількість грн")
a = input()

list_currency = []
response = requests.get("https://finance.i.ua/nbu/")
response_text = response.text
response_parse = response_text.split("<span>")
# print(response_parse)
for elem in response_parse:
    if elem.startswith("36"):
        for elem2 in elem.split("</span>"):
            if elem2.startswith("36") and elem2[1].isdigit():
                list_currency.append(float(elem2.replace('36', '').replace(',', '')))
                # print(elem2)


class con:
    a = elem2
    b = a
    g = a / elem2

    def __str__(self):
        g = a / elem2


    '''def __init__(self):
        self.a = elem2
        self.b = a
        self.g = a / elem2'''



v = con
print(g)

