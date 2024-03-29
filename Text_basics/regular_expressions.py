# Vamos a trabajar con algunas expresiones regulares que nos permitiran iterar sobre el texto buscando patrones. 

# Cada caracter que escribes es una parte del patrón, de modo que debemos saber que significa cada uno de los caracteres que usamos:


# text = "The phone number of the agent is 408_555-1234. Call soon!"

# Podemos mirar por ejemplo si algo está incluido en un string mas grande

# "408" in text:

# Esto nos devolverá un True

# Vamos a empezar entonces a usar la libreria de expresiones regulares que viene en python para buscar patrones, para ello la importamos

import re
# text = "my phone is a new phone"

# pattern = "phone"

# re.search(pattern,text)

# Para usar esta libreria escribimos el patrón que estamos buscando y después el texto en el que queremos buscar, usando el metodo search de esta manera
# podremos hallar todas las coincidencias de nuestro patrón en el texto. 

# my_match = re.search(pattern,text)

# print(my_match.span())

# Con e metodo span() obtenemos la posición de nuestros matches dentro del string. Este metodo es mas facil de utilizar si almacenamos las coincidencias
# en otra variable, tal y como hemos hecho aqui en my_match. Existen otros comandos que se pueden ver y usar.

# my_match.start()
# my_match.end()

# Ptincipio y final del match o cuántos match hay en tu string usando el metodo findall():


# all_matches = re.findall(pattern,text)
# print(len(all_matches))

# Si quisiéramos ver la posición de todos los matches en un texto podríamos usar un iterable y el metodo finditer:

# for match in re.finditer(pattern,text):
#     print(match.span())

# Vamos a ver ahora como crear patrones mas complejos, para ello debemos usar la tabla que clasifica los caracteres y los codifica para python. 

# Character     Description    Example Pattern Code       Exammple Match

# \d             A digit        file_\d\d                  file_25

# \w             Alphanumeric     \w-\w\w\w<               A-b_1

# \s<            White space      a\sb\sc                   a b c

# \D             A non digit      \D\D\D                   ABC

# \W             Non-alphanumeric  \W\W\W\W\W               *-+=)

# \S            Non-whitespace\    S\S\S\S               Yoyo


# Tabla para establecer repeticiones o basados en frecuencia

# Character     Description              Example Pattern Code       Exammple Match

# +             Occurs one or more        version \w-\w+          version A-b1_1           

# {3}           Occurs exactly 3          \D{3}                   abc

# {2,4}         Occurs 2 to 4 times       \d{2,4}                 123

# {3,}          Occurs 3 or more          \w{3,}                 anycharacters

# *             Occurs zero or more       A*B*C*                 AAACC

# ?             Occurs Once or none       plurals?               plural


text = "My telephone number is 542-555-1234"

# Imaginemos que tenemos este texto y estamos buscando un número de teléfono, no específicamente este, sino uno cualquiera:

pattern = r'\d{3}-\d{3}-\d{4}'
# Creando esta expresion regular (con la r'' delante para saber que se trata de una expresion regular) podremos encontrar este patron en el texto,
# Recuerda que si buscamos varios matches usaremos findall()

phone_number = re.search(pattern, text)

print(phone_number.group())
# Con el metodo group() salimos del binario y así podemos ver los matches encontrados