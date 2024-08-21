# Lista original de nombres
nombres = [
    "Harry Houdini", "Newton", "David Blaine", "Hawking", "Messi", 
    "Teller", "Einstein", "Pele", "Juanes"
]

# Listas vacías para los grupos
magos = []
cientificos = []
otros = []

# Clasificar los nombres
for nombre in nombres:
    if nombre in ["Harry Houdini", "David Blaine", "Teller"]:
        magos.append(nombre)
    elif nombre in ["Newton", "Hawking", "Einstein"]:
        cientificos.append(nombre)
    else:
        otros.append(nombre)

# Función para hacer a los magos grandiosos
def hacer_grandioso(magos):
    for i in range(len(magos)):
        magos[i] = "El gran " + magos[i]

# Función para imprimir nombres
def imprimir_nombres(lista):
    for nombre in lista:
        print(nombre)
        
# Función para imprimir todas las listas
def imprimir_listas(listam, listac, listao):
    print("\nMagos grandiosos:")
    imprimir_nombres(listam)
    print("\nCientíficos:")
    imprimir_nombres(listac)
    print("\nOtros:")
    imprimir_nombres(listao)

# Imprimir nombres originales
print("\nNombres originales:")
imprimir_nombres(nombres)

# Hacer grandiosos a los magos
hacer_grandioso(magos)

# Imprimir los nombres después de la modificación
#print("\nMagos grandiosos:")
#imprimir_nombres(magos)

#print("\nCientíficos:")
#imprimir_nombres(cientificos)

#print("\nOtros:")
#imprimir_nombres(otros)

# Imprimir la lista de nombres final
imprimir_listas(magos, cientificos, otros)