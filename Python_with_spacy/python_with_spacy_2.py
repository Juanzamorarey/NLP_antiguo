# Aquí vamos a ver rule base matching con spacy
import spacy
nlp = spacy.load("en_core_web_sm")
text = "West Chesternfieldville was referenced in Mr. Deeds"

doc = nlp(text)

# spacy nos permite la aproxmación con reglas de inferencia y la aproximación con ML

# Imaginemos que queremos extraer fechas de un texto con la aproximación de reglas.
# Y nombres con la aproximación de ML.

# Vamos a extraer las entidades de este texto

for ent in doc.ents:
    print(ent.text, ent.label_)

# West Chesternfieldville PERSON
# Deeds PERSON

# Vemos que no ha podido extraer Chesternfieldville como un pueblo ni Mr. Deeds
# Vamos a arreglarlo con un ruler matcher

ruler = nlp.add_pipe("entity_ruler")
# Añadimos este feature a nuestro pipeline, si análizamos ahora el pipeline veremos que 
# se ha añadido correctamente el entity_ruler.
print(nlp.analyze_pipes())
# {'summary': {'tok2vec': {'assigns': ['doc.tensor'], 'requires': [], 'scores': [], 'retokenizes': False}, 'tagger': {'assigns': ['token.tag'], 'requires': [], 'scores': ['tag_acc'], 'retokenizes': False}, 'parser': {'assigns': ['token.dep', 'token.head', 'token.is_sent_start', 'doc.sents'], 'requires': [], 'scores': ['dep_uas', 'dep_las', 'dep_las_per_type', 'sents_p', 'sents_r', 'sents_f'], 'retokenizes': False}, 'attribute_ruler': 
# {'assigns': [], 'requires': [], 'scores': [], 'retokenizes': False}, 'lemmatizer': {'assigns': ['token.lemma'], 'requires': [], 'scores': ['lemma_acc'], 'retokenizes': False}, 'ner': {'assigns': ['doc.ents', 'token.ent_iob', 'token.ent_type'], 'requires': [], 'scores': ['ents_f', 'ents_p', 'ents_r', 'ents_per_type'], 'retokenizes': False}, 'entity_ruler': {'assigns': ['doc.ents', 'token.ent_type', 'token.ent_iob'], 'requires': [], 'scores': ['ents_f', 'ents_p', 'ents_r', 'ents_per_type'], 'retokenizes': False}}, 'problems': {'tok2vec': [], 'tagger': [], 'parser': [], 'attribute_ruler': [], 'lemmatizer': [], 'ner': [], 'entity_ruler': []}, 'attrs': {'doc.sents': {'assigns': ['parser'], 'requires': []}, 'token.head': {'assigns': ['parser'], 'requires': []}, 'doc.ents': {'assigns': ['ner', 'entity_ruler'], 'requires': []}, 'token.ent_type': {'assigns': ['ner', 'entity_ruler'], 'requires': []}, 'token.is_sent_start': {'assigns': ['parser'], 'requires': []}, 'token.tag': 
# {'assigns': ['tagger'], 'requires': []}, 'token.lemma': {'assigns': ['lemmatizer'], 'requires': []}, 'token.ent_iob': {'assigns': ['ner', 'entity_ruler'], 'requires': []}, 'token.dep': {'assigns': ['parser'], 'requires': []}, 'doc.tensor': {'assigns': ['tok2vec'], 'requires': []}}}

# ya tenemos nuestro objeto, ahor tenemos que añadirle patrones que pueda matchear. recordemos que esto será entidades.
# Estos patrones siempre serán una lista de diccionarios

patterns = [
    {"label": "GPE", "pattern":"West Chesternfieldville"}
]

# Este patrón va a tomar West Chesternfieldville como uan entidad geoplolítica o lugar (GPE)
# Tenemos el patrón pero ahora debemos añadirlo al pipeline. 

ruler.add_patterns(patterns)

doc2 = nlp(text)
for ent in doc2.ents:
    print(ent.text, ent.label_)

# West Chesternfieldville PERSON
# Deeds PERSON

# Vemos que tenemos el mismo resultado ¿por qué? porque el orden del pipeline no es el correcto
# Tenemos dos opciones o situarlo antes en el pipeline o darle la capacidad de sobreescribir.
# La segunda opción es peligrosa puesto que nos arriesgamos a estropear extracciones ya realizadas.
# Por eso vamos a colocarlo primero en el pipeline.

nlp2 = spacy.load("en_core_web_sm")
ruler2 = nlp2.add_pipe("entity_ruler", before="ner")
ruler2.add_patterns(patterns)

# Repitiendo los mismos pasos podemos ver que el uso del parámetro before o after seguido de un
# componente del pipeline sitúa el elemento que hemos añadido antes o después del componente.

doc = nlp2(text)

for ent in doc.ents:
    print(ent.text,ent.label_)

# West Chesternfieldville GPE
# Deeds PERSON

# BAM!!! ahora funciona correctamente pero seguimos teniendo a Deeds como una persona y nosotros
# queremos que extraiga Mr.Deeds. Vamos a ver como solucionarlo

nlp3 = spacy.load("en_core_web_sm")
ruler3 = nlp3.add_pipe("entity_ruler", before="ner")
patterns_2 = [
    {"label": "GPE", "pattern":"West Chesternfieldville"},
    {"label": "Film", "pattern":"Mr. Deeds"}
]
ruler3.add_patterns(patterns_2)

doc3 = nlp3(text)

for ent in doc3.ents:
    print(ent.text,ent.label_)

# Madonna!! pure magic
# West Chesternfieldville GPE
# Mr. Deeds Film

# Ahora el problema que vemos es que Mr. Deeds es en realidad un topónimo pusto que puede
# ser tanto la película como un hombre con el apellido Deeds. Para resolverlo debemos ver
# el contexto, por eso un modelo de ML que pueda predecir a partir del contexto puede sernos 
# más útil aquí que la aproximación por reglas.