#En esta parte vamos a hablar de chunking. Imaginemos que tenemos un texto dividido en frases o palabras y que ahora queremos averiguar
# Qué dicen las frases. Primero localizamos la entidad de la frase, es decir, aquello que funciona como sujeto. EL siguiente paso va a ser
# encontrar palabras que dan más información sobre el sujeto. 

# (El proceso de chunking suele dar como resultado grupos de palabras que rodean a un nombre. Para ellos podríamos usar expresiones regulares
# que establecieran una cadena (chunk) desde la que aprtir y luego continuar asociando palabras. Vamos a ver algo práctico)


import nltk 
from nltk.corpus import state_union #Esto es un corpues de textos para trabajar
from nltk.tokenize import PunktSentenceTokenizer #Este es un nuevo tokenizer que puede ser entrenado en los propósitos que nosotros queramos

sample_text = state_union.raw("2006-GWBush.txt")#Del corpus state_union estamos tomando este texto para usarlo como ejemplo
train_text = state_union.raw("2006-GWBush.txt")#Del corpus state_union estamos tomando este texto para usarlo como ejemplo
#Escribimos .raw porque se trata de texto "crudo". Esta será la muestra con la que estaremos trabajando.

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)#Aquí hemos usado el tokenizer para obtener las frases del textos customizadas

tokenized = custom_sent_tokenizer.tokenize(sample_text)#aquí hemos hecho lo mismo a partir del texto con tags incluidas

# (Para comenzar el proceso de chunking debemos primero hacer el tagging del discurso y, posteriormente, comenzar a usar expresiones regulares
# Aquí vamos a usar principalmente modifiers de las expresiones regulares. Es importante entender esto para comprender el código, por ello voy a copiarlo aquí
# {1,3} = para dígitos o numerar espacios
# + = encontrar 1 o más
# ?= encontrar 0 o 1 repetición
# * = encontrar 0 o mas repeticiones
# $ = encuentros al final del string
# ^ = encuentro al principio del string
# | = encontrar algo o algo (x|y: encontrar x o y)
# [] = rango o varianza
# {x} = para ver estesta cantidad antes del código precedente
# {x,y} = espera ver este x-y cantidad antes del código precedente. )


def proccess_content():
    try:
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged= nltk.pos_tag(words)

            chunkGram = r"""Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}"""#La r inicial informa de que se trata de una expresion regular. 
            # En el interior de esta expresión regular introducimos los códigos del speech tagger que hemos usado antes. 
            # De modo que podríamos buscar por ejemplo todos los adverbios (RB) de cualquier tipo ajustando la expresion regulat
            #Es decir, todos los ipos de adverbio son RB adverb RBR, RBS. Cada código tiene diferentes especificaciones
            #Sobre el tipo de adverbio que es pero todos son asdverbios. Por esto ajustamos la expresion regular para que encuentre
            #Todos los códigos. Además después podemos añadir más cosas que se buscarán cuando ejecutemos nuestra expresión regular.


            chunkParser = nltk.RegexpParser(chunkGram) #esto es un parser al que como argumento le pasamos nuestra expresion regular
            chunked = chunkParser.parse(tagged)#El chunkParser que usa nuestra E.REgular v a hacer un parse del discurso que ya tiene las labels

            print(chunked) #Este output será largo e incomprensible. Para verlo de una manera mas eficaz podemos usar .draw()
            chunked.draw()
            #Esto dibuja un arbol que puede ser útil para ver los análisis sintácticos y los enlaces entre las palabras. 
    except Exception as e:
        print(str(e))

proccess_content()