import spacy


nlp = spacy.load("en_core_web_md")

# words_1 = "I like apples"
# words_2 = "I like oranges"
# words_3 = "I like burgers"


# processed_1 = nlp(words_1)
# processed_2 = nlp(words_2)
# processed_3 = nlp(words_3)

# print(f" Esta frase {words_1} se parece a esta {words_2} con este procentaje {processed_1.similarity(processed_2)}")
# print(f" Esta frase {words_1} se parece a esta {words_3} con este procentaje {processed_1.similarity(processed_3)}")

# Método .similarity() mira los vectores de las frases y compara su proximitud.

# Los atributte rulers de spacy:
# Dependency parser
# Entity linker
# EntityRecognizer
# EntityRuler
# Lemmatizer
# Morpholog
# SentenceRecognizer
# Sentencizer
# SpanCategorizer
# Tagger
# TextCategorizer
# Tok2Vec -> word embeddings
# Tokenizer
# TrainablePipe
# Transformer

# How to add pipes

# Primero crearlo y luego ir añadiendo features al pipeline. Al indicar el idioma le indicamos el
# tokenizer deseado

nlp_2 = spacy.blank("en")

# añadimos al pipeline lo que queramos, por ejemplo un sentecizer.
# nlp_2.add_pipe(nlp_2.create_pipe('sentencizer'))

nlp_2.add_pipe("sentencizer")

# Es útil si queremos hacer una tarea determinada para ahorrar tiempo de procesamuiento.
# Entiendiendo siempre que el accuracy será peor.

# .analyze_pipes() nos muestra nuestro pipeline

print(nlp_2.analyze_pipes())


# {'summary': {'sentencizer': {'assigns': ['token.is_sent_start', 'doc.sents'], 'requires': [], 'scores': ['sents_f', 'sents_p', 'sents_r'], 'retokenizes': False}}, 'problems': {'sentencizer': []}, 'attrs': {'doc.sents': {'assigns': ['sentencizer'], 'requires': []}, 'token.is_sent_start': {'assigns': ['sentencizer'], 'requires': []}}}

# Podemos ver que solamente el sentencizer, veamos ahora un pipeline precreado:
print(nlp.analyze_pipes())
# {'summary': {'tok2vec': {'assigns': ['doc.tensor'], 'requires': [], 'scores': [], 'retokenizes': False}, 'tagger': {'assigns': ['token.tag'], 'requires': [], 'scores': ['tag_acc'], 'retokenizes': False}, 'parser': {'assigns': ['token.dep', 'token.head', 'token.is_sent_start', 'doc.sents'], 'requires': [], 'scores': ['dep_uas', 'dep_las', 'dep_las_per_type', 'sents_p', 'sents_r', 'sents_f'], 'retokenizes': False}, 'attribute_ruler': 
# {'assigns': [], 'requires': [], 'scores': [], 'retokenizes': False}, 'lemmatizer': {'assigns': ['token.lemma'], 'requires': [], 'scores': ['lemma_acc'], 'retokenizes': False}, 'ner': {'assigns': ['doc.ents', 'token.ent_iob', 'token.ent_type'], 'requires': [], 'scores': ['ents_f', 'ents_p', 'ents_r', 'ents_per_type'], 'retokenizes': False}}, 'problems': {'tok2vec': [], 'tagger': [], 'parser': [], 'attribute_ruler': [], 'lemmatizer': 
# [], 'ner': []}, 'attrs': {'token.ent_iob': {'assigns': ['ner'], 'requires': []}, 'doc.ents': {'assigns': ['ner'], 'requires': []}, 'token.tag': {'assigns': ['tagger'], 'requires': []}, 'token.dep': {'assigns': ['parser'], 'requires': []}, 'doc.sents': {'assigns': ['parser'], 'requires': []}, 'token.head': {'assigns': ['parser'], 'requires': []}, 'doc.tensor': {'assigns': ['tok2vec'], 'requires': []}, 'token.lemma': {'assigns': ['lemmatizer'], 'requires': []}, 'token.ent_type': {'assigns': ['ner'], 'requires': []}, 'token.is_sent_start': {'assigns': ['parser'], 'requires': []}}}
# Aquí vemos un tagger, un tok2vec, un name entity recognizer...


