
class Persona:  # definimos la plantilla para crear un objeto
    edad = 0    # propiedad del objeto/atributo de clase
    nacionalidad= " "
    grado= " "
    aloja= " "

    def __init__ (self, un_nombre):     # formula de la funcion para crear un objeto
                                        # metodo para las caracteristicas del objeto
        self.mi_nombre = un_nombre      #usamos self para relacionarnos al objeto mismo
        print("hola naci, me llamo",self.mi_nombre) # imprimimos el objeto con nombre 

    def cumple(self):                   # agregamos una funcion edad al objeto
        self.edad = self.edad + 1       # aumenta la propiedad edad en 1
        print(self.edad)

    def estudio(self):                  # agregamos una propiedad estudio
        self.grado = "inicio jardin"    #agrega la propiedad de grado
        print(self.grado)
    def nac(self,una_nac):
        self.nacionalidad = una_nac
            #metodo
    def saludo(self, hi):
        self.aloja = hi
        print(self.aloja)

pepe= Persona("pepito")                # crea la persona u objeto

pepe.nac("paraguayo")
pepe.saludo("hola soy y mi nacionalidad es "+ pepe.nacionalidad)
print(pepe.aloja)
print(pepe.edad)                       # imprime la edad del objeto
print(pepe.mi_nombre)

pepe.cumple()
print(pepe.edad)
pepe.estudio()                       # pepe es un objeto de clase de persona
print(pepe.grado)

print(pepe.nacionalidad)


# hacer una clase que se llame vehiculo y que tenga 3 atributos y que uno de ellos sea cantidad de ruedas
# y un metodo que sea definir_tipo que me diga si es"bicicletam, triciclo,auto"
class Vehiculo:
    ruedas= ""
    color= ""
    anho = ""
    def __init__(self,cant_ruedas,un_color,un_anho):
        self.ruedas= cant_ruedas
        self.color= un_color
        self.anho= un_anho

    def definir_tipo(self):
        if self.ruedas==2:
            print("El vehiculo es una bicicleta",self.color, self.anho)
        elif self.ruedas==3:
            print("El vehiculo es un triciclo",self.color, self.anho)
        elif self.ruedas==4:
            print("El vehiculo es un auto",self.color,self.anho)
movil= Vehiculo(2, "azul", 1995)      #PARA LLAMAR  VARIABLE= NIMBRE DE LA CLASE (LOS PARAMETROS)
movil.definir_tipo()                  # LA LLAMADA EN SI
movil= Vehiculo(4, "gris", 2005)
movil.definir_tipo()