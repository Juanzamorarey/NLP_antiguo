# Impñort spacy and load the language library. Remeber tio use a larger model
import spacy

nlp = spacy.load('en_core_web_md')

#Choose the words you wish to compare, and obtain their vectors

king = "king"
queen = "queen"
prince = "prince"

palabras = u'king queen prince'

queen_vector = nlp(u'queen').vector

prince_vector = nlp(u'prince').vector

king_vector = nlp(u'king').vector

#Import spatial and define cosine_similarity function

from scipy import spatial

cosine_similarity = lambda vec1, vec2: 1 - spatial.distance.cosine(vec1,vec2)

#Write an expression for vector arithmetic and list top ten closest vectors in the vocabulary to result the expression.
#Doing it within a function is a plus!!

def vector_match(a,b,c):
    a = nlp.vocab[f'{a}'].vector
    b = nlp.vocab[f'{b}'].vector
    c = nlp.vocab[f'{c}'].vector

    new_vector = a-b+c

    computed_similarities = []

    for palabra in nlp.vocab:
        if palabra.has_vector:
            if palabra.is_lower:
                if palabra.is_alpha:
                    similarity = cosine_similarity(new_vector, palabra.vector) 
                    computed_similarities.append((palabra,similarity))

    computed_similarities = sorted(computed_similarities, key=lambda item:-item[1])

    for i in computed_similarities[:10]:
        print(i[0].text)

# vector_match("tree","sheets","sheets")


# Perform VADER Snetiment Analysis on your own review:

#Import SntiementIntensistyAnalizer and crat a sid object

from nltk.sentiment.vader import SentimentIntensityAnalyzer

sid = SentimentIntensityAnalyzer()

#Write a review as one continuous string.

review = "This was the most Fascinating movie I've ever seen. The plot was great and the performance of Peter is outstanding"

# a = sid.polarity_scores(review)

# print(a)


def analiza_reviews(review):
    review_analizada = sid.polarity_scores(review)

    if review_analizada['compound'] > 0:
        print("Es una review positiva")
    elif review_analizada['compound'] < 0:
        print("Es una review negativa")
    else:
        print("Es una review neutral")

analiza_reviews(review)