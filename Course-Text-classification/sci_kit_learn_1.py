# Vamos a comenzar el scikit-learn

import numpy as numpy #
import pandas as pd # nos permite leer csv
#Panda lee objetos en los que se llaman frames

import matplotlib.pyplot as plt
#  #para visualizar

df = pd.read_csv('TextFiles/smsspamcollection.tsv', sep="\t")
#Aquí estamos creando un objeto que lea el csv separado por tabuladores, no por comas como sería el valor default

# print(df.head())

#Con esto veremos los primeros 5 elementos de nuestro set. Es útil para ver cuáles son los datos
#que hay, en este caso son el numero, la etiqueta, el mensaje, la longitud y la puntuación que indica cuanta 
# puntuación contiene el mensaje.


#Para analizar los sets necesitamos comprobar si tenemos todos los campos mencionados anteriormente en cada
#elemento del set, de lo contrario no será válido, para ello podemos hacer lo siguiente:

# print(df.isnull().sum())

# Esto comprueba si hay algún valor en el campo requerido y, si lo hay, indica 0. De este modo al sumar todo
# podremos ver, si existe un 1 en algún dato, o un número diferente a 0 que hay algún dato inexistente
#y el set no es válido.

#para ver la cantidad de mensajes

# print(len(df))

#Si quisiera ver las etiquetas o cualquier otro campo del csv print(df['label']), pero queremos ver solo las 
# posibilidades que existen dentro de label

# print(df['label'].unique())

#Si además quisiera ver el valor de cada uno de estos valores únicos:

# print(df['label'].value_counts())

# Este es el resultado :
# ham     4825
# spam     747
# Name: label, dtype: int64

# Podemos decir por tanto que se trata de una clase desequilibrada porque hay mucho más de un tipo que del otro.

# Para practicar vamos a crear un modelo que intente predecir si un mensaje es HAM o SPAM a partir de únicamente 
#la longitud y la puntuación. Vamos a pegar un trozo de código para visaulizarlo, no es importante.

# plt.xscale('log')
# bins = 1.15**(np.arange(0,50))
# plt.hist(df[df['label']=='ham']['length'],bins=bins,alpha=0.8)
# plt.hist(df[df['label']=='spam']['length'],bins=bins,alpha=0.8)
# plt.legend(('ham','spam'))
# plt.show()

#No tira, no existe np

# Vamos a centrarnos ahora en ver la sintaxis de scikit learn para crear un modelo simple:

from sklearn.model_selection import train_test_split #Esto nos ayudara a coger el train test set

#X is our feature
X = df[['length','punct']] #Son dos brackets porque es una lsita de columnas

#Y is our label
Y = df['label'] #Solo es una columna asi que no hace falta dobles brackets

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3,random_state=42)

#Necesitamos cuatro variables para esta función ya que recordemos que el modelo requiere 4 variables (true_positive, false_negative....)
#Para no obtener un resultado muy sesgado el parametro random_state se utilizará para seleccionar de forma aleatoria varias veces el mismo data_set

# print(X_train.shape) #para el entrenamiento

#Esto nos mostrará el número de filas primero y de columnas después para cada uno de los sets. O sea
#el data set de features para el entrenamiento es de 3900 lineas y dos columnas (length and punct)

# print(X_test.shape) #para el test

#Si queremos ver el set entero solo lo imprimimos y obtendremos también su index en el total print(Y_test)
#El index en el total no aparece en orden porque lo hemos seleccionado de forma random pero lo podremos usar 
#para hacer los matches que sean necesarios.

# Ahora tenemos que elegir un modelo al cual vamos a entrenar. El modelo será mejor o pero dependiendo del 
# objetivo, pero la manera de usar el modelo es siempre muy similar.

from sklearn.linear_model import LogisticRegression

lr_model = LogisticRegression(solver ='liblinear') #aquí podemos ver los parametros. Estos podrían cambiarse pero es la parte matemática
#de la cuestión y no vamos a entrar en ello. Todo dependerá de nuevo de nuestro objetivo, set de datos...
# Vamos a cambiar el parametro solver solo por probar, pero recuerda que dependeria de lo que quieras hacer.
# En la página hay consejos sobre qué parametros puedes cambiar para ajustarlo a tu volumen de datos.

#Una vez creado el modelo hay que alimentarlo (feed)

lr_model.fit(X_train,Y_train) #Aquí utilizamos solo aquella porción que corresponde al entrenamiento.
#No hace falta ajustarlo a una variable

#Aquí tenemos por lo tanto el modelo listo para predecir. A continuación vamos a usarlo

from sklearn import metrics #Con esto podremos evaluar nuestro modelo

predictions = lr_model.predict(X_test)#Ahora le pasamos el conjunto de datos relacionados con el test.
#Merece la pena recalcar que, para comparar nuestro modelo, ya sabemos las respuestas. Las predicciones sobre
#X_test serán aquellas que están en el set Y dedicado a testear, puesto que esta son los labels y nuestro modelo
#predice los labels en base a los features que hay en el set. Vamos a ver cómo ha funcionado nuestro modelo.

#predictiones contiene el resultado de nuestro modelo, ahora debemos medirlo, para ello usamos la libreria
#metrics y, a partir de ella podemos elaborar una matriz de confusión en la que evaluamos el test "y" de pruebas
#junto con las predicciones. Por tanto:

print(metrics.confusion_matrix(Y_test, predictions))
#el resultado es: 
# [[1405   43]
#  [ 219    5]]
# Visto de manera mas clara:
df = pd.DataFrame(metrics.confusion_matrix(Y_test,predictions), index=['ham','spam'], columns=['ham','spam'])
print(df)
# ¿Cómo interpretamos esta matriz de confusión? la manera es la siguiente: 
# el dato de 1405 son los ham que realmente eran ham, los 43 son los ham que en realidad eran spam, los 219
# son los spam que realmente eran ham y los 5 eran los spam que realmente son spam 

#Para ver matriz de confusion:
# https://www.google.com/search?q=matriz+de+confusi%C3%B3n&client=firefox-b-d&source=lnms&tbm=isch&sa=X&ved=2ahUKEwi9wLW7gu_vAhUCYsAKHTmNAFYQ_AUoAXoECAIQAw&biw=1920&bih=910#imgrc=TghuvJDThR80eM

# Además de la matriz de confusión podemos ver también el reporte de clasificación, para ello:

print(metrics.classification_report(Y_test, predictions))
#esto imprimirá todos los datos que nos interesaban: precision, recall, f1-score y support

#Para imprimir el accuracy total (recordemos las formulas del machine learning) podemos hacer lo siguiente:
print(metrics.accuracy_score(Y_test,predictions))

# Si nuestro modelo no funciona podríamos probar otros modelos para ver su deployment, por ejemplo:
# from sklearn.naive_bayes import MultinomialNB

# nb_model = MultinomialNB()

# nb_model.fit(X_train,Y_train)

# predictiones = nb_model.predict(X_test)

# print(metrics.confusion_matrix(Y_test, predictions))

# Hemos hecho lo mismo pero con otro modelo, pero como vemos la sintaxis es la misma. 

# Ahora que hemos aprendido como usar los modelos entrenarlos y evaluarlos, vamos a ver la aprte mas importante
# Extraer información de los features de nuestros datos. A partir de la extracción de estos features vamos a
# poder crear modelos mejores