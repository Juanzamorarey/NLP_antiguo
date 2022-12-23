# En esta parte vamos a ver la visualización de todos los datos que antes se mostraban por consola para que sean mas fáciles de 
# interpretar por parte del usuario. 
# Para ello vamos a usar la libreria displacy, que se vale de tkinter para mostrar los datos con los que estamos trabajando. 

from spacy import displacy
import spacy
nlp = spacy.load('en_core_web_sm')

# Displacy es la parte visual de spacy, vamos a ver como funciona:

doc = nlp(u"Apple is going to build a U.K. factory for 46 million.")

# A la hora de usar displacy tenemos dos opciones. La primera es, ejecutando el metodo .serve() el cual admite diferentes parámetros. 
# Si usamos este metodo se abrirá un servidor propio desde el ordenador que tendrá nuestro display. http://localhost:5000/
# Otra opción es usar el método render que creará directamente el pdf. 
# Para ver los parámetros de displacy: https://spacy.io/api/top-level#displacy.serve

displacy.serve(doc,style='dep',options={'distance':100})

# print(displacy.render(doc,style='dep',options={'distance':50}, page=True))
# print(spacy.displacy.render(doc, style="dep", page="true"))

# Además del estilo dep, que ejecuta las dependencias sintácticas, tenemos otro estilo que ejecuta las entidades:


# doc2 = nlp(u"Over the last quarter Apple sold nearly 20 thousands iPods for a profit of 6$ million.")

# displacy.serve(doc2,style='ent')



