import nltk


# (El uso de nltk es para hacer que una máquina entienda lenguaje natural
# Normalmente pasar la información a texto y una vez hecho esto trabajar con el texto
# Para trabajar con estos datos primero debemos dividir el texto. Algunas técnicas son las isguientes:
# 
# TOkenizing = word tokenizers (divide en palabras), sentence tokenizers (divide en frases)
# 
# Lexicon = esto son las palabras y sus significados dependiendo del signifiCADO Y DE QUIÉN LO DICE ('movida': asunto complicado/ 'movida': descolocada)
# 
# Corpora = es un cuerpo de texto que tiene algo en común (perdiódicos médicos, discursos de presidentes, etc))


from nltk import sent_tokenize, word_tokenize #Esto crea tokens que dividen en frases y palabras

example_text = "Hello Mr. Juan, how are you today? The weather is great and python is awesome. The sky is pink-ish and you should not eat carbo-hydrates" #Si tuvieramos que separar esto, deberíamos mirar por los espacios, los guiones, los signos ortográficos...
#Cuidado con las mayúsculas
#Vamos a usar nltk para separar este texto de ejemplo en frases y palabras evitando tener que escribir nuestras propias expresiones regualres

print(sent_tokenize(example_text))#COmo podemos ver ha separado el texto en frases INCREÍBLE
print(word_tokenize(example_text))#Y ahora igual pero con palabras. POdemos ver que toma los signos ortográficos como una palabra, sin embargo los diminutivos como "MR." los ha respetado


for i in word_tokenize(example_text):
    print(i)
#Hemos recorrido el texto con un bucle for de manera sencilla

#Puedes realizar esto también con otras lenguas aunque es posible que haya algunos errores.

