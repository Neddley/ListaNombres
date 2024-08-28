# Lista original de nombres
nombres = [
    "Harry Houdini", "Newton", "David Blaine", "Hawking", "Messi", 
    "Teller", "Einstein", "Pele", "Juanes"
]

# Clasificación de los nombres en grupos
def clasificar_nombres(nombres):
    magos = []
    cientificos = []
    otros = []
    
    for nombre in nombres:
        if nombre in ["Harry Houdini", "David Blaine", "Teller"]:
            magos.append(nombre)
        elif nombre in ["Newton", "Hawking", "Einstein"]:
            cientificos.append(nombre)
        else:
            otros.append(nombre)
    
    return magos, cientificos, otros

# Función para hacer a los magos grandiosos
def hacer_grandioso(magos):
    return ["El gran " + mago for mago in magos]

# Función para imprimir los nombres en una lista
def imprimir_nombres(titulo, lista):
    print(f"\n{titulo}:")
    for nombre in lista:
        print(nombre)

# Función principal para la ejecución del programa
def main():
    # Imprimir nombres originales
    imprimir_nombres("Nombres originales", nombres)
    
    # Clasificar nombres
    magos, cientificos, otros = clasificar_nombres(nombres)
    
    # Hacer grandiosos a los magos
    magos = hacer_grandioso(magos)
    
    # Imprimir las listas finales
    imprimir_nombres("Magos grandiosos", magos)
    imprimir_nombres("Científicos", cientificos)
    imprimir_nombres("Otros", otros)

# Ejecución del programa principal
if __name__ == "__main__":
    main()