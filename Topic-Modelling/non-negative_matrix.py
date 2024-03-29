# Non-negative matrix factorization es un algoritmo no supervisado que hace simultáneamente una reducción dimensional 
# y una agrupación. En conjunto con TF-IDF nos puede servir para llevar a cabo topic modelling de una manera eficiente
# mejorando los resultados. 

# La idea es crear otra matriz aparte de la que ya creamos con TF-IDF y, a partir de este vector y la comparación
# con el primero poder alcanzar puntos comunes que reduzcan las posibilidades del modelling
# Siendo así esto tiene 5 pasos:
# 
#   -Construir un vector espacial para los documentos (tras eliminar stopwords) que resulta en una matriz A
#   -Aplicar TF-IDF para normalizar A
#   -Normalizar TF-IDF con una unidad de medida
#   -Inicializar factores usando NNDSVD (non-negative double single singular descomposition) en A
#   -Aplicar el gradiente proyectado NMF (non-negative gradient factorization) a A
# 
# ¿Qué obtendremos tras realizar esto?
# Primero obtendremos los vectores base los cuales agruparán los temas dentro de los datos y, al mismo tiempo, el coeficiente
# de la matriz, es decir, el peso de cada palabra dentro de su agrupación para asignarla a uno u otro tema.
# Quedarán por tanto dos matrices una que relaciona las palabras con los temas y otra que relaciona los documentos
# con los temas.
# 
# Al igual que en TF-IDF tenemos que elegir el número de posibles temas de antemano y, al mismo tiempo, tendremos que
# elegir a partir de las 10 palabras cuál es el tema al que atañe. #


import pandas as pd

npr = pd.read_csv("npr.csv")

#Pretratamos el texto con TF-IDF vectorization
from sklearn.feature_extraction.text import TfidfVectorizer

tfidf = TfidfVectorizer(max_df=0.95,min_df=2,stop_words="english")
dtm = tfidf.fit_transform(npr['Article'])

# Ahora empezamor, con el Tf-IDF ya hecho con los parametros que vimos la vez anterior, la parte de análisis a partir de 
# factorización de la matriz no negativa. 

from sklearn.decomposition import NMF 
nmf_model = NMF(n_components=7, random_state=42)
#El objeto NMF tiene multitud de parametros que pueden cambiarse, al igual que la vez anterior vamos a elegir 7 topics
#y establecer el random_state en 42

a = nmf_model.fit(dtm)
print(a)
# Entrenamos el modelo y ya está realizado. Debido a su funcionamiento va a ser mucho más rápido que TF-IDF
# tfidf.get_feature_names()[2300]
# Podríamos llevar a cabo lo mismo que con el modelo anterior para ver las palabras del modelo pero en este caso
# vamos aomitirlo.

# Vamos a ver, entonces las 15 palabras más habituales por topic.
for index,topic in enumerate(nmf_model.components_):
    print(f"THE TOP 15 WORDS FOR TOPIC # {index}")
    print([tfidf.get_feature_names()[i] for i in topic.argsort()[-15:]])
    # Esta lista de comprension nos devolverá las 15 primeras palabras de la lista. Recordemos que la lista 
    # muestra primero las palabras menos frecuentes y termina con las más frecuentes. 
    print("\n")


# THE TOP 15 WORDS FOR TOPIC # 0
# ['new', 'research', 'like', 'patients', 'health', 'disease', 'percent', 'women', 'virus', 'study', 'water', 'food', 'people', 'zika', 'says']


# THE TOP 15 WORDS FOR TOPIC # 1
# ['gop', 'pence', 'presidential', 'russia', 'administration', 'election', 'republican', 'obama', 'white', 'house', 'donald', 'campaign', 'said', 'president', 'trump']


# THE TOP 15 WORDS FOR TOPIC # 2
# ['senate', 'house', 'people', 'act', 'law', 'tax', 'plan', 'republicans', 'affordable', 'obamacare', 'coverage', 'medicaid', 'insurance', 'care', 'health']


# THE TOP 15 WORDS FOR TOPIC # 3
# ['officers', 'syria', 'security', 'department', 'law', 'isis', 'russia', 'government', 'state', 'attack', 'president', 'reports', 'court', 'said', 'police']


# THE TOP 15 WORDS FOR TOPIC # 4
# ['primary', 'cruz', 'election', 'democrats', 'percent', 'party', 'delegates', 'vote', 'state', 'democratic', 'hillary', 'campaign', 'voters', 'sanders', 'clinton']


# THE TOP 15 WORDS FOR TOPIC # 5
# ['love', 've', 'don', 'album', 'way', 'time', 'song', 'life', 'really', 'know', 'people', 'think', 'just', 'music', 'like']


# THE TOP 15 WORDS FOR TOPIC # 6
# ['teacher', 'state', 'high', 'says', 'parents', 'devos', 'children', 'college', 'kids', 'teachers', 'student', 'education', 'schools', 'school', 'students']

# Visto el proceso y llevado a cabo queda a discreeción del usuario interpretar a qué tema corresponden
# estas palabras. Normalmente sabremos a qué tema pertenecen si ya conocemos de antemano el agrupamiento general 
# de los datos con los que estamos trabajando.

# Ahora vamos a unir el topic a cada uno de los articulos del corpus, exactamente igual que hicimos en el modelo anterior.

topic_results = nmf_model.transform(dtm)
# Establecemos el modelo en el dataframe
topic_results.argmax(axis=1)
#  Establecemos 1 como el número mas alto puesto que se trata de porcentajes

npr['Topic'] = topic_results.argmax(axis=1)
# Creamos la nueva columna

# para asignar el número de los topics podríamos crear un diccionario y usar la funcion map aquí lo asignamos libremente
mis_temas = {0:"curiosidades",1:"política",2:"regueton",3:"cine",4:"corazon",5:"internacional",6:"deportes"}
npr["Topic label"] = npr['Topic'].map(mis_temas)
print(npr.head())
# E imprimimos la cabecera siendo este el output:

# 0      In the Washington of 2016, even when the polic...      1      política
# 1        Donald Trump has used Twitter  —   his prefe...      1      política
# 2        Donald Trump is unabashedly praising Russian...      1      política
# 3      Updated at 2:50 p. m. ET, Russian President Vl...      3          cine
# 4      From photography, illustration and video, to d...      6      deportes
# ...                                                  ...    ...           ...
# 11987  The number of law enforcement officers shot an...      3          cine
# 11988    Trump is busy these days with victory tours,...      1      política
# 11989  It’s always interesting for the Goats and Soda...      0  curiosidades
# 11990  The election of Donald Trump was a surprise to...      4       corazon
# 11991  Voters in the English city of Sunderland did s...      3          cine
