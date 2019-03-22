#Tuplas
tupla = (1, 2, 3)
tupla2 = ('aaaa', 'bbbb', 'cccc')
tupla3 = (1, 'aaaa', True, 1.9)
print(tupla3[2])

def enviar_datos():
    nombre = 'jose'
    correo = 'jlms@gmail.com'
    edad = 20
    ciudad = 'cancum'
    return (nombre, correo, edad, ciudad)

def recibir_datos(datos):
    print(datos[0])
    print(datos[1])
    print(datos[2])


enviar_datos()

recibir_datos(enviar_datos())
