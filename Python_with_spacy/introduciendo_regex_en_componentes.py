import spacy 
from spacy.language import Language
from spacy.tokens import Span
import re
from spacy.util import filter_spans

nlp = spacy.blank("en")
text = "Paul Newman was an American actor. Paul Hollywood is a british TV host. Paul is a very common name"
doc = nlp(text)



@Language.component("Paul_ner")
def Paul_ner(doc):
    pattern = r"Paul [A-Z]\w+"
    mwt_entity = []
    original_ents = list(doc.ents)

    for match in re.finditer(pattern,doc.text):
        start, end = match.span()
        span = doc.char_span(start,end)
        # Aquí span lo convierte a posiciones de token y no caracteres
        # char_span viene en la libreria from spacy.tokens import Span
        if span is not None:
            mwt_entity.append((span.start, span.end, span.text))
        print(mwt_entity)

    for ent in mwt_entity:
        start, end, name = ent
        # OJO: name es necesario es el span.text
        per_ent = Span(doc, start, end, label= "PERSON")
        # Y ahora lo introducimos en nuestras entidades originales
        original_ents.append(per_ent)
    doc.ents = original_ents
    return(doc)  

# Ahora mismo tenemos preparado un componente que utiliza regex para extraer el nombre
# Paul en un texto. Vamos a crear un pipeline vacío y añadirle nuestro componente para testarlo
# a ver qué tal funciona

nlp_2 = spacy.blank("en")
nlp_2.add_pipe("Paul_ner")

# Vamos a probarlo con nuestro mismo texto

doc2 = nlp_2(text)
print(doc2.ents)
# (Paul Newman, Paul Hollywood)

# Equilicua aquí están nuestras dos entidades rescatadas con el Paul_ner

# Pero qué pasa si queremos introducit nuestro componente en un modelo ya creado?
# Vamos a crear un nuevo componente que busque solo Hollywood y lo extraiga como CINEMA
# Si corriéramos esto sin más habría un error porque tenemos 2 entidades 
# que se superponen. En spacy esto siempre nos dará un error. Para ello debemos usar el filter
# spans el cual se debe importar como aparece en la parte superior. filter spans permite filtrar
# Vamos a añadir la línea de código y explicarla abajo

@Language.component("cinema_ner")
def cinema_ner(doc):
    pattern = r"Hollywood"
    mwt_entity = []
    original_ents = list(doc.ents)

    for match in re.finditer(pattern,doc.text):
        start, end = match.span()
        span = doc.char_span(start,end)
        # Aquí span lo convierte a posiciones de token y no caracteres
        if span is not None:
            mwt_entity.append((span.start, span.end, span.text))
        print(mwt_entity)

    for ent in mwt_entity:
        start, end, name = ent
        per_ent = Span(doc, start, end, label= "CINEMA")
        # Y ahora lo introducimos en nuestras entidades originales
        original_ents.append(per_ent)
    filtered = filter_spans(original_ents)
    # ¿Qué hace esto? recorre todos los inicios de las entidades rescatadas y, en caso de 
    # superposicion otorga relevancia al token más largo.
    doc.ents = filtered
    return(doc)

nlp3 = spacy.load("en_core_web_sm")
nlp3.add_pipe("cinema_ner")
doc2 = nlp3(text)
print(doc2.ents)

# (Paul Newman, American, Paul Hollywood, british)

# A la vista del output podemos declarar que nuestro arreglo funciona puesto que 
# Paul Hollywood es un token mayor que únicamente Hollywood de modo que se da relevancia a
# este sobre Holywood