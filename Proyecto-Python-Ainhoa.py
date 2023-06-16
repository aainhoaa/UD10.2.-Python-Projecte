def sumar_lista(): #Primera funcion
    numeros = []
    for i in range(1,6):
        numero = int(input(f"Ingrese su número {i}: ")) #Pide al usuario que ingrese un número.
        numeros.append(numero) #Agrega el número a la lista.
    sumar = sum(numeros) #Suma los números en la lista.
    print(f"La suma de los números es: {sumar}") #Imprime el resultado.
    return sumar

def leer_archivo(ruta): #Segunda Funcion
    with open(ruta,'r') as archivo: #Abre el archivo en modo lectura.
        lineas=archivo.readlines() #Lee todas las líneas del archivo y las guarda en una lista.
    print('Las lineas del archivo son: ')
    for linea in lineas: #Itera sobre cada línea en la lista de líneas.
        print(linea.strip()) #Imprime la línea sin espacios en blanco al principio o al final.

    respuesta = input("¿Deseas editar el archivo? (s/n): ") #Pregunta al usuario si desea editar el archivo.
    if respuesta == "s": #Si el usuario responde "s"
        with open(ruta, 'w') as archivo: #Abre el archivo en modo escritura.
            archivo.write(input("Escribe el nuevo contenido: ")) #Pide al usuario que ingrese el nuevo contenido y lo escribe en el archivo.

    return lineas #Devuelve la lista de líneas del archivo.

import random #Importa la biblioteca random para generar números aleatorios.
def juego(): #Tercera funcion
    continuar = 1 #Inicializa la variable "continuar" con el valor 1.
    while continuar==1: #Inicia un bucle while que se ejecuta mientras "continuar" es igual a 1.
        print("Bienvenido a Mastermind.\nElija la dificultad del juego:\n1. Facil\n2. Normal\n3.Dificil\n") #Imprime un mensaje de bienvenida y las opciones de dificultad.
        dificultad = int(input("La dificultad a elegir es:")) #Pide al usuario que ingrese la dificultad del juego y lo convierte en un número entero.

        if dificultad == 1: #Si la dificultad es igual a 1.
            n_digitos = 3 #Establece el número de dígitos en 3.
        elif dificultad == 2: #Si la dificultad es igual a 2.
            n_digitos = 4 #Establece el número de dígitos en 4.
        elif dificultad == 3: #Si la dificultad es igual a 3.
            n_digitos = 5 #Establece el número de dígitos en 5.

        digitos = ['0','1','2','3','4','5','6','7','8','9'] #Crea una lista de dígitos.
        codigo = '' #Inicializa la variable "codigo" como una cadena vacía.

        for i in range(n_digitos): #Inicia un bucle for que se ejecuta "n_digitos" veces.
            elegido = random.choice(digitos) # Elige un dígito aleatorio de la lista "digitos".
            while elegido in codigo: #Inicia un bucle while que se ejecuta mientras "elegido" ya está en "codigo".
                elegido = random.choice(digitos) #Elige otro dígito aleatorio de la lista "digitos".
            codigo = codigo+elegido #Agrega el dígito elegido a la variable "codigo".

        print(f"Tienes que adivinar un codigo de {n_digitos} digitos distintos.") #Imprime un mensaje que indica cuántos dígitos tiene el código secreto.
        propuesta = input("Que codigo propones?: ") #Pide al usuario que proponga un código.

        intentos = 1 #Inicializa la variable "intentos" con el valor 1.

        while propuesta != codigo: #Inicia un bucle while que se ejecuta mientras "propuesta" no es igual a "codigo".
            intentos = intentos+1 #Incrementa la variable "intentos" en 1.
            aciertos = 0 #Inicializa la variable "aciertos" con el valor 0.
            coincidencias = 0 #Inicializa la variable "coincidencias" con el valor 0.
            for i in range(n_digitos): #Inicia un bucle for que se ejecuta "n_digitos" veces.
                if propuesta[i] == codigo [i]: #Si el i-ésimo dígito de "propuesta" es igual al i-ésimo dígito de "codigo",
                    aciertos = aciertos+1 #Incrementa la variable "aciertos" en 1.
                elif propuesta[i] == codigo: #Si el i-ésimo dígito de "propuesta" no es igual al i-ésimo dígito de "codigo", pero está en algún lugar del código,
                    coincidencias = coincidencias+1 #incrementa la variable "coincidencias" en 1.
            print(f"Tu propuesta {propuesta} tiene {aciertos}, y {coincidencias} coincidencias.") #Imprime un mensaje que indica cuántas coincidencias y aciertos hay entre el código secreto y la propuesta del usuario.
            propuesta = input("Propon otros digitos: ") #Pide al usuario que proponga otro código.

        print(f"Felicidades! Adivinaste el codigo en {intentos} intentos.") #Este mensaje sale cuando ganamos y nos indica la cantidad de intentos que nos ha llevado.
        continuar=int(input("Desea seguir jugando?\nSi = 1\nNo = 0\nIndique su respuesta: ")) #Mensaje que pregunta al usuario si queire volver a jugar o no.

