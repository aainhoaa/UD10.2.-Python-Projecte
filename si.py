import random

def aplicacion1():
    # Función para trabajar con listas y números aleatorios
    lista = [1, 2, 3, 4, 5]
    numero_aleatorio = random.choice(lista)
    print("Número aleatorio:", numero_aleatorio)

def aplicacion2():
    # Función para trabajar con archivos
    # Aquí puedes implementar la lógica para guardar y manipular la información en archivos
    pass

def aplicacion3():
    # Función para implementar un juego
    # Puedes desarrollar el juego que mencionaste aquí
    pass

def aplicacion4():
    # Función para trabajar con objetos, clases, herencia, polimorfismo, etc.
    # Aquí puedes implementar la lógica relacionada con la programación orientada a objetos
    pass

def aplicacion5():
    # Función para trabajar con big data, scrapping, etc.
    # Puedes utilizar librerías como Pandas, BeautifulSoup, etc.
    pass

def aplicacion6():
    # Función para montar un servicio web
    # Puedes utilizar un framework como Flask o Django para crear el servidor web
    pass

# Programa principal
def main():
    print("Selecciona una de las siguientes aplicaciones:")
    print("1. Trabajar con listas y números aleatorios")
    print("2. Trabajar con archivos")
    print("3. Juego")
    print("4. Trabajar con objetos y clases")
    print("5. Trabajar con big data y scrapping")
    print("6. Montar un servicio web")
    
    opcion = int(input("Ingresa el número de la aplicación que deseas ejecutar: "))
    while opcion != "0":
        if opcion == 1:
            aplicacion1()
        elif opcion == 2:
            aplicacion2()
        elif opcion == 3:
            aplicacion3()
        elif opcion == 4:
            aplicacion4()
        elif opcion == 5:
            aplicacion5()
        elif opcion == 6:
            aplicacion6()
        else:
            print("Opción inválida. Por favor, ingresa un número válido.")
    print("Gracias por usar el programa de Ainhoa M. Hasta pronto!")
    
if __name__ == "__main__":
    main()