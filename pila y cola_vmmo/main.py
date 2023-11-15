import os
#ejemplo pila

class pila:
    def __init__(self):
        self.libros = []

    def isEmpty(self):
        return self.libros == []

    def apilar(self, libro):
        self.libros.append(libro)

    def desapilar(self):
        if self.isEmpty():
            print("La pila está vacía, intenta apilar primero :D")
            return
        else:
            return self.libros.pop() #el eliminacion retorna el dato eliminado

    def ultimoDato(self):
        if self.isEmpty():
            print("La pila está vacía, intenta apilar primero :D")
            return
        else:
            return self.libros[len(self.libros) - 1]

class cola:
    def __init__(self):
        self.coladelibros = []

    def isEmpty(self):
        return self.coladelibros == []

    def encolar(self, libro):
        self.coladelibros.append(libro)
    def desencolar(self):
        self.coladelibros.pop(0) #El cero indica que se eliminará el primer elemento
    def primerDato(self):
        if self.isEmpty():
            print("La cola está vacía, intenta apilar primero :D")
            return
        else:
            return self.coladelibros[0]

##Programa que apila libros
myPilaDeLibros = pila()

myColaDeLibros = cola()

case = ""
while case != "7":
    elementos = len(myPilaDeLibros.libros)
    elementosCola = len(myColaDeLibros.coladelibros)

    print("Elementos actualmente cargados en la pila: ", elementos, "\n")
    print("Elementos actualmente cargados en la cola: ", elementosCola, "\n")
    if elementos == 0:
        print("Sin elementos en la pila, intenta apilar :/")
    else:
        print("Listado pila:")
        for i in range(elementos - 1, -1, -1):
            print(myPilaDeLibros.libros[i] + "\n")
    print("----------------------------------------------------------------")
    if elementosCola == 0:
        print("Sin elementos en la cola, intenta encolar :(")

    else:
        print("Listado cola:")
        for i in range(elementosCola - 1, -1, -1):
            print(myColaDeLibros.coladelibros[i] + "\n")
    print("\n\n")
    print("*****OPCIONES DE PILA*****")
    print("1) Apilar    2) Desapilar     3) Retornar ultimo dato ingresado \n")

    print("*****OPCIONES DE COLA*****")
    print("4) Encolar    5) Desencolar     6) Retornar primer dato ingresado")
    case = (input("Menu: \n Selecciona una opcion: \n"))

    if case == "1":
        #libro = (input("Digita el nombre del libro: \n"))
        myPilaDeLibros.apilar(input("Inserta el libro que quieres apilar: "))
    elif case == "2":
        print("Dato eliminado: ", myPilaDeLibros.desapilar())
    elif case == "3":
        print("Ultimo libro: ", myPilaDeLibros.ultimoDato())
    elif case == "4":
        myColaDeLibros.encolar(input("Inserta el libro que quieres encolar: "))
    elif case == "5":
        print("Dato eliminado: ", myColaDeLibros.desencolar())
    elif case == "6":
        print("Primer libro", myColaDeLibros.primerDato())
    elif case == "7":
        break









