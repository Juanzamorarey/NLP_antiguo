#En la siguiente parte vamos a mejorar el algoritmo para ver cómo funciona la clasificación de las palabras que hemos preprocesado en text cassification

import nltk 
import random
from nltk.corpus import movie_reviews #Aquí vamos a usar un corpus con 200 reviews de películas (100 positivas/100negativas)

documents = [(list(movie_reviews.words(fileid)),category)#esto va a ser una lista de tuplas, las cuales serán palabras que clasificaremos
            for category in movie_reviews.categories()#Esto clasifica en positivo o negativo
            for fileid in movie_reviews.fileids(category)]#Esto identifica la categoría

random.shuffle(documents)#Este modulo nos ayuda a crear aleatoriedad en los datos. Shuffle significa barajar
# print(documents[1])esto imprime a primera review del corpus

all_words = []
for w in movie_reviews.words():
    all_words.append(w.lower())#lo pasamos a minúsculas para evitar problemas

all_words = nltk.FreqDist(all_words)#Aquí convertimos la lista all_words en una lista de frecuencia distributiva de nltk

# AQUÍ empieza la nueva lección
# Primero necesitamo algún tipo de limite para la cantidad de palabras que tenemos. 
word_features = list(all_words.keys())[:3000]#Aquí veremos que palabras son más comunes en negativo y cuáles en las positivas

def find_features (document):
    words = set(document)#Esto es una sola iteración pero sobre todas las palabras. 
    features = {}
    for w in word_features:
        features[w] = (w in words)

    return features
# (Lo que esta función está haciendo es tomar un documento, establecerlo con set, luego un diccionario que aun no sabemos para qué es
# y hacer que se recorra la lista word_features de modo que si la palabra está entre las 3000 más usadas dará true, y sino dará false)

print((find_features(movie_reviews.words('neg/cv000_29416.txt'))))#Aquí operamos nuestra función sobre el documento neg/cv... 

featuresets = [(find_features(rev),category) for (rev,category) in documents]
# (Toda esta línea de código hace lo siguiente. featuresets equivale a la función find_features trabajando sobre las reviews
# que dentro del corpora están llamadas como 'rev', o sea que rev es review, 1 de las 1000 del corpus. Después hace que el código
# referente a category que ya habíamos puesto en documents. De este modo lo que hace esto es convertir las reviews no solo a palabras
# , sino a palabras con el true/false que hemos trabajado con la función find_features. De esta manera podremos emepezar a trabajar
# con esta variable comparándola con otros datos para saber el impacto de si as palabras que se mencionan son positivas o negativas
# en nuestro clasificador de reviews.)

