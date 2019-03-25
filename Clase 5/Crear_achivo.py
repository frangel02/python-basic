def crear_archivo():
    archivo = open('datos.txt', 'w')
    archivo.close()


def escribir_archivo():
    archivo = open('datos.txt', 'a')
    archivo.write('Jose Lujan\n')
    archivo.write('8095565548\n')
    archivo.write('Mexico')

def leer_archivo():
    archivo = open('datos.txt', 'r')
    linea = archivo.readline()
    while linea != "":
        print(linea)
        linea = archivo.readline()
    archivo.close()


crear_archivo()
escribir_archivo()
leer_archivo()