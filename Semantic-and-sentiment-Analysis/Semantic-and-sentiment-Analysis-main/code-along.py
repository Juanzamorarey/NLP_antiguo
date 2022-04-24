import numpy as np 
import pandas as pd
import nltk

df = pd.read_csv('TextFiles/moviereviews.tsv', sep='\t')

df.dropna(inplace=True)

blanks = []

for i,lb,rv in df.itertuples(): #indice, etiqueta y review
    if type(rv) == str: #Si es un string
        if rv.isspace(): #Si está en blanco (es decir no se pueda analizar)
            blanks.append(i) #Añadimos su posición a uan lista para después eliminarla. 

df.drop(blanks,inplace = True)

a = df['label'].value_counts()
print(a)

# nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

sid = SentimentIntensityAnalyzer()

df['scores'] = df['review'].apply(lambda review:sid.polarity_scores(review))

df['compound'] = df['scores'].apply(lambda d:d['compound'])

df['compound_score'] = df['compound'].apply(lambda score: 'pos' if score >=0 else 'neg')

b = df.head()

# print(b)

# 0   neg  how do films like mouse hunt get into theatres...  {'neg': 0.121, 'neu': 0.778, 'pos': 0.101, 'co...   -0.9125           neg
# 1   neg  some talented actresses are blessed with a dem...  {'neg': 0.12, 'neu': 0.775, 'pos': 0.105, 'com...   -0.8618           neg
# 2   pos  this has been an extraordinary year for austra...  {'neg': 0.068, 'neu': 0.781, 'pos': 0.15, 'com...    0.9951           pos
# 3   pos  according to hollywood movies made in last few...  {'neg': 0.071, 'neu': 0.782, 'pos': 0.147, 'co...    0.9972           pos
# 4   neg  my first press screening of 1998 and already i...  {'neg': 0.091, 'neu': 0.817, 'pos': 0.093, 'co...   -0.2484           neg

from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# print(accuracy_score(df['label'], df['compound_score']))
# Recordemos que si el modelo es inferior a 0.5 significa que estamos haciendo unas predicciones bastante malas
#puesto que es menos que averiguar si es positiva o negativa al azar. La certitud del modelo es la siguiente:
# 0.63

# print(classification_report(df['label'], df['compound_score']))

#               precision    recall  f1-score   support

#          neg       0.72      0.44      0.55       969
#          pos       0.60      0.83      0.70       969

#     accuracy                           0.64      1938
#    macro avg       0.66      0.64      0.62      1938
# weighted avg       0.66      0.64      0.62      1938

print(confusion_matrix(df['label'], df['compound_score']))

# [[427 542]
#  [164 805]]

# Como vemos el modelo no está funcionando muy bien. Esto tiene dos razones: el sarcasmo o la ironía son muy
#difíciles de detectar por los algoritmos de machine learning (cualquiera de ellos), además de esto una review
# negativa puede contener aspectos positivos (la peli era mala pero los actores buenos). Conlusión: el modelo con
#nltk no funciona tan bien como el TF-IDF pero recordemos que el texto no requiere etiquetación previa. 