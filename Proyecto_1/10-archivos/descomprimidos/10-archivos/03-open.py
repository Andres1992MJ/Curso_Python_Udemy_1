from io import open


#Aca vamos a coger el archivo y escribimos, si no existe lo crea, Pilas porque sobreescribe todo el archivo
texto= "hola mundo desde open"

archivo = open("10-archivos/archivo-prueba_2.txt", "w")

archivo.write(texto)
archivo.close()

print("1-------------------------------------")
#Aca podemos leer el archivo y traerlo tal cual
archivo_lectura = open("10-archivos/archivo-prueba.txt", "r")

texto_leido= archivo_lectura.read()

archivo_lectura.close()

print(texto_leido)

print("2-------------------------------------")
#Aca lo vamos a traer dividiendo cada salto de linea en listas, por si requiere algun trabajo

archivo_lectura_lista = open("10-archivos/archivo-prueba.txt", "r")

texto_leido_lista= archivo_lectura_lista.readlines()

archivo_lectura_lista.close()

print(texto_leido_lista)


print("3-------------------------------------")
#Aca lo vamos a traer dividiendo cada salto de linea en listas, por si requiere algun trabajo pero with tiene metodo de cierre automatico
with open("10-archivos/archivo-prueba.txt", "r") as archivo:
    print(archivo.readlines())
    archivo.seek(0)
    print("3.1-------------------------------------")

    for linea in archivo:
        print(linea)

print("4-------------------------------------")

#Aca vamos a escribir adelante de la ultima letra que exista
archivo3 = open("10-archivos/archivo-prueba_2.txt", "a+")

archivo3.write("Chao mundo :(")
archivo3.close()

print("5-------------------------------------")

#aca vamos a leeer y escribir

with open("10-archivos/archivo-prueba_3.txt", "r+") as archivo:
    texto= archivo.readlines()
    archivo.seek(0)
    texto[0]= "YA es hora de almorzar :(("
    print(texto)
    archivo.writelines(texto)