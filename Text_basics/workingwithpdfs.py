# Normamente vamos a trabajar mas con archivos pdf que con artchivos .txt
# para leerlos vamos a usar la libreria PyPDF2 aunque es importante decir que no todos los pdfs tienen texto extraible. 
# Algunos de estos pdfs están creados con escaner y son mas una imagen que un pdf lo que requiere software especializado 
import PyPDF2

# Importamos la libreria para trabajar con el pdf

# myfile = open('US_Declaration.pdf',mode='rb')

# Es importante que el pdf esté en la misma carpeta que el archivo python, sino no funcionará porque no se detecta en el path


# pdf_reader = PyPDF2.PdfFileReader(myfile) 


# Creamos una variable a la que, usando el PyPDF2 le establecemos un metodo, en este caso PdfFileReader y como argumento pasamos la variable que contiene
# el texto en pdf, recordemos que para leer este texto hay que abrirlo en modo binario ('rb')

# numero_de_paginas = pdf_reader.numPages

# pagina_uno = pdf_reader.getPage(0)

# texto_completo_pagina_uno = pagina_uno.extractText()

# Cuando tenemos el archivo leido en la variable pdf_reader podemos usarla con los metodos de la libreria PyPDF2 para ver el numero de paginas, coger una
# página determinada o extraer el texto completo
# Recordemos que es importante cerrar el documento una vez que hemos acabado de trabajar con el

# myfile.close()

# No se pueden escribir strings directamente en un pdf, pero podemos copiar paginas y añadirlas al final, por supuesto en formato pdf. 
# Vamos a añadir una pagina a un pdf.

# f = open('US_Declaration.pdf', mode ='rb')

# texto_completo = PyPDF2.PdfFileReader(f)

# first_page = texto_completo.getPage(0)

# Hasta aquí todo es igual, hemos abierto en binario el texto, después en una variable hemos usado PyPDF2 para poder trabajar con él y hemos cogido la
# primera página.

# pdf_writer = PyPDF2.PdfFileWriter()

# pdf_writer.addPage(first_page)


# Ahora hemos creado una nueva variable que contiene un objeto para escribir en un pdf y la hemos llamado pdf_writer, y le hemos añadido la
# primera pagina dando después otra variable que contiene el output, el cual crea un nueva pdf al ponerlo en el modo escritura binaria.
# Este pdf ahora mismo está vacío pero lo vamos a completar con lo que hemos hecho antes.

# nuevo_pdf = open('MY_BRAND_NEW.pdf','wb')

# pdf_writer.write(nuevo_pdf)

# En el objeto escritura habíamos almacenado la primera página y ahora la hemos volcado en el nuevo_pdf, el cual hemos abierto en modo escritura binaria

# nuevo_pdf.close()
# f.close()

# Cerramos de nuevo el documento nuevo y el original. Para comprobar que todo ha funcionado comprobamos que el pdf creado tenga solo 1 página.

# brand_new = open('MY_BRAND_NEW.pdf','rb')

# pdf_reader=PyPDF2.PdfFileReader(brand_new)
# print(pdf_reader.numPages)


# Vamos a hacer una última demostración de como coger todo el texto de un pdf y leerlo

f = open('US_Declaration.pdf','rb')

pdf_text = []
# Creamos una lista vacía que nos sirve de almacenamiento

pdf_reader = PyPDF2.PdfFileReader(f)

for p in range(pdf_reader.numPages):
    page = pdf_reader.getPage(p)

    pdf_text.append(page.extractText())

# Este bucle hace que en el rango del numero de páginas del texto una página va a ser el texto del cual cogemos la página con el iterable como argumento
# y en la lista vacía añadimos esa página, de modo que almacenará al final del bucle todas las páginas del texto. 
# Por último cerramos el arhivo

f.close()

for page in pdf_text:
    print(page)
    print('\n')
    print('\n')
    print('\n')
    print('\n')

# Aquí podemos ver las páginas separadas con varios espacios