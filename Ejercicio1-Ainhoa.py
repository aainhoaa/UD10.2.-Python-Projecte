# Función para mostrar el menú y obtener la opción del usuario
def mostrar_menu():
    print("Bienvenido al programa de Ainhoa M.")
    print("1. Sumar una lista de números")
    print("2. Leer un archivo y obtener una lista de líneas")
    print("3. Juego de memòria")
    print("4. Aplicación de una tienda")
    print("5. Scraping de datos web")
    print("6. Aplicación web de tienda en línea")
    print("0. Salir")

    opcion = input("Ingrese su opción: ")
    return opcion

# Función principal para ejecutar el programa
def main():
    opcion = mostrar_menu()

    while opcion != "0":
        if opcion == "1":
            numeros = [int(n) for n in input("Ingrese una lista de números separados por espacios: ").split()]
            resultado = sumar_lista(numeros)
            print(f"El resultado de la suma es: {resultado}")
        elif opcion == "2":
            ruta = input("Ingrese la ruta del archivo: ")
            lineas = leer_archivo(ruta)
            print("Las líneas del archivo son:")
            for linea in lineas:
                print(linea.strip())
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")

        opcion = mostrar_menu()

    print("Gracias por usar el programa. Hasta luego!")

if __name__ == "__main__":
    main()
