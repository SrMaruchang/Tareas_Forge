#--------Funciones intermedias (Core)---
#Crea el archivo un Python llamado funciones_intermedias_1.py LISTEKE
#Actualiza los valores en diccionarios y listas
#Crea la función iterarDiccionario(lista)
#Crea la función iterarDiccionario2(llave, lista)
#Crea la función imprimirInformacion(diccionario)

#T1-Actualiza los valores en diccionarios y listas

matriz = [ [10, 15, 20], [3, 7, 14] ]
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"}
]

ciudades = {
    "México": ["Ciudad de México", "Guadalajara", "Cancún"],
    "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}

coordenadas = [
    {"latitud": 8.2588997, "longitud": -84.9399704}
]

#Acá cambio el valor de matriz
matriz[1][0] = 6
print("Matriz actualizada:", matriz)

#Acá cambio el nombre del primer cantante.
cantantes[0]["nombre"] = "Enrique Martin Morales"
print("Cantantes actualizados:", cantantes)

#Acá cambio el nombre de la ciudad de Cancún a Monterrey.
ciudades["México"][2] = "Monterrey"
print("Ciudades actualizadas:", ciudades)

#Acá cambio las coordenadas, cambia el valor de “latitud” por 9.9355431.
coordenadas[0]["latitud"] = 9.9355431
print("Coordenadas actualizadas:", coordenadas)

#------------OBJETIVOS LISTEKEEEE--------
#T2. Iterar a través de una lista de diccionarios

def iterarDiccionario(lista):
    for diccionario in lista:
        for llave, valor in diccionario.items():
            print(f"{llave} - {valor}")

cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]
#------------OBJETIVOS LISTEKEEEE--------
#T3. Obtener valores de una lista de diccionarios

def iterarDiccionario2(llave, lista):
    for diccionario in lista:
        print(diccionario[llave])
print("\n--- Ejecución T3 (Nombres) ---")
iterarDiccionario2("nombre", cantantes)

def imprimirInformacion(diccionario):
    for llave, lista in diccionario.items():
        print(f"{len(lista)} {llave.upper()}")
        for item in lista:
            print(item)
        print("")

costa_rica = {
    "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
    "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}

imprimirInformacion(costa_rica)