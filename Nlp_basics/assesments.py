import spacy

nlp = spacy.load ('en_core_web_sm')


with open ('../NLP/UPDATED_NLP_COURSE/TextFiles/owlcreek.txt') as f:
    doc = nlp(f.read())

# print(len(doc))

# phrase_list = []

frases = [sent for sent in doc.sents]

print(len(frases))


# for i in doc.sents:
#     phrase_list.append(i)

# print(len(phrase_list))    

print(frases[2])

# doc2 = nlp(frases[2])

for i in frases[2]:
    print(f'{i.text:{12}}{i.pos_:<{10}}{i.dep_:<{10}}{i.lemma_}')
    

