import nltk 
import random
from nltk.corpus import movie_reviews #Aquí vamos a usar un corpus con 200 reviews de películas (100 positivas/100negativas)

documents = [(list(movie_reviews.words(fileid)),category)#esto va a ser una lista de tuplas, las cuales serán palabras que clasificaremos
            for category in movie_reviews.categories()#Esto clasifica en positivo o negativo
            for fileid in movie_reviews.fileids(category)]#Esto identifica la categoría

random.shuffle(documents)

all_words = []

for w in movie_reviews.words():
    all_words.append(w.lower())#lo pasamos a minúsculas para evitar problemas
# (En esta parte vamos a terminar de crear un algoritmo clasificador en positivo o negativo)

all_words = nltk.FreqDist(all_words)

word_features = list(all_words.keys())[:3000]

def find_features (document):
    words = set(document)#Esto es una sola iteración pero sobre todas las palabras. 
    features = {}
    for w in word_features:
        features[w] = (w in words)

    return features
# (Lo que esta función está haciendo es tomar un documento, establecerlo con set, luego un diccionario que aun no sabemos para qué es
# y hacer que se recorra la lista word_features de modo que si la palabra está entre las 3000 más usadas dará true, y sino dará false)

# print((find_features(movie_reviews.words('neg/cv000_29416.txt'))))
featuresets = [(find_features(rev),category) for (rev,category) in documents]

# Cuando llevemos aquí el trabajo que queremos vamos a tener dos cosas diferentes: la primera va a ser un set de entrenamiento y la 
# segunda un set de prueba:
training_set = featuresets[:1900] #Con este set le indicamos a la máquina toda una serie de palabras y su frecuencia a aparecer más en
# reviews positivas o negativas.
testing_set = featuresets[1900:]#De este set pedimos a la máquina que nos diga ella misma las categorías para comprobar los aciertos.
#El número 1900 es arbitrario, pero supone una muestra suficiente.


# posterior = prior occurences x liklihood / evidence
# En la línea superior está el algoritmo para ver la base de paabras, se llama naive based algorithm. Este algoritmo nos dirá
# la posibilidad de que una palabra sea positiva o negativa.

# Ahora vamos a construir un clasificador 

classifier = nltk.NaiveBayesClassifier.train(training_set) #este metodo es el algoritmo que hemos visto antes y toma como argumento el 
# training set
print("Naive Bayes Algo accuracy percent:", (nltk.classify.accuracy(classifier,testing_set))*100)
# (Este print nos dará el cálculo basado en el algoritmo, se utilizan varios métodos interesantes. el método classify y de ahí el 
# método accuracy toma dos argumentos que son el resultado del algoritmo anterior, en nuestro caso classifier, y el set de 
# datos de prueba. Luego multiplicamos por cien para tener un porcentaje.)
classifier.show_most_informative_features(15)
# (El output de esto va a ser un porcentaje de acierto.Este porcentaje puede cambiar dependiendo de las muestras que haya tomado el algoritmo
# de nuestra muestra.
# En las palabras vemos también que aparece algo como lo siguietne:)
# frances = True              pos : neg    =      9.1 : 1.0
#            unimaginative = True              neg : pos    =      8.3 : 1.0
#                  idiotic = True              neg : pos    =      7.4 : 1.0
#               schumacher = True              neg : pos    =      7.0 : 1.0

# (Esto significa que la palabra aparece (true), y que aparece 9.1 veces más frecuentemente en una review positiva que en una negativa.)