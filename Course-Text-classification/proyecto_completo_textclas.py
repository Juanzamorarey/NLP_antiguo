import numpy as np
import pandas as pd

df = pd.read_csv("TextFiles/moviereviews.tsv",sep='\t')

# print(df.head()) #Para ver las cabeceras

# print(df['review'][0]) #Para ver una de las reviews específica usaríamos la misma estructura que es un diccionario

# Primero, antes de hacer la matriz de confusión vamos a buscar valores vacíos que puedan estropear nuestro modelo

# print(df.isnull().sum()) Esto recordemos es para ver si hay valores nulos en etiquetas o features

# Como vemos aparece lo siguiente:
# label      0
# review    35
# dtype: int64
# Mientras que en las etiquetas no existe ningún valor nulo, en las reviews hay 35, lo que no indica que de las 2000
# reviews hay 35 que están vacías. Tenemos que borrarlas para que funcione, para ello:
df.dropna(inplace=True) # De esta manera dropeamos aquellas reviews que no posean un valor para label y feaure
# print(df.isnull().sum())

# Aunque este metodo parece eficaz, a veces las BBDD hacen constar el feature como un valor string vacío, poniendo,
# por ejemplo en el caso de estas películas, una review mala pero no explicando por qué. 

#para solucionarlo vamos a hacer lo siguiente:

blanks = [] #empezamos con una lista vacía

# for index de cada review, dentro de la review la etiqueta y dentro de la review el review o feature.
# Se itera sobre las reviews
# como si fueran una lista de tuplas.
for i,lb,rv in df.itertuples():
    if rv.isspace():         #Si es un espacio:
        blanks.append(i) #Añadimos a la lista vacía su posición

df.drop(blanks, inplace=True) #hacemos el mismo metodo para eliminar las posiciones que están en la lista dandoles
# el valor True para que el inplace con valor True las saque de nuestro repertorio de reviews.

# Desde aquí seguimos con el proceso habitual:
    # 1. dividir los datos en train_set y test_set

from sklearn.model_selection import train_test_split
X = df['review']
y = df['label']
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3,random_state=42) #importante el orden X_train,X_test...

    # 2. Crear un pipeline para vectorizar los datos

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC

text_clf = Pipeline([('tfidf', TfidfVectorizer()),('clf',LinearSVC())])

    #3. Dar los datos del training al pipeline

text_clf.fit(X_train,y_train)

    #4. utilizar el modelo para predecir

predictions = text_clf.predict(X_test)

from sklearn.metrics import confusion_matrix, classification_report, accuracy_score

    #5. Medir los resultados del proceso

print(confusion_matrix(y_test,predictions)) #Aquí vemos nuestra matriz de confusion
# [[235  47]
#  [ 41 259]]
print(classification_report(y_test,predictions))
#               precision    recall  f1-score   support

#          neg       0.85      0.83      0.84       282
#          pos       0.85      0.86      0.85       300

#     accuracy                           0.85       582
#    macro avg       0.85      0.85      0.85       582
# weighted avg       0.85      0.85      0.85       582

print(accuracy_score(y_test,predictions))
# 0.8487972508591065

# Estamos prediciendo con un 84% de certeza si las reviews son malas o benas
# Una app de esto podría ser hacer webscrapping y comrpobar las reviews que pone la gente.