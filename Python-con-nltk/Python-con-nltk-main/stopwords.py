#Antes de comenzar el análisis debemos procesar el texto en varias maneras.
#nltk nos ayuda con eso más que muchas otras librerias
#Las stop words son palabras que queremos eliminar ya que no aportan significado léxico sino grmatical (preposiciones, artículos, etc)

from nltk.corpus import stopwords #Para trabajar con stopwords
from nltk.tokenize import word_tokenize #El tokenizer que vimos en la anterior

example_sentence = "This is an example showing off stop word filtration." #Ejemplo de frase

stop_words = set(stopwords.words("english"))#Auqui tenemos una lista de stopwords en inglés/español muy común

# print(stop_words)#Si imprimimos la lista la podemos ver

words = word_tokenize(example_sentence)

# filtered_sentence = []

# for w in words:
#     if w not in stop_words:
#         filtered_sentence.append(w)
# (Vamos ahora a eliminar las stopwords de la frase de ejemplo. Para ello creamos una lista con el word tokenizer a aprtir de nuestro texto y, después, otra lista vacía a la que iremos añadiendo
# . Más tarde con un bucle for recorremos nuestro texto y, en caso de que alguna de las palabras de nuestro texto esté también en la lista de stopwrds comúnes del idioma elegido,
# la añadimos a la lista vacía)
# print(filtered_sentence)

#(En este print vemos el resultado de las palabras que se eliminarán. Como podemos ver el resultado no es perfecto, algunas de las palabras que se han eliminado deberían haber permanecido
# Sin embargo el resultado es bastante satisfactorio.)

filtered_sentence = [w for w in words if not w in stop_words]
# Esto hace lo siguiente: para cada palabra(w) en words(words) si la palabra no está en stop_words entonces es parte de la filtered sentence
#Esto es en realidad una lsita que reúne una serie de condiciones, en este caso toda aquella palabra que no está en stop words, es decir, la frase limpia de stop words
print(filtered_sentence)
