# Vamos a crear aquí ya nuestro primer algoritmo para clasificar textos
# Los textos se clasifican por temas o en las categorías que tu quieras. Básicamente el análisis es binario: o spam o no spam
# o dentro del tema o fuera del mismo, todo depende del objetivo que busquemos pero la ramificación siempre será binaria.

# Esto puede ser como el sentiment analysis pero a un nivel más basico
import nltk 
import random
from nltk.corpus import movie_reviews #Aquí vamos a usar un corpus con 200 reviews de películas (100 positivas/100negativas)

documents = [(list(movie_reviews.words(fileid)),category)#esto va a ser una lista de tuplas, las cuales serán palabras que clasificaremos
            for category in movie_reviews.categories()#Esto clasifica en positivo o negativo
            for fileid in movie_reviews.fileids(category)]#Esto identifica la categoría

random.shuffle(documents)#Este modulo nos ayuda a crear aleatoriedad en los datos. Shuffle significa barajar
# print(documents[1])

all_words = []
for w in movie_reviews.words():
    all_words.append(w.lower())#lo pasamos a minúsculas para evitar problemas

all_words = nltk.FreqDist(all_words)#Aquí convertimos la lista all_words en una lista de frecuencia distributiva de nltk
# print(all_words.most_common(15))#De esta manera podemos ver, ya que es una lista de frecuencia distributiva, las 15 palabras mas comunes del texto
#Aquí hemos cogido una serie de palabras y hemos visto el número de veces que aparecen en el corpus total. Los signos ortográficos también se cuentan porque no los hemos quitado
print(all_words["stupid"])#Con esto veríamos cuántas veces aparece la palabra stupid en las reviews.

#En la siguiente parte vamos a mejorar el algoritmo para ver cómo funciona la clasificación de las palabras que hemos preprocesado aquí