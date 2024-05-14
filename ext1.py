import requests
import json


def personas(b = 0):
    url = "https://swapi.dev/api/people/"
    if b == 0:
        data = requests.get(url)
        data = data.json()
        name = data["results"]
        for i in name:
            print(i["name"])
    else:
        data = requests.get(url)
        data = data.json()
        name = data["results"]
        for i in name:
            if i["name"] == b:
                dato = i['url']
                dato = requests.get(dato)
                dato = dato.json()
                dic= dato
                for x, y in dic.items():
                    print(x,":", y)


def peliculas():
    url = "https://swapi.dev/api/films/"
    data = requests.get(url)
    data = data.json()
    name = data["results"]
    for i in name:
        print(i["name"])

def naves_estelares():
    url = "https://swapi.dev/api/starships/"
    data = requests.get(url)
    data = data.json()
    name = data["results"]
    for i in name:
        print(i["name"])

def vehiculos():
    url = "https://swapi.dev/api/vehicles/"
    data = requests.get(url)
    data = data.json()
    name = data["results"]
    for i in name:
        print(i["name"])

def especies():
    url = "https://swapi.dev/api/species/"
    data = requests.get(url)
    data = data.json()
    name = data["results"]
    for i in name:
        print(i["name"])


def planetas(b = 0):
    url = "https://swapi.dev/api/planets/"
    if b == 0:
        data = requests.get(url)
        data = data.json()
        name = data["results"]
        for i in name:
            print(i["name"])
    else:
        data = requests.get(url)
        data = data.json()
        name = data["results"]
        for i in name:
            if i["name"] == b:
                dato = i['url']
                dato = requests.get(dato)
                dato = dato.json()
                dic= dato
                for x, y in dic.items():
                    print(x,":", y)


#Owen Lars
    
#personas("Owen Lars")
#planetas("Kamino")
peliculas()

