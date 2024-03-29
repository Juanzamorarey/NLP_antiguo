# El metodo lemmatiazation (limitazation in previous lecture) es más rápido y útil que el stemming.
# Lemmatization utiliza el contexto de la palabra, es decir, las palabras al lado y la sintaxis, para determinar qué tipo de palabra es y
# junto a esta información el conjunto de caracteres nos indicará qué lexema debe encontrar la palabra. Se basa en vectores para dar una idea.


import spacy
nlp = spacy.load('en_core_web_sm')

doc1 = nlp(u'I am a runner running in a race, because I love to run since I ran today')

# for token in doc1:
#     print(token.text,'\t',token.pos_,'\t',token.lemma,'\t',token.lemma_)

# El output nos da la palabra, un tab, el pos que ya vimos en otra unidad, el lemma (que es un número), y el lemma visualizado. El número que indica
# el método .lemma se trata de la posición que ocupa el vector de la palabra dentro de la librería en_core_web_sm. 
# Vamos a utilizar una función ahora que muestre de manera más visual y correcta los lemmas, para no tener un formato tan sucio usando f strings.

def show_lemmas(text):
    for token in text:
        print(f'{token.text:{12}} {token.pos_:{6}} {token.lemma:<{22}} {token.lemma_}')

doc2 = nlp(u'I saw ten mice today!')

show_lemmas(doc2)

# Lemmatization se usa para reducir la cantidad de palabras con las que trabajar en un texto, recordemos que NLP se trata de un pretratamiento textual
# en el que haremos pasar al texto por una serie de procesos para facilitar su uso. 