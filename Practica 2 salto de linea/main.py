#1 se abre el archivo
archivo=open("file01.txt", "r")

for linea in archivo:
    print(linea, end="")
archivo.close()