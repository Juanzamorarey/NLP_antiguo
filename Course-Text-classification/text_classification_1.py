# La mayoría de algoritmos de machine learning no acpetan texto crudo, por ello debemos limpiar antes este texto
# para ello utilizamos una técnica denominada vectorización, que convierte el texto en vectores. 
# Para llevar a cabo este proceso utilizaremos también la libreria de SKlearn en este caso
# aplicada al texto. Creando un vectorizador lo vamos a pasar a nuestro texto y obtendremos
# todas las palabras que aparecen una vez en el texto. Es decir en el mensaje:

# "llama a tu hermana" el vectorizador va a coger cada palabra una vez sin repetirla y va a establecer un contador
# para cada caracterñística de la palabra. El documento que contiene el conteo de estas palabras únicas se
# denomina DTM (document term matrix). 

# Una alternativa al countvectorization es el TfidfVectorizer, lo que hace esto es:
#   TF (term frequency) -> la cantidad de veces que una palabra aparece en un elemento del corpus
#       Requiere limpiar las stopwords

# Matemáticamente expresado sería asÍ:
#  TF-IDF = term_frquency*(1/document_frequency)
# TF -IDF = term_frequency * inverse document frequency

# Al tener la cantidad de veces que aparece la palabra en el mensaje (y por tanto en el corpus) y el negativo
# de su frecuencia TF-IDF nos permite entender el contexto de cada palabra dentro del corpus en vez de solo en un documento.

# Vamos a ver cómo hacer esto con python y scikit learn

# Lo rpimero que necesitamos saber es que cualquier herramienta de NLP requiere de un vocabulario

# vocab = {} # aquí almacenamos el vocabulario

# i = 1 #Esto será para contar dentro del diccionario

# with open("1.txt") as f:
#     x = f.read().lower().split()
# #Abrimos el archivo de texto y lo dividimkos

# for word in x:
#     if word in vocab:
#         continue
#     else:
#         vocab[word] = i
#         i+=1
# # Si la palabra está en nuestro vocabulario  pasamos (recordamos solo 1 vez por palabra) si no lo está la añadimos
# # y le asignamos un índice

# # print(vocab)

# with open("2.txt") as f:
#     x = f.read().lower().split()

# for word in x:
#     if word in vocab:
#         continue
#     else:
#         vocab[word] = i
#         i+=1

# # Hacemos lo mismo con el segundo archivo pero en el mismo diccionario. Siendo así tendremos todas las palabras
# # en ambos textos con un id único.

# # Vamos a realizar feature extraction en nuestro vocabulario:

# # Primero creamos un vector vacío que tenga espacio para todo nuestro vocabulario:
# one = ['1.txt']+[0]*len(vocab)
# # print(one)

# # Ahora vamos a mapear la frecuencia de cada parabra de 1.txt en nuestro vector:
# with open('1.txt') as f:
#     x = f.read().lower().split()
# for word in x:
#     one[vocab[word]]+=1
# print(one)

# # Aquí vemos que  el 1.txt se lee de nuevo y para cada palabra vemos el número de veces que aparece en una lista.


# two = ['2.txt']+[0]*len(vocab)
# # print(two)

# with open('2.txt') as f:
#     x = f.read().lower().split()
# for word in x:
#     two[vocab[word]]+=1
# print(two)

# Al ver las dos listas podemos comparar que, de todo el vocabulario que tenemos, en el texto 1 aparecen las palabras
# un numero x de veces y en el texto dos esas mismas palabras aparecen 0 o más veces:
# ['1.txt', 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]
# ['2.txt', 1, 3, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1]

# Ahora que hemos explicado cómo funciona vamos a ver cómo realizar todas las operaciones de NLP (tokenization,
# tag_extraction...) sobre el corpus de mensaje que teníamos antes.

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv("TextFiles/smsspamcollection.tsv", sep='\t')
# print(df.isnull().sum()) Comprobamos que no haya nada vacío
# print(df['label'].value_counts())  Vemos las cifras totales del corpus

