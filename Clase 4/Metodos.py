class Persona:
    nombre = ""
    apellido = ""
    edad = 0
    pais = ""

    def saludar(self):
        print("Hola mi nombre es", self.nombre)

    def despedida(self):
        print("Hasta pronto")

#calling methods
persona = Persona()

persona.saludar()
persona.despedida()