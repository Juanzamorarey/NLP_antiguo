# Hemos visto ya clasificación de textos si están previamente etiquetados.
# 
# pero, ¿y si no tienen etiquetas?
# 
# Una solución es el VADER, un algoritmo integrado en la libreria NLTK que mide la polaridad (positividad/ negatividad)
# y la intensidad de la emoción. 
# 
# VADER se basa en un diccionario que mapea caracteristicas léxicas y intensidad de expresión en lo que se denomina
# sentiment scores. De este modo VADER realiza lo siguiente:
# 
# 1o- toma todas las palabras del texto y las etiqueta como positivas o negativas
# 
#   2o- Establece la intensidad para cada palabra
# 
# 3o- otorga el resultado final.
# 
# VADER toma además en consideración el contexto en el que se encuentra la palabra a la hora de realizar el análisis
# El problema es, de hecho, el sarcasmo, puesto que es lo que no detecta VADER. #

import nltk
# nltk.download('vader_lexicon') #Aquí bajamos el lexicon si hiciera falta

from nltk.sentiment.vader import SentimentIntensityAnalyzer #Este es nuestro modleo

sid = SentimentIntensityAnalyzer()

# Este objeto lo que hace es tomar un string y devolver un diccionario con 4 puntuaciones: negativo, neutral, positivo
# y por último una puntuación compuesta de los otros 3. 

# {'neg': 0.0, 'neu': 0.508, 'pos': 0.492, 'compound': 0.4404} El valor máximo para cada una de las puntuaciones es 1.0
# En caso de reviews negtivas se trataría de -1.0. 

a = "This was the best, most awesome movie EVER MADE!!!"
# {'neg': 0.0, 'neu': 0.425, 'pos': 0.575, 'compound': 0.8877}
b="This was the WORST movie that has ever disgraced the screen."
# {'neg': 0.465, 'neu': 0.535, 'pos': 0.0, 'compound': -0.8331}

# print(sid.polarity_scores(a)) De esta manera obtenemos la puntuación

import pandas as pd

df = pd.read_csv('TextFiles/amazonreviews.tsv', sep='\t')
# print(df.head())
# Aquí tenemos un csv con reviews sobre productos de amazon
df['label'].value_counts() #Para ver el numero de reviews

#Vamos entonces a limpiar los datos

# df.dropna(inplace=True)

# blanks = []

# for i,lb,rv in df.itertuples(): #indice, etiqueta y review
#     if type(rv) == str: #Si es un string
#         if rv.isspace(): #Si está en blanco (es decir no se pueda analizar)
#             blanks.append(i) #Añadimos su posición a uan lista para después eliminarla. 

# df.drop(blanks, inplace=True) #Si tuviera algo vacío lo borramos así. 

# print(blanks) vemos que no hay nada vacío

c = sid.polarity_scores(df.iloc[0]['review']) #De esta manera cogemos el primer elemento de la lista de reviews.
# print(c)

#Como vemos se trata de una buena review. Ahora vamos a añadir el análisis de VADER a la tabla que ya tenemos

df['scores'] = df['review'].apply(lambda review:sid.polarity_scores(review))
#De esta manera lo que vamos a hacer en df es añadir una nueva columna en la que se asigne el diccionario del análisis
#a cada una de las reviews para ver si la etiqueta se corresponde. 

# print(df.head()) #Como vemos aquí se ha añadido el score a cada una de las reviews.

# Vamos a crear ahora otra columna en la que podamos ver la puntuación compuesta:

df['compound'] = df['scores'].apply(lambda d:d['compound'])
# print(df.head())
#  Como vemos ahora tenemos todos los compound score en otra columna. Ahora vamos a comprobar si el compound score
#es mayor a 1, en cuyo caso será positivo, y si es menor entonces será negativo. De este modo podremos ver los falsos
#positivos y negativos que tenemos. 

#   label                                             review                                             scores  compound
# 0   pos  Stuning even for the non-gamer: This sound tra...  {'neg': 0.088, 'neu': 0.669, 'pos': 0.243, 'co...    0.9454
# 1   pos  The best soundtrack ever to anything.: I'm rea...  {'neg': 0.018, 'neu': 0.837, 'pos': 0.145, 'co...    0.8957
# 2   pos  Amazing!: This soundtrack is my favorite music...  {'neg': 0.04, 'neu': 0.692, 'pos': 0.268, 'com...    0.9858
# 3   pos  Excellent Soundtrack: I truly like this soundt...  {'neg': 0.09, 'neu': 0.615, 'pos': 0.295, 'com...    0.9814
# 4   pos  Remember, Pull Your Jaw Off The Floor After He...  {'neg': 0.0, 'neu': 0.746, 'pos': 0.254, 'comp...    0.9781

df['comp_score'] = df['compound'].apply(lambda score: 'pos' if score >= 0 else 'neg')
#Con esta lista de comprensión básicamente estamos creando una columna que, si todo ha funcionado bien 
# tendrá que ser idéntica a la de las etiqeutas, ya que estamos usando el modelo sid para analizar el texto directamente.
# NOTA: lambda funciona aquí como una i por lo que solamente hay que ponerlo pero no influye

# print(df.head())
#   label                                             review                                             scores  compound comp_score
# 0   pos  Stuning even for the non-gamer: This sound tra...  {'neg': 0.088, 'neu': 0.669, 'pos': 0.243, 'co...    0.9454        pos
# 1   pos  The best soundtrack ever to anything.: I'm rea...  {'neg': 0.018, 'neu': 0.837, 'pos': 0.145, 'co...    0.8957        pos
# 2   pos  Amazing!: This soundtrack is my favorite music...  {'neg': 0.04, 'neu': 0.692, 'pos': 0.268, 'com...    0.9858        pos
# 3   pos  Excellent Soundtrack: I truly like this soundt...  {'neg': 0.09, 'neu': 0.615, 'pos': 0.295, 'com...    0.9814        pos
# 4   pos  Remember, Pull Your Jaw Off The Floor After He...  {'neg': 0.0, 'neu': 0.746, 'pos': 0.254, 'comp...    0.9781        pos


# Vamos a comparar el comp_score al etiquetado manual, para ello usaremos sklearn:

from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

certitud = accuracy_score(df['label'],df['comp_score']) #Aquí medimos a que nivel coinciden en total las etiquetas asignadas
#por el VADER y las asignadas manualmente
print(certitud)

print(classification_report(df['label'],df['comp_score']))
#Aquí podremos ver la precision, el recall y el f1-score en total y podemos comprobar que VADEr tiene problemas para
#clasificar reviews positivas

# precision    recall  f1-score   support

#          neg       0.86      0.51      0.64      5097
#          pos       0.64      0.91      0.75      4903

#     accuracy                           0.71     10000
#    macro avg       0.75      0.71      0.70     10000
# weighted avg       0.75      0.71      0.70     10000

print(confusion_matrix(df['label'],df['comp_score']))
# Aquí vemos aquellas clasificadas correctamente como positivas o como negtivas

# [[2622 2475]
#  [ 434 4469]]

# Como podemos ver el modelo está analizando con una certitud del 71% lo que no es excelente pero tampoco malo