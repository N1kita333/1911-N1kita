import requests
response = requests.get("https://coinmarketcap.com/")
response_text = response.text
response_parse = response_text.split("<span>")
for elem in response_parse:
    if elem.startswith("$"):
        for elem2 in elem.split("</span>"):
            if elem2.startswith("$") and elem2[1].isdigit(): print(elem2)












import requests

response = requests.get("https://coinmarketcap.com/")
response_text = response.text
response_parse = response_text.split("<span>")
for elem in response_parse:
    if elem.startswith("$"):
        from elem2 in elem.split("</span>"):
            if elem2.startswith("$") and elem2[1].isdigit()
               print(elem2)


print(response.text)