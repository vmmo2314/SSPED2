#se abre el archivo en modo lectura
archivo = open("original.txt",'r')
#se copia el archivo original en el de respaldo
archivoRespaldo = open("respaldo.txt", 'w')
for linea in archivo:
    archivoRespaldo.write(linea)
#se cierran archivos
archivo.close()
archivoRespaldo.close()
#se abre archivo de respaldo en modo lectura y el archivo original en modo escritura
archivoRespaldo = open("respaldo.txt", 'r')
archivo = open("original.txt",'w')
#se copia la informacion del de respaldo al original
for linea in archivoRespaldo:
    archivo.write(linea)
#se añade texto deseado en el original
texto = "1"
while(texto != "0"):
    texto = (input("Ya puedes ingresar la información o digita 0 para salir\n"))
    if(texto != "0"):
        archivo.write(texto)
        archivo.write("\n")
#se cierran archivos
archivo.close()
archivoRespaldo.close()
