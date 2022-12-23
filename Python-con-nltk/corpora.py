#Vamos a trabajar con corpus, creando algunos nosotros mismos o viendo algunos con los que podemos trabajar. Se pueden descargar 
# diferentes corpus para trabajar con ellos. EL problema es que no es fácil navegar dentro de ellos.
# ()

import nltk 


# # Common locations on Windows:
#     path += [
#         os.path.join(sys.prefix, str("nltk_data")),
#         os.path.join(sys.prefix, str("share"), str("nltk_data")),
#         os.path.join(sys.prefix, str("lib"), str("nltk_data")),
#         os.path.join(os.environ.get(str("APPDATA"), str("C:\\")), str("nltk_data")),
#         str(r"C:\nltk_data"),
#         str(r"D:\nltk_data"),
#         str(r"E:\nltk_data"),
#     ]
# Aquí está la ubicación. La carpeta nltk_data incluye un montón de datos para entrenar el modelo.
# La carpeta nltk_data está en AppData/Roaming/nltk_data. Allí están todos los corpus que podemos usar
#  Todos se pueden usar, por ejemplo uno bueno para 
# sentimento analysis es movie_reviews. Vamos a trabajar con algunos de estos corpus:

from nltk.corpus import gutenberg
from nltk.tokenize import sent_tokenize

sample = gutenberg.raw("bible-kjv.txt")

tok = sent_tokenize(sample)

print(tok[5:15])

#Se puede usar esta metodología para trabajar con algunos de los corpus. Sin emabrgo la versión .raw no siempre va a funcionar correctamente, aunque si el 90%
# 