X = df['message'] #X va a ser solo el texto
y = df['label'] # y es la etiqueta

X_train, X_test, y_train, y_test =  train_test_split(X,y, test_size=0.33,random_state=42)
# Seguimos el mismo proceso que con scikitlearn de antes. Estamos creando nuestras 4 variables para realizar la 
# confusion matrix

from sklearn.feature_extraction.text import CountVectorizer #importamos el vectorizador

# y creamos un objeto con el vectorizador:
count_vect = CountVectorizer()

# Ahora que tenemos el objeto tenemos que pasarle nuestro corpus para que lo vectorice y podamos operar con él

# Primero entrenamos el vectorizador con los datos (construir un vocabulario, contar el número de palabras...)
# count_vect.fit(X_train)
# X_train_counts = count_vect.transform(X_train)

# Esta es una manera de hacerlo, la otra sería utilizar directamente un metodo que une las dos anteriores:

X_train_counts = count_vect.fit_transform(X_train)

# Ahora hemos vectorizado el texto y ya lo podemos utilizar para entrenar el modelo

# print(X_train_counts.shape)
# Aquí vemos todos los mensajes y el conteo de palabras únicas, es decir nuestro vocabulario

# Ahora nos interesa transformar el conteo a frecuencias usando el TF-IDF para eliminar el peso de las palabras
# que son mas frecuentes como las stopwords.

from sklearn.feature_extraction.text import TfidfTransformer, TfidfVectorizer

tfidf_transformer = TfidfTransformer()

X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
# Creamos y transformarmos el vector que ya teniamos para añadirle precision

# print(X_train_tfidf.shape)
# Aunque sean las mismas cifras ya no solo está contando sino que ahora estamos tomando el término frecuencia y lo
# estamos multiplicando por su frecuencia inversa.

# Como estos dos procesos se suelen realizar juntos sklearn tiene un metodo para usar simultáneamente 
# Countvectorization y Tfidf, sería de la sigueinte manera:

# from sklearn.feature_extraction.text import TfidfVectorizer
# vectorizer = TfidfVectorizer()
# X_train_tfidf = vectorizer.fit_transform(X_train)

# Vamos a entrenar el clasificador como lo hicimos antes:

from sklearn.svm import LinearSVC
# importamos un modelo
clf = LinearSVC()
# Creamos la instanciación u objeto de este modelo

clf.fit(X_train_tfidf,y_train)
# Lo entrenamos

# Para ahorrar todo este proceso y el de clasificación podemos usar un pipeline:

from sklearn.pipeline import Pipeline

text_clf = Pipeline([('tfidf', TfidfVectorizer()),('clf',LinearSVC())])
# El pipeline takes una lista de tuplas, con nombre y metodo

# Esta es la manera más habitual de hacer el proceso de forma profesional en una sola línea de código
# de tal modo que no tengamos que escribir todo lo de arriba. Es importante matizar que aquí la línea es corta
# puesto que solo estamos haciendo la vectorización y la clasificación, pero las pipelines suelen ser mucho más
# largas normalmente ya que conllecan varios procesos.

text_clf.fit(X_train, y_train)
# Ahora text_clf sería el modelo que puede predecir nuevos datos, vamos a probarlos con el test_set

predictions = text_clf.predict(X_test)
# Aquí ya tendré el modelo trabajando en el test, merece la pena ver que  estamos pasando el texto
# crudo, sin vectorizar lo que hace el proceso con las pipelines mucho más cómodo
# 
# 

from sklearn.metrics import confusion_matrix, classification_report
# Importamos para medir

print(confusion_matrix(y_test, predictions)) 
# Aquí veremos la matriz de confusión, la cual está obteniendo unos resultados mucho mejores
print(classification_report(y_test, predictions))
# Aquí vemos el informe de clasificación

# El modelo está funcionando mucho mejor que el que hicimos previamente teniendo solo en cuenta la longitud y 
# del texto. Al utilizar el texto hemnos podido analizar mucho más en detalle los mensajes para crear
# un modelo funcional.