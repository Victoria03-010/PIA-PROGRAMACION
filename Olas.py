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
     print("Capture 1 si desea guardar en un archivo la informacion de un personaje de star wars")
     print("Capture 1 si desea guardar en un archivo la informacion de un plabeta de star wars")
     print("Capture 1 si desea guardar en un archivo la informacion de una pelicula de star wars")
     print("Capture 1 si desea guardar en un archivo la informacion de algunas de las naves estelares de star wars")
     print("Capture 1 si desea guardar en un archivo la informacion de un vehiculo de star wars")
     print("Capture 1 si desea guardar en un archivo la informacion de un especie de star wars")
     respuesta=int(input())

     if(respuesta==1):
        personaje_url = input("Pon el url del personaje: ")
        personaje_data=star_wars_informacion(personaje_url)
        if personaje_data:
           guardar_archivo(personaje_data, 'personaje.txt')
           print("informacion guardada en personaje.txt")
        
        else:
           print("respuesta invalida")
     elif (respuesta==2):
        planeta_url = input("Pon el url del planeta: ")
        planeta_data=star_wars_informacion(planeta_url)
        if planeta_data:
            guardar_archivo(planeta_data, 'planeta.txt')
            print("informacion guardada en personaje.txt")
        
        else:
            print("respuesta invalida")
    elif(respuesta==3):
        pelicula_url = input("Pon el url del pelicula: ")
        pelicula_data=star_wars_informacion(pelicula_url)
        if pelicula_data:
           guardar_archivo(pelicula_data, 'pelicula.txt')
           print("informacion guardada en pelicula.txt")
    
        else:
           print("respuesta invalida")
    elif(respuesta==4):
        nave_espacial_url = input("Pon el url de la nave espacial: ")
        nave_espacial_data=star_wars_informacion(nave_espacial_url)
        if nave_espacial_data:
           guardar_archivo(nave_espacial_data, 'nave espacial.txt')
           print("informacion guardada en nave espacial.txt")
        
        else:
           print("respuesta invalida")
    elif(respuesta==5):
        vehiculo_url = input("Pon el url de la nave espacial: ")
        vehiculo_data=star_wars_informacion(vehiculo_url)
        if vehiculo_url:
            guardar_archivo(vehiculo_data, 'vehiculo.txt')
            print("informacion guardada en vehiculo.txt")
        else:
           print("respuesta invalida")
    elif(respuesta==6):
        especie_url = input("Pon el url de la nave espacial: ")
        especie_data=star_wars_informacion(especie_url)
        if especie_data:
           guardar_archivo(especie_data, 'especie.txt')
           print("informacion guardada en especie.txt")
  
        else:
           print("respuesta invalida")
    else:
        print("Capture una respuestra valida")
      
    print("ola")
  elif opcion == "8":
    print("nos vemos pronto")
    break
  else:
    print("Seleccioneuna opcion válida.")



    
