"esrto es un sttrink" # esto es un comentario
# tipos de datos enteros
385 
[] # lista vacia

lista = ["hola",3,5,6,8,9] #lista cargada
# variables una carpeta que puede tener muchos elementos y puede ser modificada en cualquier momento se agrega con =
#lista.apepend  como agregar
#lista.pop() elimina el ultimo elemento de la lista
#for son buclues genera un paso por todos los elementos
#acceder a un elemento de la lista
# modificar un elemento de la lista ej:variable_lista[2]= 50
for loquesea in lista:
    print (loquesea)
for cualquieracosa in range(10):
    print(cualquieracosa + 1)
#imprimir ultimo elemento de una lista sin sber cuantos elementos tiene
otra_lista=["hola", "chau", "vos", "no"]
dimension_de_lista= len(otra_lista) -1
print(otra_lista[dimension_de_lista])
#otro metodo
dimension_de_lista= len(otra_lista)
indice_ultimo = dimension_de_lista -1
print(indice_ultimo)
otra_lista[indice_ultimo]
print(otra_lista[indice_ultimo])



#como imprimir un rango
for numero in range(1,11):
    print(numero)


for numero in range (10):
    print("hola", numero)

#imprimir el numero de resultado de la suma de los numeros del 1 al 10


#################FUNCIONES#######################

#def  definir ppamar una funcion- 
def suma(num1, num2):
    resultado = num1 + num2
    return num1 + num2
print(suma (5,10))
result= suma(5,8)
print(result)
#crear una funcion resta, que reciba como parametro dos numeros y que retorne ls resta de esos numeros luegollamar a la funcion imprimir

def resta (num1, num2):
    resultado= num1 - num2
    return resultado

print(resta(18,8))
#cresar la funcion saludo llamar distintas veces a los valoresretornar es algo opcionl

def saludo (nombre, edad):
  print("hola soy", nombre, "y tengo", edad, "anhos")
  resultado = "un gusto conocerte"
  print(resultado)
  return resultado

saludo("Sirley",29)
saludo("Raul", 30)
saludo("Cris", 24)
saludo("mark", 19)
saludo("mit", 25)
#ej crear una funciodesafio= [1,2,3,4,5,6,7,8,9,10] # se crea una lista

def suma_lista (listita):
    a=0
    for casa in listita:
        a = a+ casa
    return a
ayna=[1,2,3,4,5]
suma_lista(ayna)
print(suma_lista(ayna))
ayayai=[100,5,5]
suma_lista(ayayai)
print(suma_lista(ayayai))
#ej 2blista al cuadrado
#crear una funcion que reciba una lista de nuevo como parametro
#y retorne una lista con los numeros al cuadrado
#lista cuadrado[1,4,9,16,25]

def lista_cuadrado(listajeyma):
  a=[]
  for jeyma in listajeyma:
    a.append(jeyma * jeyma)
  return a


otrave=[1,4,9,16,25]
listax=[2,3,5]
lista_cuadrado((otrave))
print(lista_cuadrado(otrave))

print(lista_cuadrado(listax))
print(lista_cuadrado([2,2,2,2]))

def lilis (two):
    a=[]
    for lolo in two:
        a.append(lolo*lolo)
        return a


#figonachi una sserie que empiexa con dos elemntos 0,1 y se calcula e4l siguiente termino sumando los dos ultimos elementos de la serie
#0+1= 1
#1+1= 2
#1+2=3
#2+3=5
#3+5=8
#5+8=13
#8+13=21
#13+21=34
def figo(x):
    a=0
    b=1
    for i in range(x):
        c=a+b
        a=b
        b=c
    print(c)

#figo(5)
grupo5=["n","f1","f2","a"]
print("antes",grupo5)
for i in grupo5:
    grupo5.pop()
print("despues",grupo5) #en este caso solo elimina la mitad por el recorrido de for
#return se usa para guardar el resultado y poder utilizarlo despues
for i in range (len(grupo5)):
    grupo5.pop()
print(grupo5)
#en este caso elimina todo el rango de elementos dentro de la lista 5
###################################
#crear una funcion de suma cuadrado que reciba una lista de numeros y retorne el valor de la suma de cada numero al cuaddrado
#[1,2,3,] 1+4+9=14
lista_n=[1,2,3]
def suma_cuadrado (lista_n):
  suma=0
  for p in lista_n:
    suma=suma + (p*p)
  return suma
print(suma_cuadrado(lista_n))


    
    



    