# Tokenization es el proceso de romper el texto en tokens. Esto ocurre cuando usamos spacy para separar textos o frases.

# Los tokens son la pieza mínima de las que vamos a trabajar. Tenemos prefijos, sufijos, infijos y excepciones, entrando en esta última
# todos los símbolos de ortografía. Dentro de los sufijos, prefijos e infijos entran también los guiones así como km., $, %...
# Vamos a ver cómo trabajar con spacy y los tokens

import spacy
nlp = spacy.load('en_core_web_sm')


# mystring = '"We\'re moving to L.A.!"'

# doc = nlp(mystring)

# for token in doc:
#     print(token.text)

# Al ejecutar este código vamos a ver que spacy puede separar aquellos signos que no forman parte de una palabra como tokens individuales (en este caso
# el símbolo de interrogación) Pero no va a separar los puntos en L.A. o los apóstrofes de las otras palabras. También separa las comillas

# doc2 = nlp(u"We're here to help! Send snail-mail, email support@oursite.com or visit at http://www.oursite.com!")

# for t in doc2:
#     print(t)

# En este ejemplo vemos como un string como este, muy difícil de catalogar por la cantidad de símbolos, funciona bien en spacy excepto por el -
#  Si ponemos el modo de lectura con la u delante no se tomarán las comillas como tokens individuales. Podemos ver asimismo la cantidad de tokens
# de un objeto con len()

doc4 = nlp(u"Let's visit St.Louis in the U.S. next year.")

# print(len(doc4))

#  y de una libreria con .vocab. Aparte de esto podemos recorrer los tokens como si se tratara de una lista.

print(len(doc4.vocab))

doc5 = nlp(u"It is better to give than receive.")

print(doc5[0:4])

# Es importante recordar que las posiciones de estas listas no pueden ser reasignadas:

# doc5[0] = 'pene'
# Este código va a dar error porque no se pueden reasignar dichas posiciones. 

# Spacy puede reconocer, además de tokens, entidades, que son útiles para análisis sentimental de textos. 

doc8 = nlp(u'Apple to build a Hong Kong factory for $6million')

# Con este código lo que hacemos es añadir un final a cada uno de los tokens, en este caso unos espacios y la barra |.
# for token in doc8:
#     print(token.text, end='   |   ')

for entity in doc8.ents:
    print(entity)
    print(entity.label_)
    print(str(spacy.explain(entity.label_)))
    print('\n')

# Con el comando .ents vemos las entidades que hay dentro del documento y, con el label_, podemos ver las abreviaciones de lo que son estas entidades para
# spacy: money, organization, or geopolitical. Si hubiera problemas para estas entidades podemos añadir esta linea de código:
# print(str(spacy.explain(entity.label_)))
# En la cual con el comando .explain() spacy nos da una explicación de las etiquetas para evitar confusiones. 
# Gracias a las entidades tenemos lo que se llaman noun chunks, es decir, sintagmas nominales que tienen un nombre como cabeza y todo lo que 
# les acompaña.

doc9 = nlp(u'Autonomous cars shift insurance liability toward manufacturers.')

# En este caso podemos ver que el chunk correspondería a Autonomous cars, luego hay otro de insurance liability, y por último manufacturers que no tiene adj.

for chunk in doc9.noun_chunks:
    print(chunk)

# Al ejecutar este bloque for con el metodo .noun_chunks vemos como aparecen todos los sintagmas nominales contenidos en el texto. 