import numpy as np
import pandas as pd

df = pd.read_csv("TextFiles/moviereviews2.tsv", sep='\t') #Lo abro con Pandas

# print(df.head)

# print(df.isnull().sum()) #Comrprueba que no hay valores nulos

df.dropna(inplace=True) #Elimino los valores nulos

# print(df.isnull().sum()) #Compruebo de nuevo

# blanks = []

# for i,lb,rv in df.itertuples():
#     if rv.isspace():
#         blanks.append(i)
#Elimino los valores si el feature es un espacio en blanco

from sklearn.model_selection import train_test_split

X = df['review'] #El featura es la columna reviews
y = df['label'] #Las labels son la columna de labels

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3, random_state=42) #Dividimos en grupode control
#y grupo de entrenamiento

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
#Importamos el pipeline, el extractor de características textuales con su vectorizador y el clasificador LinearSVC

clasificador_texto = Pipeline([('tfidf',TfidfVectorizer()), ('clf', LinearSVC())])
#Creamos el modelo clasificador

clasificador_texto.fit(X_train,y_train)

predicciones = clasificador_texto.predict(X_test)

from sklearn.metrics import confusion_matrix, classification_report, accuracy_score

print(confusion_matrix(y_test,predicciones))

print(classification_report(y_test,predicciones))

print(accuracy_score(y_test,predicciones))




