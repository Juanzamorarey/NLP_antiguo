# nuestro objetivo aquí es costruir un ner que idntifique nombres de fondos indexados o diferentes
# entidades como empresas.

import spacy 
import pandas as pd
# from spacy import displacy

df = pd.read_csv("stocks.tsv", sep="\t")
# sSetrata de un dataframe que está separado, en este caso por tabuladores.
# empezamos por ver nuestros datos

# print(df.head())
# print(df.tail())
#   Symbol            CompanyName                        Industry MarketCap
# 0      A   Agilent Technologies  Life Sciences Tools & Services    53.65B
# 1     AA                  Alcoa                 Metals & Mining     9.25B
# 2    AAC       Ares Acquisition                 Shell Companies     1.22B
# 3   AACG  ATA Creativity Global   Diversified Consumer Services    90.35M
# 4   AADI        Aadi Bioscience                 Pharmaceuticals   104.85M
#      Symbol              CompanyName                          Industry MarketCap
# 5874   ZWRK       Z-Work Acquisition                   Shell Companies   278.88M
# 5875     ZY                 Zymergen                         Chemicals     1.31B
# 5876   ZYME                Zymeworks                     Biotechnology     1.50B
# 5877   ZYNE  Zynerba Pharmaceuticals                   Pharmaceuticals   184.39M
# 5878   ZYXI                    Zynex  Health Care Equipment & Supplies   438.33M

# Así luce nuestro df. Necesitamos por tanto de este dataset crear nuestro extractor de entidades.
# A tal efecto nos interesan las columnas de symbol (el IDF del fondo o compañía) y el nombre 
# de la compañía.

# Empecemos por crear rápidamente una lsita con el contenido ed la columna symbol 
# y otra con los nombres

symbols = df.Symbol.tolist()
companies = df.CompanyName.tolist()
# print(symbols)
# print(symbols)

# Antes de crear toda una serie de features vamos a empezar por hacer este entity matcher

# nlp = spacy.blank("en")
# ruler = nlp.add_pipe("entity_ruler")
# patterns = []
# # recordemos que el ner utiliza una lita de diccionarios como argumetno.
# for symbol in symbols:
#     patterns.append({"label":"STOCK", "pattern":symbol})

# for company in companies:
#     patterns.append({"label":"COMPANY", "pattern":company})

# ruler.add_patterns(patterns)
# # Añadimos los nuevos patrones al ner
# with open ("text_example.txt") as f:
#     texto = f.read()

# doc = nlp(texto)

# for ent in doc.ents:
#     print(ent.text, ent.label_)

# Apple COMPANY
# Apple COMPANY
# Apple COMPANY
# Nasdaq COMPANY
# two COMPANY
# ET STOCK
# Nasdaq COMPANY
# JD.com COMPANY
# Kroger COMPANY
# Nasdaq COMPANY
# Nasdaq COMPANY

# Como hemos visto tenemos varios problemas. Si bien Apple ha sido extraída como una compañía,
# no lo ha sido como fondo. Al mismo tiempo aparece una compañía llamada two. La corrección 
# de este problema es compleja desde una aproximación con reglas como la que estamos tomando por lo que
# de momento debemos aceptar que ese two será un false positive. 

# Vamos a verlo mejor mediante displacy

# displacy.render(doc, style="ent")

# Al visualizarlo podemos ver que no hemos rescatado varias entidades. Vamos a fijarnos con
# propósito didáctico en una especialmetne. En nuestros datos aparece APPO.O como un fondo
# y no lo hemos extraído. 
# Al analizar nuestros datos vemos que existen una serie de nombres de fondos que tienen
# el siguiente patrón: IDF + . + LETRA MAYÚSCULA
# Una opción sería añadirlo a la lista pero es probable
# que en una lista no podamos guardar todos los nomrbes de los fondos, asi que lo que 
# vamos a hacer es crear un patrón que itere sobre las posibles letras mayúsculas.

