# Vamos a ver algunas librerias pra trabajar con textos en python

# Vamos a empezar con el f_string literal, así como su alineamiento
person = "Juan"


print(f"my name is {person}")

# Con el f string delante del print puedes colocar directamente el nombre de las variables entre
# las llaves. 


# El f string también se puede usar para trabajar con diccionarios
# estableciendo las operaciones dentro de los {}
d = {'a':13,'b':456 }

print(f"my number is {d['a']}")

# Y con listas:

mylist = [0,1,2]


print(f"my number is {mylist[0]}")

# It's important to know how to change the format when you need it, as well as the 
# alignment. That's because normally spacy prints things in a non desirable way. To do so:

library = [('Author','Topic','Pages'),('Twain','Rafting',601),('Feynman','Physics',95)]

# Esto es una lista con tuplas que no se imprimen de la manera deseada, para ello usamos bucles for:
# Como ves el uso de f strings sirve para simplificar la sintaxis.

for book in library:
    print(f"El tema es: {book[1]}")

for author,topic,pages in library:
    print(f"{author} {topic} {pages}")

# El output de esto apesta asi que para corregirlo hacemos lo siguiente:
# Al poner los dos puntos y las llaves podemos introducir un número de espacios que se reconocen gracias al f string.

for author,topic,pages in library:
    print(f"{author:{10}} {topic:{10}} {pages:{10}}")

# Aún así el formato queda un poco feo por paages que se queda descuadrado, para arreglar esto podemos trabajar con f string:

for author,topic,pages in library:
    print(f"{author:{10}} {topic:{10}} {pages:.>{10}}")

# El símbolo mayor alinea a los diez espacios de modo que se corrige automáticamente. Si pusieramos cualquier caracter
# Antes del símbolo mayor se rellenaría con dicho caracter.

for author,topic,pages in library:
    print(f"{author:{10}} {topic:{10}} {pages:.>{10}}")

# Por último vamos a ver las capacidades de formateo. Con un objeto especializado como los que vienen en la librería datetime podemos crear un obejto día
# El cual también funciona conf-strings literals. Si quisiéramos formatear el aspecto que va a tener únicamente tendríamos que instroducir dos puntos y el tipo de formato
# deseado. En este caso se trata de un formato de una pagina especifica (strftime.org) que contiene los formatos deseados. 

from datetime import datetime
today = datetime(year=2020,month=2,day=28)
print(f"{today:%B %d, %Y}")
today
