class CifradoCesar:
    def __init__(self, archivo, desplazamiento):
        self.archivo = archivo
        self.desplazamiento = desplazamiento

    def leer_archivo(self):
        with open(self.archivo, "r") as archivo:
            self.texto = archivo.read()

    def cifrar(self):
        texto_codificado = ""
        for letra in self.texto:
            if letra.isalpha():
                codigo = ord(letra) + self.desplazamiento
                if letra.isupper():
                    if codigo > ord('Z'):
                        codigo -= 26
                    elif codigo < ord('A'):
                        codigo += 26
                else:
                    if codigo > ord('z'):
                        codigo -= 26
                    elif codigo < ord('a'):
                        codigo += 26
                letra_codificada = chr(codigo)
            else:
                letra_codificada = letra
            texto_codificado += letra_codificada
        self.texto_codificado = texto_codificado

    def escribir_archivo_codificado(self):
        with open("CancionCodificada.txt", "w") as archivo_codificado:
            archivo_codificado.write(self.texto_codificado)

    def descifrar(self):
        with open("CancionCodificada.txt", "r") as archivo_codificado:
            texto_codificado = archivo_codificado.read()
        texto_descodificado = ""
        for letra in texto_codificado:
            if letra.isalpha():
                codigo = ord(letra) - self.desplazamiento
                if letra.isupper():
                    if codigo < ord('A'):
                        codigo += 26
                    elif codigo > ord('Z'):
                        codigo -= 26
                else:
                    if codigo < ord('a'):
                        codigo += 26
                    elif codigo > ord('z'):
                        codigo -= 26
                letra_descodificada = chr(codigo)
            else:
                letra_descodificada = letra
            texto_descodificado += letra_descodificada
        with open("CancionDecodificada.txt", "w") as archivo_descodificado:
            archivo_descodificado.write(texto_descodificado)

    def imprimir_codificado(self):
        print(self.texto_codificado)

archivo = "apocalypse.txt"
desplazamiento = 1
cifrado = CifradoCesar(archivo, desplazamiento)
cifrado.leer_archivo()
cifrado.cifrar()
cifrado.escribir_archivo_codificado()
cifrado.descifrar()