def animales(): #Cuarta Funcion
    #Definimos una clase Animal que representa una entidad general con atributos y métodos comunes.
    class Animal:
        #El método __init__ se ejecuta al crear una instancia de la clase y recibe los parámetros especie y edad.
        def __init__(self, especie, edad):
            #Asignamos los parámetros a los atributos de la instancia.
            self.especie=especie
            self.edad=edad
        #Definimos un método hablar que no hace nada por defecto, pero se puede sobrescribir en las subclases.
        def hablar(self):
            pass
        #Definimos un método movimiento que no hace nada por defecto, pero se puede sobrescribir en las subclases.
        def movimiento(self):
            pass
        #Definimos un método soy que imprime el tipo de animal que es la instancia.
        def soy(self):
            print("Soy un animal del tipo {}".format(self.especie))

    #Definimos una clase Caballo que hereda de la clase Animal y representa un animal específico.
    class Caballo(Animal):
        #Sobrescribimos el método hablar para que imprima el sonido característico del caballo.
        def hablar(self):
            print("El sonido que me caracteriza es: iiiiiii")
        #Sobrescribimos el método movimiento para que imprima la forma de moverse del caballo.
        def movimiento(self):
            print("Me muevo trotando!")

    #Definimos una clase Delfin que hereda de la clase Animal y representa otro animal específico.
    class Delfin(Animal):
        #Sobrescribimos el método hablar para que imprima el sonido característico del delfín.
        def hablar(self):
            print("El sonido que me caracteriza es: Txasss!")
        #Sobrescribimos el método movimiento para que imprima la forma de moverse del delfín.
        def movimiento(self):
            print("Me muevo nadando!")

    #Definimos una clase Abeja que hereda de la clase Animal y representa otro animal específico.
    class Abeja(Animal):
        #Sobrescribimos el método hablar para que imprima el sonido característico de la abeja.
        def hablar(self):
            print("El sonido que me caracteriza es: Bzzzzz!")
        #Sobrescribimos el método movimiento para que imprima la forma de moverse de la abeja.
        def movimiento(self):
            print("Me muevo volando!")
        #Definimos un método picar que imprime una advertencia si se molesta a la abeja.
        def picar(self):
            print("Si me molestas, te picare")

    #Definimos una clase Humano que hereda de la clase Animal y representa otro animal específico.
    class Humano(Animal):
        #Sobrescribimos el método __init__ para que reciba un parámetro adicional: nombre.
        def __init__(self, especie, edad, nombre):
            #Llamamos al método __init__ de la superclase para asignar los atributos especie y edad.
            super().__init__(especie,edad)
            #Asignamos el parámetro nombre al atributo de la instancia.
            self.nombre=nombre
        #Sobrescribimos el método hablar para que imprima el sonido característico del humano.
        def hablar(self):
            print("El sonido que me caracteriza es la palabra Hola!")
        #Sobrescribimos el método movimiento para que imprima la forma de moverse del humano.
        def movimiento(self):
            print("Me muevo caminando")
        #Sobrescribimos el método soy para que imprima el nombre del humano además del tipo de animal.
        def soy(self):
            print("Soy un humano y me dicen {}".format(self.nombre))

    #Definimos una clase Fiet que hereda de la clase Humano y representa un tipo específico de humano con un atributo adicional: padres.
    class Niño(Humano):
        #Sobrescribimos el método __init__ para que reciba un parámetro adicional: padres.
        def __init__(self, especie, edad, nombre, padres):
            #Llamamos al método __init__ de la superclase para asignar los atributos especie, edad y nombre.
            super().__init__(especie,edad,nombre)
            #Asignamos el parámetro padres al atributo de la instancia.
            self.padres=padres
        #Definimos un método nombre_padres que imprime el nombre de los padres del Fiet.
        def nombre_padres(self):
            print("Mi padre se llama {} y mi madre {}".format(self.padres[0],self.padres[1]))

    #Creamos una lista de instancias de las clases definidas anteriormente con diferentes valores para los atributos.
    f= [Humano("Humano", 32, "Joan"), Caballo('mamifero', 10), Delfin('mamifero', 23), Abeja('insecto', 1), Niño('humano', 6, 'Pau',('Joan', 'Luz'))]

    #Creamos una lista vacía para almacenar los nombres de las clases de las instancias creadas.
    nombres = []
    #Recorremos la lista de instancias y usamos el método __class__.__name__ para obtener el nombre de la clase de cada una y lo añadimos a la lista nombres.
    for e in f:
        nombres.append(e.__class__.__name__)

    #Imprimimos un mensaje para preguntar al usuario qué animal quiere.
    print("¿Qué animal quieres?")
    #Recorremos la lista nombres y usamos el índice para mostrar las opciones disponibles al usuario.
    for i in range(len(nombres)):
        print("{} - {}".format(i+1, nombres[i]))
    #Pedimos al usuario que ingrese el número del animal que quiere y lo convertimos a entero.
    opcion = int(input("Ingresa el número del animal: "))

    #Verificamos si la opción ingresada es válida, es decir, si está dentro del rango de la lista nombres.
    if opcion < 1 or opcion > len(nombres):
        #Si no es válida, imprimimos un mensaje de error.
        print("Opción inválida")
    else:
        #Si es válida, obtenemos la instancia correspondiente a la opción elegida usando el índice de la lista f.
        animal = f[opcion-1]
        
        #Llamamos al método soy de la instancia para que imprima su tipo y nombre si es humano o Fiet.
        animal.soy()
        #Llamamos al método movimiento de la instancia para que imprima su forma de moverse.
        animal.movimiento()
        #Llamamos al método hablar de la instancia para que imprima su sonido característico.
        animal.hablar()
        #Imprimimos el atributo edad de la instancia usando el formato string.
        print("Tengo {} años".format(animal.edad))
        
        #Verificamos si la instancia es de tipo Fiet usando la función type.
        if type(animal)==Niño:
            #Si es así, llamamos al método nombre_padres de la instancia para que imprima el nombre de sus padres.
            animal.nombre_padres()
        #Verificamos si la instancia es de tipo Abeja usando la función type.
        if type(animal)==Abeja:
            #Si es así, llamamos al método picar de la instancia para que imprima una advertencia.
            animal.picar()
    
