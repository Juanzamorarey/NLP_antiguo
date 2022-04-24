# (Cada vez que creamos un proceso de entrenamiento para un clasificador abrimos el programa que, al cerrarse, hace que se pierdan todos
# los procesos que se estaban llevando a cabo, es por eso que si queremos entrenar el modelo y no tener que rentrnarlo cada vez
# podemos simplemente guardarlo con pickle)

import nltk 
import random
from nltk.corpus import movie_reviews 
import pickle

documents = [(list(movie_reviews.words(fileid)),category)#esto va a ser una lista de tuplas, las cuales serán palabras que clasificaremos
            for category in movie_reviews.categories()#Esto clasifica en positivo o negativo
            for fileid in movie_reviews.fileids(category)]#Esto identifica la categoría

random.shuffle(documents)

all_words = []

for w in movie_reviews.words():
    all_words.append(w.lower())

all_words = nltk.FreqDist(all_words)

word_features = list(all_words.keys())[:3000]

def find_features (document):
    words = set(document) 
    features = {}
    for w in word_features:
        features[w] = (w in words)

    return features

featuresets = [(find_features(rev),category) for (rev,category) in documents]


training_set = featuresets[:1900] 
testing_set = featuresets[1900:]

classifier = nltk.NaiveBayesClassifier.train(training_set) 

# (ATeNCIÖN)
classifier_f = open("naivebayes.pickle","rb")
classifier = pickle.load(classifier_f)
classifier_f.close()
# (ATENCIÓN el bloque de código que tenemos aquí arriba se trata de una comprobación para ver si pickle ha funcionado en el código
# de abajo, por lo que no funcionará si se corren los dos a la vez.)

print("Naive Bayes Algo accuracy percent:", (nltk.classify.accuracy(classifier,testing_set))*100)
classifier.show_most_informative_features(15)




# save_classifier = open("naivebayes.pickle","wb")#Aquí reescribimos el classifier en modo lectura
# pickle.dump(classifier, save_classifier)#Aquí recuerda que volcamos el contenido

# save_classifier.close()#Y aquí cerramos el programa

# (Aquí empieza la lección . 
# En este caso tenemos únicamente un algoritmo pero, normalmente tendremos varios algoritmos ocurriendo simultáneamente. Para que esto ocurra
# sin tardar mucho en cargar deberemos guardarlo con pickle.)

