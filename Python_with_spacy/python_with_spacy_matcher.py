import spacy
from spacy.matcher import Matcher


# Es importante señalar que el Matcher no funciona igual que el ents. 
# El entity ruler se usa cuando se le puede asignar una etiqueta. 
# El matcher es útil para extraer una especie de estructura repetitiva en el texto

nlp = spacy.load("en_core_web_sm")

matcher = Matcher(nlp.vocab)

# El matcher necesita el vocabulario presente en nuestro set de datos asi que ese será el 
# argumento que se envie a la instanciación. De momento añadiremos solo esto.
# Vamos a intentar rescatar direcciones de email de un texto

pattern = [{"LIKE_EMAIL": True}]
matcher.add("EMAIL_ADDRESS", [pattern])
# Es importante señalar que el parametro 2 es siempre una lsita de listas por lo que tal y como
# está ahora la sintaxis el segundo argumento debe ir entre []

doc = nlp("This is an email address: pepegonz@gmail.com")
# Para rescatar pasamos doc como un argumetno
matches = matcher(doc)
print(matches)

# El resultado es siempre una lista con tuplas de 3 elementos

# [(16571425990740197027, 6, 7)]

# El rpimer numero es el lexema seguido del token de inicio y el token final
# Vamos a imprimir ese lexema, cogemos la posicion de nuestro matcher y le damos un .text
print(nlp.vocab[matches[0][0]].text)

# Takata EMAIL_ADDRESS aquí tenemos el resultado, la label que asignamos antes para nuestro patron
# El matcher tiene muchísimos parametros que se pueden introducir para acotar sus extracciones
# y hacerlas más precisas https://spacy.io/api/matcher

# Vamos a hacer una tarea más real. Extraer todos los nombres propios de un texto. Será
# la entrada de Wikipedia de Martin Luther King

nlp_2 = spacy.load("en_core_web_sm")
matcher_2 = Matcher(nlp_2.vocab)
pattern_2 = [{"POS":"PROPN"}]
matcher_2.add("PROPER_NOUN", [pattern_2])

with open("wiki_mlk.txt", "r") as f:
    doc = f.read()

doc_ready = nlp_2(doc)
matches = matcher_2(doc_ready)

print(f"hemos encontrado {len(matches)} matches")

# Vamos a imprimir solo los 10 primeros. Recordemos que el matches es una lsita de tuplas
# el primer elemento es el lema y los otros dos los tokens de inicio y fin
for match in matches[:10]:
    print(match, doc_ready[match[1]:match[2]])

# hemos encontrado 65 matches
# (451313080118390996, 0, 1) Martin
# (451313080118390996, 1, 2) Luther
# (451313080118390996, 2, 3) King
# (451313080118390996, 3, 4) Jr.
# (451313080118390996, 6, 7) Michael
# (451313080118390996, 7, 8) King
# (451313080118390996, 8, 9) Jr.
# (451313080118390996, 10, 11) January
# (451313080118390996, 16, 17) April
# (451313080118390996, 23, 24) American

# El problema que tenemos aquí es que los nombres salen separados, pero y si pusiéramos un nuevo parametro

nlp_3 = spacy.load("en_core_web_sm")
matcher_3 = Matcher(nlp_3.vocab)
pattern_3 = [{"POS":"PROPN", "OP":"+"}]
matcher_3.add("PROPER_NOUN", [pattern_3])

with open("wiki_mlk.txt", "r") as f:
    doc = f.read()

doc_ready = nlp_3(doc)
matches = matcher_3(doc_ready)

print(f"hemos encontrado {len(matches)} matches")

# Vamos a imprimir solo los 10 primeros. Recordemos que el matches es una lsita de tuplas
# el primer elemento es el lema y los otros dos los tokens de inicio y fin
for match in matches[:10]:
    print(match, doc_ready[match[1]:match[2]])

# Ou mamma hemos encontrado 112 matches
# (451313080118390996, 0, 1) Martin
# (451313080118390996, 0, 2) Martin Luther
# (451313080118390996, 1, 2) Luther
# (451313080118390996, 0, 3) Martin Luther King
# (451313080118390996, 1, 3) Luther King
# (451313080118390996, 2, 3) King
# (451313080118390996, 0, 4) Martin Luther King Jr.
# (451313080118390996, 1, 4) Luther King Jr.
# (451313080118390996, 2, 4) King Jr.
# (451313080118390996, 3, 4) Jr.

# Pero seguimos teniendo problemas porque se superpoenen unos a otros. Intentemos arreglarlo
# Con un nuevo parametro en el matcher que se aplicará a todas las extracciones. 

nlp_4 = spacy.load("en_core_web_sm")
matcher_4 = Matcher(nlp_4.vocab)
pattern_4 = [{"POS":"PROPN", "OP":"+"}]
matcher_4.add("PROPER_NOUN", [pattern_4], greedy="LONGEST")

with open("wiki_mlk.txt", "r") as f:
    doc = f.read()

doc_ready = nlp_4(doc)
matches = matcher_4(doc_ready)

print(f"hemos encontrado {len(matches)} matches")

