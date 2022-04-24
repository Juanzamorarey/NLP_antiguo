# En esta parte del curso vamos a ver la semántica y el sentiment analysis

# Para llevar a cabo la vectorización correcta debemos descargar de spacy los modelos medium o large ya que el pequeño
# no contiene las vectorizaciones.

# Los vectores de palabras se crean a partir de lo siguiente:
#Wrod2Vec es una red neuronal de dos capas que procesa textos, en su input introducimos corpus de textos y en su output
# es una serie de vectores para las palabras en dicho corpus. Word2vec sirve para una vez procesado ese texto
# detectar similaridades matemáticamente. Esto permite detectar las características de una palabra no solo por la palabra
# en sí si no también a partir de su contexto. 
# 
# Esto quiere decir que si nos valemos de Word2Vec y le ofrecemos suficientes cantidades de datos, estadísticamente
# el programa creará asociaciones del tipo man es a boy lo que woman es a girl.
# 
# De esta manera Word2Vec entrena sus palabras comparándolas con otras palabras que aparecen en su contexto, esto lo
# hace de dos maneras:
# 1. usando el contexto para rpedecir una palabra objetivo (continuous bag of words (CBOW)) o usando una palabra
# para predecir un contexto para ella lo que se denomina skip-gram.
# 
# Estas dos aproximaciones son opuestas. En la primera a partir de varias palabras extraemos una, mientras que en la segunda
# a partir de una palabra sacamos todas las demás.
# 
# 
# 
# Entendiendo que cada palabra es un vector que está en un espacio multidimensaional podemos medir la distancia que existe
# entre una palabra y otra, o inlcuso "restar" dos palabras para ver cual es el resultado. Así si a la palabra rey le
# restáramos hombre y le sumáramos mujer aparecería la palabra reina y viceversa. #
