#Vamos a hablar del part of speech tagging, es decir, poner etiquetas a las palabras para identificarlas. 
import nltk 
from nltk.corpus import state_union #Esto es un corpues de textos para trabajar
from nltk.tokenize import PunktSentenceTokenizer #Este es un nuevo tokenizer que puede ser entrenado en los propósitos que nosotros queramos

sample_text = state_union.raw("2006-GWBush.txt")#Del corpus state_union estamos tomando este texto para usarlo como ejemplo
train_text = state_union.raw("2006-GWBush.txt")#Del corpus state_union estamos tomando este texto para usarlo como ejemplo
#Escribimos .raw porque se trata de texto "crudo". Esta será la muestra con la que estaremos trabajando.

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)#Aquí hemos usado el tokenizer para obtener las frases del textos customizadas

tokenized = custom_sent_tokenizer.tokenize(sample_text)#aquí hemos hecho lo mismo 

# (USamos dos textos porque uno servirá de entrenamiento para analizar el otro. Vamos a crear algunas funciones para realizar el entrenamiento)

def proccess_content():
    try:
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged= nltk.pos_tag(words)
            print(tagged)
    except Exception as e:
        print(str(e))

proccess_content()

#(Como vemos en el output de este código tenemos todo el discurso del presidente con etiquetas para cada palabra, identificándoals como verbos, signos de puntuación
# nombres, etc. Se trata de algo muy útil para la creación de textos)
#Con este procedimiento hemos creado una tupla para cada palabra en la que se contiene su información. Cada código corresponde a una clasificación de la categoría
#gramatical de la palabra, y algunas que courren en el discurso de una enunciación natural tales como interjecciones. 
#A veces falla porque nltk reconoce el texto correcto y en algunos comentarios o reviews la gente no escribe según estos parámetros.

# (A continuación copio una lista de las claves que da el output sobre la clasificación de palabras según su categoría gramatical:
#     CC coordinating conjunction
    # CD cardinal digit
    # DT determiner
    # EX existential there (like: “there is” … think of it like “there exists”)
    # FW foreign word
    # IN preposition/subordinating conjunction
    # JJ adjective ‘big’
    # JJR adjective, comparative ‘bigger’
    # JJS adjective, superlative ‘biggest’
    # LS list marker 1)
    # MD modal could, will
    # NN noun, singular ‘desk’
    # NNS noun plural ‘desks’
    # NNP proper noun, singular ‘Harrison’
    # NNPS proper noun, plural ‘Americans’
    # PDT predeterminer ‘all the kids’
    # POS possessive ending parent’s
    # PRP personal pronoun I, he, she
    # PRP$ possessive pronoun my, his, hers
    # RB adverb very, silently,
    # RBR adverb, comparative better
    # RBS adverb, superlative best
    # RP particle give up
    # TO, to go ‘to’ the store.
    # UH interjection, errrrrrrrm
    # VB verb, base form take
    # VBD verb, past tense took
    # VBG verb, gerund/present participle taking
    # VBN verb, past participle taken
    # VBP verb, sing. present, non-3d take
    # VBZ verb, 3rd person sing. present takes
    # WDT wh-determiner which
    # WP wh-pronoun who, what
    # WP$ possessive wh-pronoun whose
    # WRB wh-abverb where, when)