import requests

import requests #Importamos el módulo requests para hacer peticiones HTTP.

def return_clima(ciudad): #Quinta Funcion
    #Definimos una función que recibe el nombre de una ciudad y devuelve la temperatura y la descripción del clima.
    url=f"https://es.wttr.in/{ciudad}?format=j1" #Creamos una variable con la URL de la API que nos da el clima.
    respuesta = requests.get(url) #Hacemos una petición GET a la URL y guardamos la respuesta en una variable.
    clima_dic = respuesta.json() #Convertimos la respuesta en un diccionario de Python usando el método json().
    temp_c = clima_dic["current_condition"][0]['temp_C'] #Obtenemos la temperatura en grados Celsius del diccionario.
    desc_temp = clima_dic["current_condition"][0]['lang_es'] #Obtenemos la descripción del clima en español del diccionario.
    desc_temp = desc_temp[0]['value'] #Obtenemos el valor de la descripción del clima como una cadena de texto.
    return temp_c, desc_temp #Devolvemos la temperatura y la descripción del clima como una tupla.

def localidad(): #Quinta funcion
    #Definimos una función que no recibe ningún parámetro y muestra el clima de una ciudad ingresada por el usuario.
    ciudad = input("Introduce el nombre de tu ciudad: ") # Pide al usuario que ingrese el nombre de su ciudad y lo guarda en una variable.
    temp_c, desc_temp = return_clima(ciudad) # Llama a la función return_clima() para obtener la información del clima y la guarda en dos variables.
    print(f"La temperatura actual de {ciudad} es de {temp_c} °C. {desc_temp}.") # Muestra la información del clima en la pantalla usando una cadena formateada.

