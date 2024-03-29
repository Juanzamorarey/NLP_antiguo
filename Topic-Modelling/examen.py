import pandas as pd

docuemnto = pd.read_csv("quora_questions.csv")

print(docuemnto.head())

from sklearn.feature_extraction.text import TfidfVectorizer
# importamos el vectorizador

tfidf = TfidfVectorizer(max_df=0.95,min_df=2,stop_words="english")
# Tenemos nuestro objeto Tfidf con los parametros deseados, las palabras deben aparecer en al menos el 95% de los textos
#  y como mínimo en 2 de ellos. Además eliminamos las stopwords del idioma inglés
matriz = tfidf.fit_transform(docuemnto["Question"])
# Creamos la matriz a partir de la columna question

# print(dtm)

from sklearn.decomposition import NMF
nmf_model = NMF(n_components=20,random_state=42)
# Creamos nuestro objeto analizador NMF con un número de 20 topics y un random_state de 42

nmf_model.fit(matriz)
# Introducimos nuestra matriz en el modelo
# print(a)
for indice,topic in enumerate(nmf_model.components_):
    print(f"THE TOP 15 WORDS FOR TOPIC # {indice}")
    print([tfidf.get_feature_names()[i] for i in topic.argsort()[-15:]])
    print("\n")
# Impirmimos las 15 palabras mas usadas por topic

# THE TOP 15 WORDS FOR TOPIC # 0
# ['thing', 'read', 'place', 'visit', 'places', 'phone', 'buy', 'laptop', 'movie', 'ways', '2016', 'books', 'book', 'movies', 'best']


# THE TOP 15 WORDS FOR TOPIC # 1
# ['majors', 'recruit', 'sex', 'looking', 'differ', 'use', 'exist', 'really', 'compare', 'cost', 'long', 'feel', 'work', 'mean', 'does']


# THE TOP 15 WORDS FOR TOPIC # 2
# ['add', 'answered', 'needing', 'post', 'easily', 'improvement', 'delete', 'asked', 'google', 'answers', 'answer', 'ask', 'question', 'questions', 'quora']


# THE TOP 15 WORDS FOR TOPIC # 3
# ['using', 'website', 'investment', 'friends', 'black', 'internet', 'free', 'home', 'easy', 'youtube', 'ways', 'earn', 'online', 'make', 'money']


# THE TOP 15 WORDS FOR TOPIC # 4
# ['balance', 'earth', 'day', 'death', 'changed', 'live', 'want', 'change', 'moment', 'real', 'important', 'thing', 'meaning', 'purpose', 'life']


# THE TOP 15 WORDS FOR TOPIC # 5
# ['reservation', 'engineering', 'minister', 'president', 'company', 'china', 'business', 'country', 'olympics', 'available', 'job', 'spotify', 'war', 'pakistan', 'india']


# THE TOP 15 WORDS FOR TOPIC # 6
# ['beginners', 'online', 'english', 'book', 'did', 'hacking', 'want', 'python', 'languages', 'java', 'learning', 'start', 'language', 'programming', 'learn']


# THE TOP 15 WORDS FOR TOPIC # 7
# ['happen', 'presidency', 'think', 'presidential', '2016', 'vote', 'better', 'election', 'did', 'win', 'hillary', 'president', 'clinton', 'donald', 'trump']


# THE TOP 15 WORDS FOR TOPIC # 8
# ['russia', 'business', 'win', 'coming', 'countries', 'place', 'pakistan', 'happen', 'end', 'country', 'iii', 'start', 'did', 'war', 'world']


# THE TOP 15 WORDS FOR TOPIC # 9
# ['indian', 'companies', 'don', 'guy', 'men', 'culture', 'women', 'work', 'girls', 'live', 'girl', 'look', 'sex', 'feel', 'like']


# THE TOP 15 WORDS FOR TOPIC # 10
# ['ca', 'departments', 'positions', 'movies', 'songs', 'business', 'read', 'start', 'job', 'work', 'engineering', 'ways', 'bad', 'books', 'good']


# THE TOP 15 WORDS FOR TOPIC # 11
# ['money', 'modi', 'currency', 'economy', 'think', 'government', 'ban', 'banning', 'black', 'indian', 'rupee', 'rs', '1000', 'notes', '500']


# THE TOP 15 WORDS FOR TOPIC # 12
# ['blowing', 'resolutions', 'resolution', 'mind', 'likes', 'girl', '2017', 'year', 'don', 'employees', 'going', 'day', 'things', 'new', 'know']


# THE TOP 15 WORDS FOR TOPIC # 13
# ['aspects', 'fluent', 'skill', 'spoken', 'ways', 'language', 'fluently', 'speak', 'communication', 'pronunciation', 'speaking', 'writing', 'skills', 'improve', 'english']


# THE TOP 15 WORDS FOR TOPIC # 14
# ['diet', 'help', 'healthy', 'exercise', 'month', 'pounds', 'reduce', 'quickly', 'loss', 'fast', 'fat', 'ways', 'gain', 'lose', 'weight']


# THE TOP 15 WORDS FOR TOPIC # 15
# ['having', 'feel', 'long', 'spend', 'did', 'person', 'machine', 'movies', 'favorite', 'job', 'home', 'sex', 'possible', 'travel', 'time']


# THE TOP 15 WORDS FOR TOPIC # 16
# ['marriage', 'make', 'did', 'girlfriend', 'feel', 'tell', 'forget', 'really', 'friend', 'true', 'know', 'person', 'girl', 'fall', 'love']


# THE TOP 15 WORDS FOR TOPIC # 17
# ['easy', 'hack', 'prepare', 'quickest', 'facebook', 'increase', 'painless', 'instagram', 'account', 'best', 'commit', 'fastest', 'suicide', 'easiest', 'way']


# THE TOP 15 WORDS FOR TOPIC # 18
# ['web', 'java', 'scripting', 'phone', 'mechanical', 'better', 'job', 'use', 'account', 'data', 'software', 'science', 'computer', 'engineering', 'difference']

# THE TOP 15 WORDS FOR TOPIC # 19
# ['earth', 'blowing', 'stop', 'use', 'easily', 'mind', 'google', 'flat', 'questions', 'hate', 'believe', 'ask', 'don', 'think', 'people']


topic_results = nmf_model.transform(matriz)
# topic_results.argmax(axis=1)

docuemnto["topic"] = topic_results.argmax(axis=1)

print(docuemnto.head())