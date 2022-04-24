import pandas as pd
from scipy.sparse.construct import random 

npr = pd.read_csv("npr.csv")

a = npr.head()

# print(a)

# a_1 = npr['Article'][4000]
# # Ya que la tabla que hemos usado solo tiene una columna llamada article podemos verla como si fuera una lista.

# print(a_1)
# print(len(npr))#Numero de articulos

# Antes de llevar a cabo el LDA tenemos que hacer un peuqeño preprocesamiento. 
from sklearn.feature_extraction.text import CountVectorizer

cv = CountVectorizer(max_df=0.95,min_df=2,stop_words="english")

# Este objeto usa 3 parametros:
    # max_df = ignora ciertas palabras que tienen una alta frecuencia de aparición.
            #  Si pasamos por ejemplo 0.9 significa que
            # nuestro objeto va a ignorar aquellas palabras que aparezcan en el 90% de los docuemntos.
    # min_df = establece una frecuencia mínima de aparición de una palabra. Si ponemos un entero 
    #       tomará en cuenta el número de documentos, en caso de poner un flotante será un porcentaje. Es muy útil
    #       para eliminar los errore de trasncripción por ejemplo.
    # stop_words = toma como parámetro un idioma y elimina las stop words de dicho idioma.  #

# En este caso no tenemos que hacer el train split porque se trata de aprendizaje no supervisado, no tenemos
# etiquetas en las ue poder basarnos por lo que el grupo de control no es necesario. 

dtm = cv.fit_transform(npr['Article'])
# Vamos a aplicar el fit_transform únicamente a la columna del article. 

# print(dtm)
# dtm es la documentum term matrix, es decir, la matriz que contiene la relación entre palabras y documentos. 
# Ahora que tenemos esta matriz que, recordemos, ha asignado las palabras a temas aleatorios por lo que es inútil de 
# momento de cara a clasificar, vamos a realizar el LDA. 

from sklearn.decomposition import LatentDirichletAllocation

LDA = LatentDirichletAllocation(n_components=7,random_state=42)
# Este objeto tiene una multitud enrome de parámetros que pueden utilizarse. Nosotros vamos a usar
    # n_components -> para asignar el número de temas en los que queremos clasificar los documentos.
    #  random_state -> para valernos de la aleatoriedad. 

# Ahora que tenemos el modelo vamos a alimentarlo con nuestra matriz
LDA.fit(dtm)

# Esto va a llevar mucho tiempo puesto que se trata de una gran cantidad de docuemntos y tiene que ir
# uno a uno. 
# una vez terminado esto nos quedan 3 pasos:
    # Coger el vocabulario de las palabras

cv.get_feature_names()
# El len de esto es 54777, lo que quiere decir que hay 54777 palabras en el docuemtno. Esto se toma como una lista
print(cv.get_feature_names()[50000])
# Si quisiéramos elegir palabras randome dentro de las palabras que están en nuestro vocabulario:
import random
random_word_id = random.randint(0,54777)
# Escoge una palabra entre las poasiciones de la lista 0 y 54777
cv.get_feature_names()[random_word_id]

    # Coger los temas

# Los temas los podemos coger directamente del modelo entrenado:
len(LDA.components_)
# Aquí veremos que el output es 7 puesto que habíamos elegido 7 temas diferentes
# Del mismo modo si vemos el tipo de dato
type(LDA.components_)
# Se trata de un ndarray, una macrotupla que contiene las palabras y la probabilidad de cada una en cada topic.
# Podmos cmbinar esto con el vocabulario para ver las palabras más probables en cada tema, lo que es el último paso.

single_topic = LDA.components_[0]
print(single_topic) #impirmimos para ver qué sale
single_topic.argsort() 
#argsort() devuelve los índices de una lista ordenados por el valor que tienen los elementos de dicha lista,
# en orden de menor a mayor así:
                    # lista = [10, 200, 1]
                    # neng = lista.argsort()
                    # print(neng) -> [2,0,1]
