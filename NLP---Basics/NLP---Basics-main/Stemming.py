# Vamos a hablar de Stemming. ¿Qué es Stemming?, es crear en las búsquedas de una palabra que se toma como orígen y recuperar del texto todas las que estén
# relacionadas con dicha palabra. Así, si busco "barco" con stemming recuperaré también "barca","barcos",etc. 
# En inglés se trata de una tarea difícil y la librería spacy no incluye un stemizador, pero siempre aparecerá en NLP como una herramienta fundamental. 
# Spacy usa un limitaizer, por lo que usaremos NLTK para hacer Stemming. 

import nltk
from nltk.stem.porter import PorterStemmer

p_stemmer = PorterStemmer()


words = ["run","runner","ran","runs","easily","fairly","fairness"]

# Dentro de NLTK el mejor stemmer es el de porter que utiliza un algoritmo de 5 niveles para averiguar las relaciones de la palabra a partir de 
# sufijos y prefijos. Vamos a ir con un ejemplo:

# for word in words:
#     print(word + '------>' + p_stemmer.stem(word))

# Este bucle va a imprimir la palabra de la lista, una línea y después la clasificación de la palabra a partir del stemmer. El resutado es:
# run------>run
# runner------>runner
# ran------>ran
# runs------>run
# easily------>easili
# fairly------>fairli

# Como podemos ver el stemmer puede reconocer que runner es un nombre no un verbo. Asimismo podemos ver que en los adverbio cambia y por i lo que
# es también interesante. 

# Existe otro stemer que es también muy utilizado y mas eficaz llamado snowball stemer. Este stemer requiere como argumento que pasemos el idioma
# Vamos a ver que el output que ofrece es diferente al anterior, mas eficaz y más rápido. 

from nltk.stem.snowball import SnowballStemmer
s_stemmer = SnowballStemmer(language='english')

# for word in words:
#     print(word + '-------->' + s_stemmer.stem(word))

# run-------->run
# runner-------->runner
# ran-------->ran
# runs-------->run
# easily-------->easili
# fairly-------->fair

# Como podemos ver el output de esto da como resultado palabras más específicas, reconociendo fair en fairly. Lo importante mas que el proceso
# es entender que se trata de un algoritmo que reduce las letras de la palabra en busca de un lexema para la palabra. 


words2=['generous','generation',"generously","generate"]

for word in words2:
    print(word + '-------->' + s_stemmer.stem(word))

# Cuando vemos en este ejemplo, se reducen las palabras a un intento de lexema pero falla ya que si bien generation y generate son similares 
# morfológicamente, no lo son semánticamente y aún así quedan reducidas al mismo lexema. 

# generous-------->generous
# generation-------->generat
# generously-------->generous
# generate-------->generat

# Si bien este proceso es conocido en NLP se utiliza ahora de manera mucho más habitual el metodo llamado limitación. 