# nlp = spacy.blank("en")
# ruler = nlp.add_pipe("entity_ruler")
# letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# patterns = []
# # recordemos que el ner utiliza una lita de diccionarios como argumetno.
# for symbol in symbols:
#     patterns.append({"label":"STOCK", "pattern":symbol})
#     for i in letras:
#         patterns.append({"label":"STOCK", "pattern":symbol+f".{i}"})
#     # Este segundo bucle va a mirar si nuestra entidad ya rescatada tiene el patrón
#     # que hemos encontrado en nuestros datos y a partir de ahí añadirlo como otra entidad

# for company in companies:
#     patterns.append({"label":"COMPANY", "pattern":company})

# ruler.add_patterns(patterns)
# # Añadimos los nuevos patrones al ner
# with open ("text_example.txt") as f:
#     texto = f.read()

# doc = nlp(texto)

# for ent in doc.ents:
#     print(ent.text, ent.label_)


# Apple COMPANY
# Apple COMPANY
# AAPL.O STOCK
# Apple COMPANY
# Nasdaq COMPANY
# two COMPANY
# ET STOCK
# Nasdaq COMPANY
# JD.com COMPANY
# TME.N STOCK
# NIO.N STOCK
# Kroger COMPANY
# KR.N STOCK
# Nasdaq COMPANY
# Nasdaq COMPANY

# Ahora hemos tenido mejores resultados rescatando los Stocks pero seguimos teniendo ruido. Por
# ejemplo esto:

# two COMPANY

# En este caso vamos a hace que "two" cuente como un stopword de modo que no sea extraído por el
# entity matcher. Echemos un vistazo a cómo añadir stopwords al pipeline:


nlp = spacy.blank("en")
ruler = nlp.add_pipe("entity_ruler")
letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
patterns = []
stopwords = ["two"]
# recordemos que el ner utiliza una lita de diccionarios como argumetno.
for symbol in symbols:
    patterns.append({"label":"STOCK", "pattern":symbol})
    for i in letras:
        patterns.append({"label":"STOCK", "pattern":symbol+f".{i}"})
    # Este segundo bucle va a mirar si nuestra entidad ya rescatada tiene el patrón
    # que hemos encontrado en nuestros datos y a partir de ahí añadirlo como otra entidad

for company in companies:
    if company not in stopwords:
        patterns.append({"label":"COMPANY", "pattern":company})

ruler.add_patterns(patterns)
# Añadimos los nuevos patrones al ner
with open ("text_example.txt") as f:
    texto = f.read()

# doc = nlp(texto)

# for ent in doc.ents:
#     print(ent.text, ent.label_)

# Apple COMPANY
# Apple COMPANY
# AAPL.O STOCK
# Apple COMPANY
# Nasdaq COMPANY
# ET STOCK
# Nasdaq COMPANY
# JD.com COMPANY
# TME.N STOCK
# NIO.N STOCK
# Kroger COMPANY
# KR.N STOCK
# Nasdaq COMPANY
# Nasdaq COMPANY

# Voila, two ya no se extrae. 

# Ahora mismo tenemos un modelo que fuciona bastante bien para extraer esos nombres de empresas
# o de IDF. Imaginemos que el cliente está tan contento que nos quiere pedir también los índices
# de los fondos. Para ello analizamos los documento y anotamos todos los índice en un excel
# que después importamos: 

df2 = pd.read_csv("indexes.tsv", sep="\t")

# Como siempre es conveniente visualizar nuestrod datos
# print(df2.head())
# print(df2.tail())



# Y vamos a repetir el mismo proceso creando un nueco componente que añadir al pipeline
indexes = df2.IndexName.tolist()
indexes_symbols = df2.IndexSymbol.tolist()

# ruler = nlp.add_pipe("entity_ruler")
# patterns_2 = []

# for index in indexes:
#     patterns_2.append({"label":"INDEX", "pattern":index})

# for indexSymbol in indexes_symbols:
#     patterns_2.append({"label":"DFA", "pattern":indexSymbol})

# ruler.add_patterns(patterns_2)

# doc = nlp(texto)

# for ent in doc.ents:
#     print(ent.text, ent.label_)

