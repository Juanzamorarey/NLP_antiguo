import nltk 
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

#Aquí vamos a hablar del reconocimiento de entidades en python

sample_text = state_union.raw("2006-GWBush.txt")
train_text = state_union.raw("2006-GWBush.txt")

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)
tokenized = custom_sent_tokenizer.tokenize(sample_text)


def proccess_content():
    try:
        for i in tokenized[5:]:
            words = nltk.word_tokenize(i)
            tagged= nltk.pos_tag(words)

            namedEnt = nltk.ne_chunk(tagged)

            namedEnt.draw()

    except Exception as e:
        print(str(e))

proccess_content()
#El name entities recognition a veces falla y se obtienen gran cantidad de falsos positivos, lo que lo hace una herramienta útil pero 
#de la que no se debe confiar mucho




#(Aquí tenemos algunos ejemplos de nombres de entidades para su análisis:
# NE type examples:
# Organization 
# Person
# Location
# Date
# Time
# Money
# Percent
# Facility
# GPE)
    