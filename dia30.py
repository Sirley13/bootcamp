# repaso
#
ing_pan= ["harina", "levadura", "sal", "azucar", "agua"]
# def imprimir_lista(ingredientes, nombre_producto):
#     print("lista de compras de", nombre_producto)
#     print("......................")
#     for producto in ingredientes:
#         print(producto)
# imprimir_lista(ing_pan,"pan")
# ing_salsa=["tomate","azucar", "cebolla"]
# imprimir_lista(ing_salsa,"salsa")
# #####################condicionales#########################

# # == igual
# #> mayor que
# #< menor que
# #>= mayor igual
# #<= menor igual
# #!= distinto de
# a=3
# if a>3:
#     print("si,a es mayor a 3")
#     print("chau")
# else:
#     print("no, a no es mayor a 3")
#         #pregunta2
# if a==3:
#     print("a es igual")

# nota=60
# if nota >= 60:
#     print("pasate!!!!!!")
# else:
#     print("hule")
# #ej: crear una funcion que reciba como parametro una nota e imprima si pasaste o te aplasaste

# def puntaje(nota, nombre):  #def solo lleva la variable y el parametro
	
# 	if nota>60:
# 		print("pasaste", nombre)
# 	else:
# 		print("no pasaste", nombre)

# puntaje(50, "laura") # solo en el momento de la llamada se le asigna valor
# puntaje(60, "luis")
# puntaje(67.5, "Marcos")
# puntaje(55.4,"luz")
# # and es para agregar ptra condicion
# a=11
# if a>5 and a<10 and a !=7:
# 	print("a es mayor a 5 y menor que 10 y distinto que 7") 
# else:
# 	print("a no cumple el rango a 5 y menor que 10 y distinto que 7")
# # or se usa cuando cumple alguna de las condiciones pero es independiente osea que puede o no cumplirse las otras condiciones
# if a> 5 or a<10:
# 	print("a es mayor que 5 o menor que 10")
# else:
# 	print("a no es mayor que 5 ni menor que 10")
# # verdadedro y falso solo se utiliza el prin con las condicionantes
# #elif es equivalente al no pero si
# edad=7
# if edad>18:
# 	print("universidad")
# elif edad >14:
# 	print("secundaria")
# elif edad<6:
# 	print("primaria")
# else:
# 	print("bbdlc")
# #crear una funcion puntaje que reciba como parametro una nota
# #del 1 al 100 e imprima que nota sacaste
# #nota> 60   <1
# #nota entre 60 y 70 <2
# #nota entre 71 y 75  <3
# #nota 76 y 85  <4
# #nota mayor que 85  <5
# nota=0
# def nivel(puntaje1):
# 	if puntaje1 <=60 and puntaje1 >=1:
# 		return (" sacaste 1")
# 	elif puntaje1 >=60 and puntaje1 <=70:
# 		return ("sacaste 2")
# 	elif puntaje1 >=71 and puntaje1 <=75:
# 		return ("sacaste 3")
# 	elif puntaje1 >= 76 and puntaje1 <85:
# 		return("sacaste 4")
# 	elif puntaje1 >= 85:
# 		return ("sacaste 5 felicitaciones!!!")
# 	else:
# 		return ("ausente")
# nivel(nota)
# nivel(67)
# nivel(83)
# nivel(73)
# nivel(86)
# #input te permite ingresar valores despues por teclado
# #nombre = input("ingresa tu nombre:")
# #print("hola", nombre)
# #ej pedir al usuario que ingrese tres numeros y multiplicarlo
# #entre si, imprimir

# #nombre1 = int(input("ingrese el primer numero:"))
# #nombre2= int(input("ingrese el segundo numero:"))
# #nombre3 =int(input("ingrese el tercero numero:"))
# #print("resultado es",nombre1*nombre2* nombre3)
# #ej2

# #nombre = int (input("un numero del 1 al 100:"))
# #print(nivel(nombre))

# ##########bucle while########################
# # ejecuta mientras se cumple una funcion 
# # x=0
# # while x != 5:
# # 	print("hola esto es un bucle")
# # 	x = int(input("ingresa algo"))
# # print ("fin")

# ######contador##########3
# #repite 
# contador=0
# while contador<10:
# 	print("estoy en un blucle mental")
# 	contador=contador + 1
# 	print("se repitio",contador,"veces")

# contador = 10
# while contador >0:
# 	print("estoy en un bucle")
# 	contador = contador -1
# 	print("te quedan", contador,"veces")
# # usando while pedir al usuario al usuario 5 ingredientes para hacer una pizza y agregar a una lista al final y al final imprimir
# listadeingredientes= []
# ingrediente = 1
# while ingrediente <= 5:
# 	ingrediente= ingrediente +1
# 	listadeingredientes.append(input("ingresa un ingrediente de la pizza:"))
# print(listadeingredientes)

# ej- crear un juego de advinanza donde el numero a adivinar de pistas en cada ingreso
from random import randint # es una funcion que ya esta
numero_secreto = randint(0,10)

adivino = False
while adivino == False:
	apuesta =input("adivina el numero secreto: ") 
	if int(apuesta) == numero_secreto:
		print("ganaste")
		adivino =True
	elif int(apuesta) >numero_secreto: 
		print("es un numero menor","segui participando")
	elif int(apuesta) <numero_secreto:
		print("elige un numero mayor","segui participando")

print(randint(1,26))


	