# Apple COMPANY
# Apple COMPANY
# AAPL.O STOCK
# Apple COMPANY
# Nasdaq COMPANY
# ET STOCK
# Dow Jones Industrial Average INDEX
# Nasdaq COMPANY
# JD.com COMPANY
# TME.N STOCK
# NIO.N STOCK
# Kroger COMPANY
# KR.N STOCK
# Nasdaq COMPANY
# Nasdaq COMPANY


# Nuestra lista contenía nombres de índices seguidos de la palabra index, ¿qué pasa con INDEX como
# por ejemlo el S&P 500 o el S&P 400 que no van seguidos de "index"?. Podemos hacer la presunción de que,
#  Las primeras palabras de un índice le permitan referenciarse a sí mismo. Es deicr:

# S&P 500 index (así aparece en la lista)
# Lo dividimos y decimos que S&P 500 puede autoreferenciarse sin ecesidad que en el texto
# aparezca S&P 500 index.


patterns_2 = []

for index in indexes:
    patterns_2.append({"label":"INDEX", "pattern":index})
    words = index.split()
    # DIVIDIMOS EL INDICE
    patterns_2.append({"label":"INDEX", "pattern":" ".join(words[:2])})
    # Creamos un aptrón que sea el nombre inicial del índice y los dos tokens a continuación que
    # para que el índice se autoreferencia.

for indexSymbol in indexes_symbols:
    patterns_2.append({"label":"DFA", "pattern":indexSymbol})

ruler.add_patterns(patterns_2)

# doc = nlp(texto)

# for ent in doc.ents:
#     print(ent.text, ent.label_)

# Apple COMPANY
# Apple COMPANY
# AAPL.O STOCK
# Apple COMPANY
# Nasdaq COMPANY
# S&P 500 INDEX
# S&P 500 INDEX
# ET STOCK
# Dow Jones Industrial Average INDEX
# S&P 500 INDEX
# Nasdaq COMPANY
# S&P 500 INDEX
# JD.com COMPANY
# TME.N STOCK
# NIO.N STOCK
# Kroger COMPANY
# KR.N STOCK
# Nasdaq COMPANY
# Nasdaq COMPANY

# Como vemos ahora estamos extrayendo índices que tienen varios componentes como el S&P 500 o
# el S&P 400. El ciente está suepr contento. Quiere encontrar también los stock exchanges 
# y nos pagará mucho mñas dinero.

# Repetimos el proceso. Analizamos el corpus, creamos una lsita en el excel y la añadimos:
# Nos interesa la descripción y la etiqueta de Gooogle.

df3 = pd.read_csv("stock_exchanges.tsv", sep="\t")
exchanges = df3.ISOMIC.tolist() + df3["Google Prefix"].tolist() + df3.Description.tolist()
# Este df está organizado de forma diferente pero recordemos que siempre deberemos convertir
# las entidades a una lista.

patterns_3 = []

for e in exchanges:
    patterns_3.append({"label":"STOCK_EXCHANGE", "pattern":e})

ruler.add_patterns(patterns_3)

doc = nlp(texto)

for ent in doc.ents:
    print(ent.text, ent.label_)

# Apple COMPANY
# Apple COMPANY
# AAPL.O STOCK
# Apple COMPANY
# Nasdaq COMPANY
# S&P 500 INDEX
# S&P 500 INDEX
# ET STOCK
# Dow Jones Industrial Average INDEX
# S&P 500 INDEX
# Nasdaq COMPANY
# S&P 500 INDEX
# JD.com COMPANY
# TME.N STOCK
# NIO.N STOCK
# Kroger COMPANY
# KR.N STOCK
# NYSE STOCK_EXCHANGE
# Nasdaq COMPANY
# Nasdaq COMPANY


# Vamos a dejar aquí el ejercicio, si bien se podría refinar aún más utilizando stopwrods, 
# componentes añadidos al pipeline y otros elementos que podrían llevar aún más all`´a las extracciones las cuals están 
# actualmente a un 90% aproximadamente.`