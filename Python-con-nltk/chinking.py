#Chinking es parte del chunking. Esto viene a solucionar el siguiente problema. En el chunking creábamos una expresión regular que 
#cogía partes del texto con las que queríamos trabajar. Bien, si dentro de esas aprtes queremos eliminar algunas deberemos ser
#aún más precisos, ahí es donde entra el chinking.

import nltk 
from nltk.corpus import state_union #Esto es un corpues de textos para trabajar
from nltk.tokenize import PunktSentenceTokenizer #Este es un nuevo tokenizer que puede ser entrenado en los propósitos que nosotros queramos

sample_text = state_union.raw("2006-GWBush.txt")#Del corpus state_union estamos tomando este texto para usarlo como ejemplo
train_text = state_union.raw("2006-GWBush.txt")#Del corpus state_union estamos tomando este texto para usarlo como ejemplo
#Escribimos .raw porque se trata de texto "crudo". Esta será la muestra con la que estaremos trabajando.

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)#Aquí hemos usado el tokenizer para obtener las frases del textos customizadas

tokenized = custom_sent_tokenizer.tokenize(sample_text)#aquí hemos hecho lo mismo 


def proccess_content():
    try:
        for i in tokenized[5:]:
            words = nltk.word_tokenize(i)
            tagged= nltk.pos_tag(words)

            chunkGram = r"""Chunk: {<.*>+}
                            }<VB.?|IN|DT|TO>+{"""#Con esta expresión regular estamos: en la primera parte cogiendo 1 o más de cualquier elemento. 
                            #Mientras que en la segunda estamos dejando fuera de nuestra selección cualquier verbo, preposición o determinante 
            

            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged)
            chunked.draw()




    except Exception as e:
        print(str(e))

proccess_content()