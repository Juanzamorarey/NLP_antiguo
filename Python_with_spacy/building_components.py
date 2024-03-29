import spacy
import re

nlp = spacy.load("en_core_web_md")
doc = nlp("Britain is a place. Mary is a doctor")

for ent in doc.ents:
    print(ent.text, ent.label_)

# Imaginemos que nos piden extraer los lugares con la etiqueta LOC de location. Para ello
# vamos a crear nuestro propio componente. Empecemos por importar language

from spacy.language import Language
# Ahora nombrarmos a nuestro nuevo componente
@Language.component("remove_gpe")
# Y creamos una función que borre los ents de tipo GPE
def remove_gpe(doc):
    original_ents = list(doc.ents)
    for ent in doc.ents:
        if ent.label_ == "GPE":
            original_ents.remove(ent)
    doc.ents = original_ents
    return (doc)

nlp.add_pipe("remove_gpe")

doc = nlp("Britain is a place. Mary is a doctor")

for ent in doc.ents:
    print(ent.text, ent.label_)

# Ahora vamos a empezar a aplicar regex a nuestros propios componentes:

text_2 = "Tis is a sample number (555) 555-5555."

nlp_2 = spacy.blank("en")

ruler = nlp_2.add_pipe("entity_ruler")
# Es importante recordar que las regex solo funcionan con tokens individuales y no con multiples tokens
# patterns = [
#     {
#         "label":"PHONE_NUMBER",
#         "pattern":[
#             {
#                 "TEXT":{"REGEX": "(\d{3}-(\d{4})"}
#             }
#         ]
#     }
# ]

# El anterior pattern no funcionará porque se trata de un pattern que toma más de un token

text = "Paul Newman was an American actor. Paul Hollywood is a british TV host. Paul is a very common name"

pattern = r"Paul [A-Z]\w+"

# Vamos a ir importando varias cosas

from spacy.tokens import Span

nlp = spacy.blank("en")

# Creamos el multi word tokens entity
doc = nlp(text)
mwt_entity = []
original_ents = list(doc.ents)

for match in re.finditer(pattern,doc.text):
    start, end = match.span()
    span = doc.char_span(start,end)
    print(span)

# Paul Newman
# Paul Hollywood

# tenemos que crear así este bucle porque si bien la regex mira al inicio y final 
# de la cadena de caracteres que se está extrayendo spacy actúa a nivel de token. 
#  La función "char_span" de spacy nos sirve para convertir tokens a caracteres 
# y poder así utilizar el span que devuelva a la regex. Siendo así ahora que tenemos
# rescatadas las posiciones necesitamos asignarlas coo entidades, para ello
# las convertimos en una tupla:

for match in re.finditer(pattern,doc.text):
    start, end = match.span()
    span = doc.char_span(start,end)
    # Aquí span lo convierte a posiciones de token y no caracteres
    if span is not None:
        mwt_entity.append((span.start, span.end, span.text))
    print(mwt_entity)

# [(0, 2, 'Paul Newman'), (7, 9, 'Paul Hollywood')]
# Voila ahi tenemos la tupla con los tokens que contiene la entidad, y su texto
# Ahora debemos incorporarlas a nuestras entidades y a nuestro pipeline.
for ent in mwt_entity:
    start, end, name = ent
    # Aquí creamos la entidad individual y ahora llamamos a la clase Span de spacy
    # Esta clase toma como argumento el objeto doc de spacy
    #  las posiciones que tenemos en nuestra tupla y una etiqeuta
    per_ent = Span(doc, start, end, label= "PERSON")
    # Y ahora lo introducimos en nuestras entidades originales
    original_ents.append(per_ent)
# Y finalmente asignamos a doc.ents la lista con las nuevas entidades.
doc.ents = original_ents
print (doc.ents)
# (Paul Newman, Paul Hollywood)
# BAM

# Pero ¿cómo podemos introducir esto en nuestro propios componentes? 
