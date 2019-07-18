### stackoverflow = solucionador de problemas
# OMDb api # para peliculas contrsenha: 

import requests
key = "4e9fcd9d"
url= "http://www.omdbapi.com/?apikey="
titulo = "fast & furius"
busqueda = url + key+ "&t=" + titulo

resultado = requests.get(busqueda)
dicc= resultado.json()  # guardamos en una variable para usar despues
print(dicc )
print(" el director es: ", dicc["Director"])

def p (titpel):
    busqueda = url + key+ "&t=" + titulo
    resultado = requests.get(busqueda)
    dicc= resultado.json()
    return dicc["Director"]
print(p("MOANA"))


 ######################## pip install gjango ########################