#Aquí vamos a hablar de las redes de palabras
#Es uno de los más grandes capacidades que vienen con nltk. Coges palabras y miras sus relaciones de antonimia, sinonimia, etc. Para
# averiguar el contexto de aparición.  En este caso vamos a ver sinónimos (syns)

from nltk.corpus import wordnet
syns = wordnet.synsets("program")

#synset
# print(syns[0].name())


# (Aquí estamos imprimiendo toda una serie de sinónimos para diferentes contextos de la palabra program, esto puede resultar útil
#  ya que las relaciones de una palabra con otras palabras pueden ayudarnos a crear texto o algunas otras partes que resultan importantes.
# Los sinónimos se importan como una listaasií que podemos referirnos a ellos con los métodos de una lista)
#  print(syns)


#just the word
print(syns[0].lemmas()[0].name()) #Aquí podemos obtener de las lista syns que es programa en el corpus el primer elemento de su
# lista de lemmas en format string gracias al comando .name()

#definition
print(syns[0].definition())

#Ejemplos. También podemos imprimir ejemplos de la palabra en contexto
print(syns[0].examples())



#Vamos a crear ahora una lista de antónimos y sinónimos para la palabra
synonims = []
antonyms = []

for syn in wordnet.synsets("good"):#En el corpus wordnet good recorriendo con syn
    for l in syn.lemmas():#y recorriendo con l dentro de los lemmas de las palabras que recorre syn
        # print("l:",l)#Esto a a imprimir todos losposibles lemmas
        synonims.append(l.name())#adjunta a la lista de sinónimos el nombre de los lemas
        if l.antonyms():#Si l llega a un antónimo
            antonyms.append(l.antonyms()[0].name())#Adjunta a la lista antónimos el nombre del lemma

# print(set(synonims))
# print(set(antonyms))



#Ahora que hemos visto cómo funcionan los lemmas y cómo extraerlos vamos a ver la similitud, específicamente la similitud semántica
#Empecemos con dos palabras:

w1 = wordnet.synset("ship.n.01")#Elegimos ship, que es un nombre (n) y elegimos la primera
w2 = wordnet.synset("boat.n.01")
#Ahora vamos a comparar la similitud entre estas dos palabras semánticamente

print(w1.wup_similarity(w2))# El método .wup_similarity() hace que se compare la similitud semántica del objeto (w1 en este caso), con su argumento(w2).
#El output de esto es un número porcentual que dice lo similares que son estas palabras

w1 = wordnet.synset("ship.n.01")
w2 = wordnet.synset("car.n.01")
print(w1.wup_similarity(w2))

w1 = wordnet.synset("ship.n.01")
w2 = wordnet.synset("cat.n.01")
print(w1.wup_similarity(w2))

# Como vemos los outputs de esto dan un número cada vez más pequeño porque las palabras son cada vez mas diferentes semánticamente.
# Esto puede utilizarse para leer exámenes o trabajos por ejemplo y saber si la gente ha copiado cambiando por sinónimos.


