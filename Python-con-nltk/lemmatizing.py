#Vamos a hablar de lemmatizing. El lemmatizing es una operacion similar al stemming 
#Esto hace que el ordenador reconozca las palabras y las cambie por un sinónimo, de modo que se simplifiquen los datos
#para su interpretación
from nltk.stem import WordNetLemmatizer

lemmatizier = WordNetLemmatizer()#Siempre es aconsejable igualar un método en una variable de modo que no haya 
# que escribir el método con todo lo que queremos que trabaje entre paréntesis

# print(lemmatizier.lemmatize("cats"))#EL output de esto es cat, lo cual es una versión simplificada de cats
# print(lemmatizier.lemmatize("cacti"))
# print(lemmatizier.lemmatize("geese"))
# print(lemmatizier.lemmatize("rocks"))
# print(lemmatizier.lemmatize("python"))
#Como podemos ver el ouput de todas estas palabras es el lemma (lexema) de cada una de ellas

print(lemmatizier.lemmatize("better", pos="a"))#El comando pos= muestra un lemmatizier en un sentido específico, en este caso pasamos de better a good el cual es un adjetivo
print(lemmatizier.lemmatize("run", 'n'))
#El default del lemmatizier es sacar nombres, por lo que si encontramos palabras que no son nombres tenemos que pasarlas por el tag of speech
