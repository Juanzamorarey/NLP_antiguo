# Vamos a trabajar ahora con spacy definiendo patrones a partir de los conocimientos anteriores y haciendo matchings en grandes textos

import spacy

nlp = spacy.load('en_core_web_sm')

# En la documentacion del curso vamos a ver algunas tablas que van a hacer realmente fácil el uso de estas expresiones regulares.
# Dentro del curso se ncuentra en la parte 5 
# Spacy tiene una herramienta entera de matches llamada .matcher() que nos ahorra escribir las expresiones regulares. Primero hay que importarlo

# from spacy.matcher import Matcher

# matcher = Matcher(nlp.vocab)

# Es necesario pasarle al matcher el nlp.vocab
# Se pueden añadir múltiples patrones al mismo matcher.
# Dentro de spacy existen sus propias expresiones regulares cuya sintaxis viene determinada por una lista de diccionarios en la que introduciremos un key
# que incluye el valor determinado y un valor que incluye lo que buscamos para esa key, por ejemplo:

# Queremos encontrar la palabra solarpower de las siguientes maneras:
# SolarPower
# Solar-power
# Solar Power
# Para estas palabras deberíamos establecer los siguientes patrones de búsqueda:

# pattern1 = [{'LOWER':'solarpower'}]

# Este patrón busca solarpower en minúsculas (se ignoran las iniciales) SolarPower

# pattern2 = [{'LOWER':'solar'},{'IS_PUNCT':True},{'LOWER':'power'}]

# Este patrón busca la palabra solar seguida de un signo de puntuación (en este caso buscamos el guión), seguida de power en minúscula Solar-power

# pattern3 = [{'LOWER':'solar'},{'LOWER':'power'}]

# Este patrón busca las dos palabras separadas. Solar Power

# Estos patrones son muy simples, pero si añadimos loa attributes (en la documentación), podemos ver que la cantidad de parámetros que se pueden introducir
# para llevar a cabo búsquedas es muy amplia lo que radica en búsquedas realmetne específicas. 
# 
# ## Other token attributes
# Besides lemmas, there are a variety of token attributes we can use to determine matching rules:
# <table><tr><th>Attribute</th><th>Description</th></tr>

# <tr ><td><span >`ORTH`</span></td><td>The exact verbatim text of a token</td></tr>
# <tr ><td><span >`LOWER`</span></td><td>The lowercase form of the token text</td></tr>
# <tr ><td><span >`LENGTH`</span></td><td>The length of the token text</td></tr>
# <tr ><td><span >`IS_ALPHA`, `IS_ASCII`, `IS_DIGIT`</span></td><td>Token text consists of alphanumeric characters, ASCII characters, digits</td></tr>
# <tr ><td><span >`IS_LOWER`, `IS_UPPER`, `IS_TITLE`</span></td><td>Token text is in lowercase, uppercase, titlecase</td></tr>
# <tr ><td><span >`IS_PUNCT`, `IS_SPACE`, `IS_STOP`</span></td><td>Token is punctuation, whitespace, stop word</td></tr>
# <tr ><td><span >`LIKE_NUM`, `LIKE_URL`, `LIKE_EMAIL`</span></td><td>Token text resembles a number, URL, email</td></tr>
# <tr ><td><span >`POS`, `TAG`, `DEP`, `LEMMA`, `SHAPE`</span></td><td>The token's simple and extended part-of-speech tag, dependency label, lemma, shape</td></tr>
# <tr ><td><span >`ENT_TYPE`</span></td><td>The token's entity label</td></tr>

# </table> 

# Ahora que tenemos nuestros tres patrones es el momento de unirlos a nuestro matcher:

# matcher.add('SolarPower',None,pattern1,pattern2,pattern3)

# El None corresponde al callback, del cual hablaremos mas tarde. El string es el nombre del matcher concreto que contiene estos patrones. 

# doc = nlp(u"The Solar Power industry continuous to grow as solarpower increases. Solar-power is amazing!")

# found_matches = matcher(doc)
# print(found_matches)
# El objeto found_matches que almacena los matches en nuestro doc devuelve una serie de tuplas que tienen 3 informaciones. Lo primero es el 
# string id, los otros dos numeros son el principio y el final en el span. Este contador se refiere a tokens. Para representarlo de una manera 
# mas visual podemos usar este bucle for:

