#En esta parte vamos a trabajar el stemming. El stemming sirve para tomar las raíces de las palabras en para realizar el análisis de dato que te resulte conveniente
#(Se trata de una parte del preprocesamiento de datos para la obtención de resultados mediante el NLP
# Entonces el stemming sirve para sacar los lexemas de las palabras.)

#La razón por la que se hace es por las diferentes variaciones de palabras pueden simplificarse para ser enteniddas en el ordenador

# I was taking a car ride in the car
# I was riding a car
#En estas dos frases ride significa lo mismo, pero aparece de dos formas diferentes. Para resolver esto acudimos a lo siguiente:
from nltk.stem import PorterStemmer

#Existen diferentes Stemmers

from nltk.tokenize import word_tokenize

ps = PorterStemmer()

example_words = ["python","pythoner","pythoning","pythoned","pythonly"]
#Aquí tenemos algunos ejemplos de diferentes variaciones morfológicos de una palabra

# for w in example_words:
#     print(ps.stem(w))
#Con este bucle for hacemos que el Stemmer actúe sobre nuestra lista de palabras dando als raíces de cada una.
#El resultado no es 100% satisfactorio como se pude ver, pero ha funcionado en 4/5 palabras

new_text = "It is very important to be pythonly while you are pythoning with python. All pythoners have phytoned poorly at least once."

words = word_tokenize(new_text)

for w in words:
    print(ps.stem(w))

#El outcome de este fragmento de código nos hace ver la igualación de significados para la máquina reduciendo las palabras a sus raíces
#  A pesar de su poder no es muy utilizado de manera profesional. 
#Su utilidad se hace notable cuando tras el proceso de lemmatizing existen palabras que no pueden ser nombres, en este caso el stemming
#es la única solución posible.