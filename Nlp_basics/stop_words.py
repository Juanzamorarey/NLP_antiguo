# Las stop words son todas la spreposiciones o palabras con significado simplemente gramatical que molestan a la hora de tratar el texto
# Un proceso muy normal es eliminarlas. Para eliminarlas podemos usar spacy, también vamos a ver como mantener algunas para casos particulares.

import spacy

nlp = spacy.load('en_core_web_sm')

# print(nlp.Defaults.stop_words)
# Aquí tenemos todas las stop words dentro la libreria spacy, tiene un len() de 305. Puedes comprobar si una palabra es un stop word de la siguiente
# manera:

# print(nlp.vocab['mystery'].is_stop)

# Si obtenemos true se trata de un stop_wprd, en caso contrario no. 
# Imagine entonces que estás trabajando con una serie de comentarios de twitter y en ellos aparecen abreviaciones tales como 'btw' por 'by the way'
# En ese caso lo que tenemos que hacer es añadir este 'btw' como stop word. Se hace así:

nlp.Defaults.stop_words.add('btw')
nlp.vocab['btw'].is_stop = True

# Así habremos añadido btw a las stop words. Para comprobarlo:

# print(len(nlp.Defaults.stop_words))
# Si se ha añadido debería haber una
print(nlp.vocab['btw'].is_stop)
# Otra manera es simplemente comprobarlo

# Imaginemos ahora que quieres eliminar una de las stop_words del set puesto que es especialmetne importante para este trabajo. 

nlp.Defaults.stop_words.remove('btw')
nlp.vocab['btw'].is_stop = False
# Aquí la hemos eliminado

print(nlp.vocab['btw'].is_stop)
