import requests

# adresy wszystkich naszych nodeów
adresy = [
    '127.0.0.1:5000',
    '127.0.0.1:5001',
    '127.0.0.1:5002'
]

def get_highest_index_globaly(my_addres):
    highest = 0
    print("jestem w get_highest")
    for adres in adresy:
        if adres != my_addres:
            print("przerabian adres: ",adres)
            res = requests.get('http://'+adres+"/lastindex")
            if int(res.text) > highest:
                highest = int(res.text)
    print("zwracam najwyzszy: ",highest)
    return highest

def get_global_database(my_addres):
    combined = {}
    for adres in adresy:
        if adres != my_addres:
            res = requests.get('http://'+adres+"/local")
            combined.update(eval(res.text))
    return combined