# Vamos a imprimir solo los 10 primeros. Recordemos que el matches es una lsita de tuplas
# el primer elemento es el lema y los otros dos los tokens de inicio y fin
for match in matches[:10]:
    print(match, doc_ready[match[1]:match[2]])

# Ahora sí tenemos estos resultados. Pero no están colocados, veamos como hacerlo.
# hemos encontrado 37 matches
# (451313080118390996, 68, 73) Martin Luther King Sr.
# (451313080118390996, 0, 4) Martin Luther King Jr.
# (451313080118390996, 165, 169) Southern Christian Leadership Conference
# (451313080118390996, 332, 336) Director J. Edgar Hoover
# (451313080118390996, 6, 9) Michael King Jr.
# (451313080118390996, 252, 255) Civil Rights Act
# (451313080118390996, 258, 261) Voting Rights Act
# (451313080118390996, 266, 269) Fair Housing Act
# (451313080118390996, 23, 25) American Baptist
# (451313080118390996, 85, 87) United States


nlp_5 = spacy.load("en_core_web_sm")
matcher_5 = Matcher(nlp_4.vocab)
pattern_5 = [{"POS":"PROPN", "OP":"+"}]
matcher_5.add("PROPER_NOUN", [pattern_5], greedy="LONGEST")

with open("wiki_mlk.txt", "r") as f:
    doc = f.read()

doc_ready = nlp_5(doc)
matches = matcher_5(doc_ready)
matches.sort(key = lambda x: x[1])
# Aquí lambda nos ayuda a iterar sobre las tuplas

print(f"hemos encontrado {len(matches)} matches")

# Vamos a imprimir solo los 10 primeros. Recordemos que el matches es una lsita de tuplas
# el primer elemento es el lema y los otros dos los tokens de inicio y fin
for match in matches[:10]:
    print(match, doc_ready[match[1]:match[2]])

# hemos encontrado 37 matches
# (451313080118390996, 0, 4) Martin Luther King Jr.
# (451313080118390996, 6, 9) Michael King Jr.
# (451313080118390996, 10, 11) January
# (451313080118390996, 16, 17) April
# (451313080118390996, 23, 25) American Baptist
# (451313080118390996, 41, 42) rights
# (451313080118390996, 68, 73) Martin Luther King Sr.
# (451313080118390996, 74, 75) King
# (451313080118390996, 85, 87) United States
# (451313080118390996, 104, 106) Mahatma Gandhi

# Ahora tiene mejor pinta pero imaginemos que queremos sacar solo los PROPN que vengan después de un verbo
# Debemos entonces mejorar nuestro pattern

nlp_6 = spacy.load("en_core_web_sm")
matcher_6 = Matcher(nlp_6.vocab)
pattern_6 = [{"POS":"PROPN", "OP":"+"},{"POS":"VERB"}]
matcher_6.add("PROPER_NOUN", [pattern_6], greedy="LONGEST")

with open("wiki_mlk.txt", "r") as f:
    doc = f.read()

doc_ready = nlp_6(doc)
matches = matcher_6(doc_ready)
matches.sort(key = lambda x: x[1])
# Aquí lambda nos ayuda a iterar sobre las tuplas

print(f"hemos encontrado {len(matches)} matches")

# Vamos a imprimir solo los 10 primeros. Recordemos que el matches es una lsita de tuplas
# el primer elemento es el lema y los otros dos los tokens de inicio y fin
for match in matches[:10]:
    print(match, doc_ready[match[1]:match[2]])

# hemos encontrado 3 matches
# (451313080118390996, 74, 76) King advanced
# (451313080118390996, 126, 128) King participated
# (451313080118390996, 332, 337) Director J. Edgar Hoover considered

# Al añadir a nuestro patrón una nueva ocurrencia basada en caracterñistias lingüísticas podemos
# extraer asunciones tremendamente elaboradas y complejas lingüísticamente.

# Ejercicio propio extraer los años en e texto

nlp_7 = spacy.load("en_core_web_sm")
matcher_7 = Matcher(nlp_7.vocab)
pattern_7 = [{"IS_DIGIT":True, "LENGTH":{">=":4}}]
matcher_7.add("YEAR", [pattern_7])

with open("wiki_mlk.txt", "r") as f:
    doc = f.read()

doc_ready = nlp_7(doc)
matches = matcher_7(doc_ready)
matches.sort(key = lambda x: x[1])
# Aquí lambda nos ayuda a iterar sobre las tuplas

print(f"hemos encontrado {len(matches)} matches")

# Vamos a imprimir solo los 10 primeros. Recordemos que el matches es una lsita de tuplas
# el primer elemento es el lema y los otros dos los tokens de inicio y fin
for match in matches[:10]:
    print(match, doc_ready[match[1]:match[2]])


# hemos encontrado 12 matches
# (5999387239696442499, 13, 14) 1929
# (5999387239696442499, 19, 20) 1968
# (5999387239696442499, 44, 45) 1955
# (5999387239696442499, 49, 50) 1968
# (5999387239696442499, 152, 153) 1955
# (5999387239696442499, 199, 200) 1963
# (5999387239696442499, 215, 216) 1963
# (5999387239696442499, 256, 257) 1964
# (5999387239696442499, 262, 263) 1965
# (5999387239696442499, 270, 271) 1968