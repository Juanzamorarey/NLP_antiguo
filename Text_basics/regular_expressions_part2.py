# Vamos a continuar con las expresiones regulares.


# Las expresiones regulares también pueden coger grupos y trabajar con ellos como si fueran una lista, por ejemplo:

import re


text = "My telephone number is 542-555-1234"

pattern = r'(\d{3})-(\d{3})-(\d{4})'

# Al introducir los parentesis haces que se separen los diferentes grupos a los cuales puedes llamar despues con el metodo group()

phone_number = re.search(pattern, text)

print(phone_number.group(1))
# Aquí llamo al grupo 1, si llamamos al 0 llamará a todo el grupo. 



# Podemos usar el | para establecer patrones de búsqueda que funcionan como un or

a = re.search(r"man|woman","This man was here")
print(a)

# La expresion regular de arriba buscará todas las palabras que sean man or woman. Otra cosa que podemos hacer es usar el .
# Este . hará que todo lo que termine con lo que indiquemos despues del punto aparecerá en nuestro patron, por ejemplo:

b= re.findall(r'.at',"The cat sat in the hat while I was doing the math")

print(b)

# Fijémonos es que en math únicamente busca hasta el final de nuestra expresión regular omitiendo la h final. Si pones más de un punto
# La expresión regular abarcará el mimso número de caracteres previos que de puntos se hayan escrito. 


# Vamos a ver ahora cómo se buscan cosas que empiezan o terminan de una manera determinada.Para ello usamos los siguientes caracteres:

# $ -> ends with...

# ^ -> starts with...

c = re.findall(r'\d$','This ends with a number 2')

print(c)

d = re.findall(r'^\d','1 is the lonliest number')

print(d)

# Estos comandos solo funcionan con numeros. 

# Podemos usar las expresiones regulares también para deshacernos de partes que no queremos de un string, por ejemplo imaginemos que queremos borrar todos
# los numeros del siguiente string:

ejemplo = "there are 3 numbers 34 inside 5 this sentence"

e = re.findall(r'[^\d]+',ejemplo)
print(e)

# Los [] en una expresion regular implican exclusión, por lo que nuestro patrón aquí está diciendo que se excluyan todos los dígitos. Si después ponemos 
# el símbolo + al final de la expresión hará una lista de strings separados por aquello que hemos excluido, esto es muy util para eliminar la 
# puntuación en un texto, algo muy común en NLP. 

ejemplo_2 = "This is a string! but it has punctuation. How to remove it?"

f = re.findall(r'[^!.? ]+',ejemplo_2)
print(f)

# Esto devuelve una lista de todo lo que no es puntuacion, se puede usar también para separar cada palabra. Si Quiero unirlo únicamente uso los
# métodos típicos de una lista:

print(' '.join(f))


# Vamos a ver por último los usos del + para unir las palabras:

ejemplo_3 = "Only fin he hyphen-words. Were are the long-ish dash words?"

g = re.findall(r'[\w]+-[\w]+',ejemplo_3)
print(g)

# Al usar esta expresion regular estamos haciendo que se cojan cualquier número de alfanuméricos con un guión y seguidos de cualquier numero de 
# caracteres alfanuméricos. Esto da como resultado lo que andamos buscando, las palabras con guiones.