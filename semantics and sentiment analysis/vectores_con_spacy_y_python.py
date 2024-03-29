import spacy 
nlp = spacy.load('en_core_web_md')
# Aquí cargamos la librería md


# print(nlp(u'lion').vector)

# Ahora somos capaces de ver los vectores que componen cada una de las palabras. Veamos por ejemplo
# la palabra lion

# Nota: La u delante del string implica un strong unicode

# Debemos tener en cuenta que no solamente puede hacerse esto con palabras si no que también puede hacerse con frases

# Si quisiéramos ver la cantidad de dimensiones contempladas en el vector podríamos hacerlo con el comando shape

# print(nlp(u'fox').vector.shape)

# Ahora que hemos comprendido el sistema de vectores vamos a intentar analizar vectores similares:

tokens = nlp(u'lion cat pet')

# for token1 in tokens:
#     for token2 in tokens:
#         print(token1.text, token2.text, token1.similarity(token2))
#         # Aquí estamos diciendo que para el 1er token en tokens, y para el segundo token en tokens imprime
#         #el texto de ambos tokens y luego la similitud entre el token 1 y el 2 


# Aquí obtenemos el siguiente resultado:
# lion lion 1.0                          Aquí por supuesto es 1 porque una palabra es idéntica a la otra
# lion cat 0.5265438                        Cuanto mas similares son mayor será el número
# lion pet 0.39923766
# cat lion 0.5265438
# cat cat 1.0
# cat pet 0.7505457
# pet lion 0.39923766
# pet cat 0.7505457
# pet pet 1.0

# Es relevante señalar que si buscáramos las similitudes entre 3 palabras aparentemente contrarias pero que suelen
# aparecer en el mismo contexto encontraríamos cosas sorprendetes omo que love y hate tienen la misma similitud que
# like y love a pesar de ser aparentemente contrarias. Esto es así porque aparecen en el mismo contexto. 

# para ver nuestro vocabulario podemos hacer lo siguiente:

print(len(nlp.vocab.vectors)) #Aquí veremos el número de palabras únicas que tenemos en nuestro vocabulario

print(nlp.vocab.vectors.shape) #Así vemos cuantas palabras tiene nuestro vocabulario y cuántas dimensiones

# A veces podemos encontrar palabras que están fuera del vocabulario como nombres extraños. Vamos a ver cómo es eso:

tokens = nlp(u"dog cat nargle")

# for token in tokens:
#     print(token.text, token.has_vector, token.vector_norm,token.is_oov)

    #Esto implica: primero el texto del token, despues si tiene o no vector (true si está en el vocab False si no
    # .vector_norm implica su normalización en el vector y por último una comprobación para ver si está fuera del 
    # vocabulario. En caso de que esté fuera devuelve True.)

# dog True 7.0336733 False
# cat True 6.6808186 False
# nargle False 0.0 True

# Algo incríeble es que podemos calcualr palabras a partir de sus vectores. Para hacer esto veremos lo siguiente:

from scipy import spatial

cosine_similarity = lambda vec1, vec2: 1- spatial.distance.cosine(vec1,vec2)
# Esta fórmula matemática nos permite calcular la distancia entre vectores, sumarlos o restarlos

king = nlp.vocab['king'].vector
man = nlp.vocab['man'].vector
woman = nlp.vocab['woman'].vector
# Cogemos los vectores de las palabras que queremos en diferentes variables. 
# El objetivo ahora es que realizando operaciones con estos vectores obtengamos un vector cuya similaridad a 
# queen sea muy próxima o lo más próxima posible. 

new_vector = king-man+woman

computed_similarities = []

for word in nlp.vocab: #para cada palabra de nuestro vocab
    if word.has_vector: #si tiene un vector
        if word.is_lower: #si está en minúsculas
            if word.is_alpha: #si es una letra y no un número
                similarity = cosine_similarity(new_vector, word.vector) #comparala con el nuevo vector
                computed_similarities.append((word,similarity)) #Añade a la lista la similitud entre la palabra y el
                                                                #nuevo vector
computed_similarities = sorted(computed_similarities, key=lambda item:-item[1])
# En la lista vamos a eliminar las palabras que tengan una similaridad baja
print([t[0].text for t in computed_similarities[:10]])
# Recordando que tenemos una lista de tuplas cogemos el texto del primer elemento de la tupla de los 10 primeros
# elementos de la lista, lo que serían los diez vectores mas similares a la suma que hicimos arriba, es decir,
# el vector mas similar a la resta de palabras que ocurrió arriba. 

# Con la libreria intermedia:
# ['king', 'woman', 'she', 'lion', 'who', 'when', 'dare', 'cat', 'was', 'not']






right = nlp.vocab['cloud'].vector
wrong = nlp.vocab['rain'].vector
regular = nlp.vocab['sun'].vector


new_vector = regular+right+wrong

computed_similarities_2 = []

for word in nlp.vocab: #para cada palabra de nuestro vocab
    if word.has_vector: #si tiene un vector
        if word.is_lower: #si está en minúsculas
            if word.is_alpha: #si es una letra y no un número
                similarity = cosine_similarity(new_vector, word.vector) #comparala con el nuevo vector
                computed_similarities_2.append((word,similarity)) #Añade a la lista la similitud entre la palabra y el
                                                                #nuevo vector
computed_similarities_2 = sorted(computed_similarities_2, key=lambda item:-item[1])
# En la lista vamos a eliminar las palabras que tengan una similaridad baja
print([t[0].text for t in computed_similarities_2[:10]])