if __name__ == '__localidad__': #Quinta funcion
    #Verificamos si el módulo se ejecuta como programa principal usando la variable especial __name__.
    localidad() #Llama a la función localidad().


def mostrar_menu():
    #Definimos una función que no recibe ningún parámetro y muestra un menú con las opciones del programa.
    print ("\nBienvenido al programa de Ainhoa M.\n") # Imprimimos un mensaje de bienvenida.
    print("1. Sumar una lista de numeros.\n2. Leer un archivo y obtener una lista de lineas.\n3. Jugar a adivinar digitos.\n4. Trabajar con animales y clases.\n5. Saber la temperatura actual de una ciudad.\n6. Salir.\n") #Imprimimos las opciones disponibles.
    opcion=input("Ingrese su opcion: ") # Pedimos al usuario que ingrese su opción y la guardamos en una variable.
    return opcion #Devolvemos la opción ingresada.

def main():
    #Definimos una función que no recibe ningún parámetro y ejecuta el programa principal.
    opcion=mostrar_menu() #Llamamos a la función mostrar_menu() y guardamos la opción devuelta en una variable.

    while opcion!= "6": #Mientras la opción no sea 6 (salir).
        if opcion == "1": #Si la opción es 1.
            sumar_lista() #Llamamos a la función sumar_lista() que suma una lista de números.
        elif opcion == "2": #Si la opción es 2.
            ruta = input("Ingrese la ruta del archivo: ") #Se solicita la ruta del archivo al usuario y se guarda en una variable.
            leer_archivo(ruta) #Se pasa la ruta del archivo como argumento a la función leer_archivo() que lee el archivo y obtiene una lista de líneas.
        elif opcion == "3": #Si la opción es 3.
            juego() #Llamamos a la función juego() que permite jugar a adivinar dígitos.
        elif opcion == "4": #Si la opción es 4.
            animales() #Llamamos a la función animales() que trabaja con animales y clases.
        elif opcion == "5": #Si la opción es 5.
            localidad() #Llamada a la función localidad() que muestra el clima de una ciudad ingresada por el usuario.

        else: #Si la opción no es ninguna de las anteriores.
            print("\nOpcion invalida. Por favor, ingrese una opcion invalida.\n") # Imprimimos un mensaje de error.
        
        opcion = mostrar_menu() #Volvemos a llamar a la función mostrar_menu() y actualizamos el valor de la variable opción.
    print('Gracias por usar el programa de Ainhoa M.\n\nHasta luego!') #Imprimimos un mensaje de despedida.

main() #Llamamos a la función main() para ejecutar el programa principal.
