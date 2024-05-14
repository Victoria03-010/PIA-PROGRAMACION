import requests
import json as js

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

def peliculas():
    url = "https://swapi.dev/api/films/"
    data = requests.get(url)
    data = data.json()
    name = data["results"]
    for i in name:
        print(i["title"])

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

# Menú principal
while True:
  print("\nMenú Principal:")
  print("1. Ver personaje/s")
  print("2. Ver planeta/s")
  print("3. Ver titulos de peliculas")
  print("4. Ver naves espaciales")
  print("5. Ver vehiculos")
  print("6. Ver especies")
  print("7. Informacion almacenada")
  print("8. Salir")

  opcion = input("Seleccione una opción: ")

  if opcion == '1':
    op = input("Igrese nombre o presione x para ver nombres: ")
    if op == "x":
      personas()
    else:
      personas(op)
  elif opcion == "2":
    op = input("Igrese planeta o presione x para ver planetas: ")
    if op == "x":
      planetas()
    else:
      planetas(op)
  elif opcion == "3":
    peliculas()
  elif opcion == "4":
    naves_estelares()
  elif opcion == "5":
    vehiculos()
  elif opcion == "6":
    especies()
  elif opcion == "7":
    ####Informacion para almacenar
    print("ola")
  elif opcion == "8":
    print("nos vemos pronto")
    break
  else:
    print("Seleccioneuna opcion válida.")



    
