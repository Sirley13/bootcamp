a = 10
b=3 
print(a)
# al poner = guarda un dato dentro de una caja
# entre parentesis resuelve los ejercicios
# poner comillas es para palabras
# comillas y + es la sumatoria de los strings
print("hola mundo")
print(a+b)
print("hola", 2, "chau")
# al poner entre comas si combina textos y numeros
# ej. crear una variable nombre y una variable edad con nuestros datos e imprimir
# variable es =

nombre="sirley" 
edad = 29 
hobby= "escuchar musica"
print("hola, me llamo", nombre, "tengo", edad, "anhos" " y mi hobby es", hobby)
lista_vacia=[] #los corchetes represenan listas.
listax=[1,2,4,6,8]
datos="sirley"
print(datos)
# crear una lista de datos que en el primer lugar este tu nomre
# y en la segunda posicion este tu edad
#imprimir "hola me llamo........, y tengo....... anhos"
alumnos= [ nombre, edad, hobby]  
print("hola, me llamo" ,alumnos[0],"y tengo" ,alumnos[1])
# agragar tercera posicion hobby
print("hola, me llamo", alumnos[0], "y tengo",alumnos[1],"mi hobby es",alumnos[2] )
alumnos[1]= 25 
print("hola, me llamo", alumnos[0], "y tengo",alumnos[1],"mi hobby es",alumnos[2] )
#para modificar algun dato coloco la carpeta, identifico la posicion e igualo al nuevo dato y vuelvo a imprimir
print(alumnos)
alumnos.append("programador")
print(alumnos)
#ej. agregar una profesion y un hobby a la lista datos previamente creada. el punto relaciona la accion siguiente
datos=[nombre,edad,hobby]
print(datos)
datos.append("administradora") # agrega otra opcion a la lista
print(datos)

nombre="sirley" 
edad = 25
hobby= "escuchar musica"
profesion= "administradora"
print(datos)
datos.pop() #para eliminar el ultimo caracter agregado
print(datos)
# funcion len() longitud o dimencion de algo, püara saber cuantos elementos tiene una lista
print(len(datos))
dimension_de_datos= len(datos)
print(dimension_de_datos)
# ej. obtener la dimencion de la lista de datos e imprimir
# la lista de datos tiene
print("la lista de datos tiene", dimension_de_datos, "elementos")
#ej. imprimir el ultimo elemento de una lista que no sabemos cuantos elementos tiene
lista_larga = [2,4,3,5,6,7,8,9,0,8,7,6,5,3,5,645,7,8,9,4,23,5,7,89]
print(lista_larga)
dimension_de_datos= len(lista_larga) - 1
print(lista_larga[dimension_de_datos])
#### bucles/loops/ciclos/interacciones###
#bucle for recorre elemento por elemento una lista para utilizar los rangos
lista_temas= ["variables", "listas", "tipos de datos"]
print(lista_temas)
#: todo lo que viene despues es tabulado o lista de codigos
for concepto in lista_temas:
    print("hoy aprendi", concepto) 
    print("que gusto")
print("esto es lo que aprendi hoy")
for variable_for in lista_temas:
        #bloque de codigo
        print("esto se repite")
print("esto no se repite")
# recorrer una lista e imprimir en cada ciclo
#el valor del elemento con 3 signos de admiracion
lista_larga = [2,4,3,5,6,7,8,9,0,8,7,6,5,3,5,645,7,8,9,4,23,5,7,89]

for variables  in lista_larga:
    print(variables,"!!!")
print("fin")
# reange repite las vecs que se quiera una palabra
for w in range(1,101):
    print("hola", w)
suma = 0
for i in range(1,11):
    suma = suma + i
    print("hola", suma)

