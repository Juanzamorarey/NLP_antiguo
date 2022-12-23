# En esta parte vamos a ver lo básico de procesamiento del lenguaje natural. Para ello utilizaremos spacy además de entender lo básico como:

# (tokenization
# Stemming
# Lemmatization
# Stop words
# 
# 
# 
# 
# También hablaremos sobre spacy y NLTK)

# Para la mayoría de tareas habituales spacy es mas rápido, mientras que NLTK es mas útil, pero menos eficaz.

# Para empezar vamos a ver los usos básicos de spacy. 

import spacy
nlp = spacy.load('en_core_web_sm')
# En NLP guardamos el objeto canalizador, es decir, la libreria que ya hemos descargado previamente.


# Con spacy, al igual que con otras librerias de NLP, tenemos que crear objetos de canalización que nos sirvan como modelo para trabajar a partir de ellos.
# Entonces, este objeto de canalización va a llevar a cabo una serie de tareas comunes en NLP como funciones:
# (tokenize
# tag
# parse...
# )

doc = nlp(u'Tesla is looking at buying U.S. startup for $6 million')
# Aquí llevamos a cabo una operación de lectura con nuestro objeto de canalización a un texto que está ya precodificado, de ahi la u inicial. 
# Nuestro objeto va a parsear la frase y crear tokens por cada palabra. COn este bucle for vemos que ha separado la frase en palabras, incluyendo
# acrónimos, o símbolos del dolar. 

# for token in doc:
#     print(token.text,token.pos,token.dep_)

# El comando .text imprime el texto crudo y el comando .pos se refiere a part of speech que contiene un número el cual se corresponde a una categoría gramatical. 
# si ponemos .pos_ nos dirá la palabra clara. Así también .dep_ nos dará las dependencias sintácticas. 


# nlp.pipeline

# El metodo pipeline lo que hace es llevar a cabo todas las operaciones de tagger, parser y ner sobre un texto. Esto es extremadamente útil a la hora de 
# trabajar de forma mas eficiente. 

# Vamos a hablar ahora de cada uno de estos procesos más detenidamente, empecemos por la tokenization:

# Tokenization consiste en dividir un texto en pequeñas partes con las que podamos trabajar. Estos fragmentos se llaman tokens:

# doc2 = nlp(u"Tesla isn't looking into startups anymore.")

# for token in doc2:
#     print(token.text, token.pos_,token.dep_)

# Podemos también trabajar también con los tokens de forma individual como si se tratara de una lista:

# print(doc2[0].pos_)
# print(doc2[0].dep_)

# Aquí por ejemplo imprimimos el part of speech del primer elemento del texto y el output nos indica que se trata de un nombre propio. En la documentacion
# hay más información con la que podemos trabajar sobre las extensiones de spacy. Podemos también cambiar la lengua o también ver en dicha documentacion
# los códigos de las palabras clave. Las dependencias sintácticas pueden estar en inglés y alemán. 

# Aparte de los que ya hemos visto hay también multitud de etiquetas como lemmas, entidades, forma, saber si es alfanumerico o si es un singo de puntuacion
# ,etc.


# Cuando trabajamos con strings muy largos podemos tener algunos problemas que también se pueden solucionar con spacy.

doc3 = nlp(u'Although commmonly attributed to John Lennon from his song "Beautiful Boy", \
the phrase "Life is what happens to us while we are making other plans" was written by \
cartoonist Allen Saunders and published in Reader\'s Digest in 1957, when Lennon was 17.')

# Imaginemos que queremos coger de este string solo el span, o sea, posición de una parte del string

life_quote = doc3[16:30]
print(life_quote)

# spacy es capaz de entender a su vez que cuando almacenamos algo de texto en una variable se trata de un lapspo del texto. Por ejemplo:

print(type(life_quote))

# EL comando type nos da explicaciones cobre los objetos, y aqui indica que se trata de un SPan o lapso. Spacy también puede dividir en oraciones

doc4 = nlp(u"This is the first sentence. This is another sentence. This is the last sentence")

for sentence in doc4.sents:
    print(sentence)

# De nuevo podemos trabajar a traves deotros metodos para saber si se trata o no del principio de una frase: 

print(doc4[0].is_sent_start)

# Si se trata del principio devolverá un True, si no, devolverá un None