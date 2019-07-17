

class Dino:
    ojos=2
    def __init__(self, un_nombre, un_color, canti_patas, un_genero=None):
        self.nombre= un_nombre
        self.color= un_color
        self.patas= canti_patas
        self.genero= un_genero
        print("holii")
    def saludar(self):
        print("hola me llamo", self.nombre, "tengo", self.patas, "patas soy", self.genero, "y mi color es", self.color)
    
    def corta_pata(self, cant_de_patas=2):
        self.patas=self.patas - cant_de_patas

mar = Dino("marck", "verde", 4, "indefinido")
mar.saludar()  # accion/metodos termina con parentesis.
car= Dino("carlos", "lila", 4,"macho")
mar.saludar()
car.saludar()
mar.corta_pata()
car.saludar()

######### herencia ###############
 
class Trex (Dino):

    def __init__ (self, nombre, patas=8,color=None):
        self.nombre = nombre
        self.patas = patas
        self.color = color
print("hola soy un Trex y me llamo", self.nombre)

ricardo = Trex("ricardro el Trex ")
print(ricardo.ojos)
ricardo.saludar()
ricardo.genero()
ricardo.esta_vivo()
ricardo.saludar()
 