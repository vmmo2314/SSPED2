import os
#agenda
class agendaV2:
    def metodoCopiadoArchivos(self, name, code):
        # se abre el archivo en modo lectura
        archivo = open("original.txt", 'r')
        # se copia el archivo original en el de respaldo
        archivoRespaldo = open("respaldo.txt", 'w')
        for linea in archivo:
            archivoRespaldo.write(linea)
        # se cierran archivos
        archivo.close()
        archivoRespaldo.close()
        # se abre archivo de respaldo en modo lectura y el archivo original en modo escritura
        archivoRespaldo = open("respaldo.txt", 'r')
        archivo = open("original.txt", 'w')
        # se copia la informacion del de respaldo al original
        for linea in archivoRespaldo:
            archivo.write(linea)
        archivoRespaldo.close()
        archivo.write(f"{name}*{code}*")
        # se cierran archivos
        archivo.close()
    def agregarContacto(self):
        if os.path.exists("original.txt"): #validacion en caso de que no exista un txt llamado original
            print("El archivo 'original.txt' existe.")
            # se añade texto deseado en el original
            name = (input("Digita el nombre de la persona"))
            code = (input("Digita el codigo de la persona"))
            self.metodoCopiadoArchivos(name, code)
        else:
            print("El archivo 'original.txt' no existe.")
            archivo = open("original.txt", 'w')
            name = (input("Digita el nombre de la persona"))
            code = (input("Digita el codigo de la persona"))
            archivo.write(f"{name}*{code}*") #se escriben los datos con la cadena formateada junto con separadores de campo
    def menuAgenda(self):
        salir = ""
        while salir != "afirmativo":
            self.mostrarContactos()
            print("1)Agregar contacto \n2)Buscar contacto\n3)Salir")
            case = (input("Qué quieres hacer? \nSelecciona una opción\n"))

            if case == '1':
                os.system('cls')  # Comando para limpiar la pantalla en Windows
                print("Seleccionaste agregar contacto")
                self.agregarContacto()
            elif case == '2':
                os.system('cls')  # Comando para limpiar la pantalla en Windows
                print("Seleccionaste buscar contacto: \n")
                nombre = (input("Digita el nombre a buscar"))
                self.buscarContacto(nombre)
            elif case == '3':
                salir = "afirmativo"
            else:
                print("Selecciona una opción válida")

    import os

    def buscarContacto(self, fName):
        archivo = open("original.txt", 'r')  # Se abre el archivo original en modo lectura
        contenido = archivo.read()  # Leer el contenido del archivo
        palabras = contenido.split("*")  # Dividir el contenido por el separador de campo "*"

        agendaTemp = open("temp.txt", 'w')
        modificado = False
        contador = 0 #ayuda en caso de haber eliminado un nombre, así también se elimina el codigo
        for palabra in palabras:  # Iterar sobre las palabras obtenidas
            contador += 1 #si se eliminó un nombre, el contador aumenta a uno junto con el booleano "modificado"
            if palabra == fName: #si hay una coincidencia entre el nombre del txt y el que se busca modificar
                opc = input("El dato sí existe, deseas modificar el dato?\n [1] sí      [2] no      [3] Eliminar")
                if opc == "1" and not modificado:  #el booleano permite saber si ya se modificaron los datos
                    palabra = (input("Digita el nuevo dato, digita uno nuevo: \n"))
                    agendaTemp.write(palabra + "*")
                    modificado = True
                if opc == "2":
                    return
                if opc == "3": #caso eliminar
                    if palabra.isdigit(): #si la palabra es numero, significa que se eliminó un codigo
                        print("Eliminaste un codigo") #se requiere que reingrese un nuevo codigo
                        palabra = (input("Digita el nuevo dato, digita uno nuevo: \n"))
                        agendaTemp.write(palabra + "*")

                    else: #la palabra eliminada es un nombre y requiere doble eliminación
                        contador = 0
                modificado = True #Sirve para marcar que se modificaron datos o sí se encontró el dato a buscar
            elif contador == 1 and modificado:
                print("Eliminando codigo del usuario eliminado")
            else:
                agendaTemp.write(palabra + "*") ##En todo momento se escribe un documento auxiliar por si el usuario
                                                ##quiere modificó algun dato

        if not modificado:
            print("El nombre no existe")

        archivo.close()
        agendaTemp.close()

        if modificado:  # Verificar si se ha modificado antes de renombrar el archivo
            os.remove("original.txt")  # Eliminar el archivo original
            os.rename("temp.txt", "original.txt")  # Renombrar el archivo temporal a "original.txt"

    def mostrarContactos(self):
        if os.path.exists("original.txt"):  # validacion en caso de que no exista un txt llamado original
            print("Contactos actualmente cargados al documento...")
            archivo = open("original.txt", 'r') #se abre el archivo original en modo lectura
            # Leer el contenido del archivo
            contenido = archivo.read()
            # Dividir el contenido por el separador de campo "*"
            palabras = contenido.split("*")
            print("::Nombre::::Codigo::")

            cont = 0 ##para imprimir nombre junto con codigo y posteriormente un salto de linea
            # Iterar sobre las palabras obtenidas
            for palabra in palabras: #la variable palabra contiene los nombres y codigos
                if palabra != "":
                    print("::", palabra, "::", end='')
                cont += 1 #contador que sirve para mostrar el nombre junto con codigo sin salto de linea
                if cont == 2:#si el contador vale 2, ya se mostró un nombre y un codigo, entonces se requiere un salto de linea
                    print("\n")
                    cont = 0
            archivo.close()
        else:
            print("Lista de contactos vacía... \n Intenta agregar contactos :)")
            return


myAgenda = agendaV2()
myAgenda.menuAgenda()