# devuelve el valor mas bajo 1 que está en la posición 2, luego 10 en la posicion 0 y 200 en la posicion 1.
# Entonces podemos usar argsort para ver, dentro de un topic, cuáles son las palabras con mayor número de apariciones,
# para este topic en particular:

top_10_palabras = single_topic.argsort()[-10:]
# Aquí vamos a ver las 10 palabras más usadas en este topic en concreto, el del index 0 de la lista.
for indice in top_10_palabras:
    print(cv.get_feature_names()[indice])
# new
# percent
# government
# company
# million
# care
# people
# health
# said
# says
 
#     # Coger las palabras con mayor probabilidad para cada tema
for i, topic in enumerate(LDA.components_):
    print(f"THE TOP 15 WORDS FOR TOPIC #{i}")
    print([cv.get_feature_names()[i] for i in topic.argsort()[-15:]])
    print('\n')
    print('\n')


# THE TOP 15 WORDS FOR TOPIC #0
# ['companies', 'money', 'year', 'federal', '000', 'new', 'percent', 'government', 'company', 'million', 'care', 'people', 'health', 'said', 'says']




# THE TOP 15 WORDS FOR TOPIC #1
# ['military', 'house', 'security', 'russia', 'government', 'npr', 'reports', 'says', 'news', 'people', 'told', 'police', 'president', 'trump', 'said']




# THE TOP 15 WORDS FOR TOPIC #2
# ['way', 'world', 'family', 'home', 'day', 'time', 'water', 'city', 'new', 'years', 'food', 'just', 'people', 'like', 'says']




# THE TOP 15 WORDS FOR TOPIC #3
# ['time', 'new', 'don', 'years', 'medical', 'disease', 'patients', 'just', 'children', 'study', 'like', 'women', 'health', 'people', 'says']




# THE TOP 15 WORDS FOR TOPIC #4
# ['voters', 'vote', 'election', 'party', 'new', 'obama', 'court', 'republican', 'campaign', 'people', 'state', 'president', 'clinton', 'said', 'trump']




# THE TOP 15 WORDS FOR TOPIC #5
# ['years', 'going', 've', 'life', 'don', 'new', 'way', 'music', 'really', 'time', 'know', 'think', 'people', 'just', 'like']




# THE TOP 15 WORDS FOR TOPIC #6
# ['student', 'years', 'data', 'science', 'university', 'people', 'time', 'schools', 'just', 'education', 'new', 'like', 'students', 'school', 'says']

# Ahora que tenemos las 15 palabras más representativas de cada tema podríamos intuir mas o menos cuál es el tema. 
# lo último que tenemos que hacer es unir el número de los topics al npr.head() original que contiene los articulos. 
# De esta manera vamos a crear una nueva columna en la que constará el tema al que pertenece el artículo.
# Recordemos que en la asignación del tema debe ser el usuario quien lo lleve a cabo. 

# Para llevarlo a cabo usamos nuestro spare matrix original y nuestro dataframe con los articulos.
# Vamos entonces a crear una lista a partir de la matriz dtm. 

topic_results = LDA.transform(dtm)

# El resultado de esto será una serie de datos en los que podremos ver la relacion del documento con cada uno de los
# topics. Para visualizarlo es bueno redondear el resultado, de este modo:

print(topic_results[0].round(2))
# esto nos muesta el siguiente output:
# ([0.02,0.68,0.,0.,0.3,0.,0.])
# Como podemos ver por los resultados este documento en particular tiene una probabilidad más alta de pertenecer al topic
# numero 1

# Debido a que únicamente nos interesa este dato vamos a ver entonces de qué manera podemos asignarlo
topic_results[0].argmax()

b = npr['Topic'] = topic_results.argmax(axis=1)
# Creamos una nueva columna Topic que contiene el número del topic al que pertenece el tema
# NOTA -> argmax(axis=1) indica que 1 es el número más alto que puede haber puesto que recordemos que se trata de porcentajes

print(b)

# Continuar en leccion 61