# for match_id, start, end in found_matches:
#     string_id = nlp.vocab.strings[match_id]  # get string representation
#     span = doc[start:end]                    # get the matched span
#     print(match_id, string_id, start, end, span.text)

# En este bucle for tenemos la misma información que arriba pero incluyendo también el match concreto impreso y el nombre del objeto matcher, en este caso
# SolarPower. 

# Si queremos eliminar una serie de patrones de nuestro matcher solo tenemos que indicarlo de la siguiente manera:
# matcher.remove('SolarPower')
# Ahora hemos borrado todos los patterns de SolarPower

# pattern1 = [{'LOWER':'solarpower'}]
# pattern2 = [{'LOWER':'solar'},{'IS_PUNCT':True,'OP':'*'},{'LOWER':'power'}]

# El paramtero 'OP' va a permitir incluir más opcines, a continuación una lista:

# The following quantifiers can be passed to the `'OP'` key:
# <table><tr><th>OP</th><th>Description</th></tr>

# <tr ><td><span >\!</span></td><td>Negate the pattern, by requiring it to match exactly 0 times</td></tr>
# <tr ><td><span >?</span></td><td>Make the pattern optional, by allowing it to match 0 or 1 times</td></tr>
# <tr ><td><span >\+</span></td><td>Require the pattern to match 1 or more times</td></tr>
# <tr ><td><span >\*</span></td><td>Allow the pattern to match zero or more times</td></tr>
# </table>

# Con todo esto vamos a añadir entonces los nuevos patrones a nuestro matcher:

# matcher.add('SolarPower',None,pattern1,pattern2)

# doc2 = nlp(u"Solar--power is solarpower yay!")

# found_matches = matcher(doc2)

# print(found_matches)

# Como podemos ver ahora, gracias al parámetro 'OP' hemos encontrado el match con dos - que hay en doc2, que antes no se habría encontrado. 


# PARTE 2 -> Phrase matching

from spacy.matcher import PhraseMatcher

matcher_phrase = PhraseMatcher(nlp.vocab)

# Para este artículo vamos a usar un artículo de wikipedia que está descargado, primero lo abrimos en el directorio correcto

with open('../NLP/UPDATED_NLP_COURSE/TextFiles/reaganomics.txt') as f:
    doc3 = nlp(f.read())

# Ahora imaginemos que queremos encontrar una serie de terminos de los cuales nos suena el nombre pero no los sabemos exactamente:

phrase_list = ['voodoo economics','supply-side economics','trickle-down economics','free-market economics']

# El siguiente paso será dividir el texto de modo que cada frase sea un doc text:
# Creamos una variable que almacena una lista en la cual usamos nlp para procesar el texto en phrase_list. Por cada phrase dentro de phrase list
# creamos entonces diferentes elementos de la lista.

phrase_patterns = [nlp(text) for text in phrase_list]

# Ahora añadimos al matcher cada una de las frases en la lista. Para ello igual que con el matcher de palabras, ponemos un nombre al matcher, un None,
# y por último podemos ir pasando cada uno de los elementos de la lista phrase_patterns de arriba pero, como en este caso queremos todas, pasamos 
# con un * toda la lista para el matcher. 

matcher_phrase.add('EconMatcher',None,*phrase_patterns)

found_matches = matcher_phrase(doc3)
# En esta variable están almacenados todos los matches en forma de tuplas, recordemos que venían tres datos, el primero la clave y el segundo y tercero
# la posición. Vamos a utilizar el mismo bucle for que usamos antes para ver los matches de una forma más visual. 

for match_id, start, end in found_matches:
    string_id = nlp.vocab.strings[match_id]  # get string representation
    span = doc3[start:end]                   # get the matched span
    print(match_id, string_id, start, end, span.text)

# Si quisiéramos ver el contexto de nuestro match podríamos, en este bucle for, añadir a la 3a línea algo al end y restar al start para ver qué
# contexto rodea a nuestros matches. 
# span = doc3[start-5:end+5]