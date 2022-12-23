# VAmos a leer y escribir en archivos de texto usando python. 
# Para crear un archivo de texto en python tenemos que hacer lo siguiente:

# To create a new file in Python, use the open() method, with one of the following parameters:

# "x" - Create - will create a file, returns an error if the file exist

# "a" - Append - will create a file if the specified file does not exist

# "w" - Write - will create a file if the specified file does not exist
# Example

# Create a file called "myfile.txt":
# f = open("myfile.txt", "x")

# Result: a new empty file is created!
# Example

# Create a new file if it does not exist:
# f = open("myfile.txt", "w")

# Aquí tenemos una serie de comandos para crearlos a partir del metodo open. Siendo así usaríamos este código para crear un archivo de texto:

# texto = open("test.txt", "x") LO COMENTAMOS PARA NO CREAR UN SEGUNDO DOCUMENTO DE TEXTO


# To write to an existing file, you must add a parameter to the open() function:

# "a" - Append - will append to the end of the file

# "w" - Write - will overwrite any existing content
# Example

# Open the file "demofile2.txt" and append content to the file:
# f = open("demofile2.txt", "a")
# f.write("Now the file has more content!")
# f.close()

# #open and read the file after the appending:
# f = open("demofile2.txt", "r")
# print(f.read()) 

# Siguiendo estas directrices para escribir en un archivo de texto podemos modificarlo desde nuestro código python 

# texto_modo_escritura = open("test.txt", "w")
# texto.write("Ahora el txt no está vacío")
# texto.close()

# texto_modo_lectura = open("test.txt","r")
# print(texto_modo_lectura.read())

# COMENTAMOS TODo LO ANTERIOR PARA PODER CONTINNUAR CON LA LECCIÓN
# Debemos por lo tanto crear una variable que tratará el texto en el modo en el que queremos y después operar con dicha variable. 
# Es importante saber la localización de los archivos cuando trabajamos con archivos externos. 
# Si quieres abrir un archivo que está en un path diferente en el que estás trabajando deberás
#  usar el método open() y poner toda la ruta con \ si estás en windows.


# Este metodo de lectura nos sirve para ver el texto, pero no para trabajar con él. En NLP muchas veces necesitaremos trabajar con grandes 
# volúmenes de texto de modo que nos interesará segmentarlo quizá por líneas o por palabras. Para ello usaremos otro modo de lectura:

# myfile = open('test.txt')
# f = myfile.readlines()
# print(f)

# El metodo readlines nos permite ver el texto como una lista que separa cada línea a partir del \n que indica una nueva línea. De este modo
# podemos ahora iterar sobre nuestra lista como sobre cualquier otra lista en python: 

# for line in f:
#     print(line[0])

# En este caso imprimimos la primera letra
# o con el metodo split() podemos separar las líneas e imprimir las palabras por separado:

# for line in f:
#     print(line.split()[0])

# El metodo split() sirve para separar los strings a partir de los espacios, por lo que nos sirve para separar.

# myfile = open('test.txt','w+')
# f= myfile.read()
# print(f)
# El modo 'w+' con open hace que al abrir el texto se sobreescriba todo lo que haya en el texto concreto. Por lo que al abrirlo se elimina todo en el archivo

# myfile.write('Mi nuevo texto \n lo peta')
# myfile.seek(0)
# f= myfile.read()
# print(f)
# Como vemos aquí el texto anterior ha desaparecido y ahora tenemos un nuevo texto que hemos creado con el metodo write. es importante remarcar
# que el .seek() lo tenemos que utilizar porque no se ha guardado en ninguna variable el texto nuevo. COMENTAMOS AHORA TOdo LO ANTERIOR
# para ver como adjuntar cosas a un texto

# myfile = open('test.txt','a+')
# myfile.write('\nratamajata majata rakata\n regueton bien duro papasito con el culo')
# myfile.close()

# Es importante que tras cada modificación debemos cerrar el texto y volver a abrirlo lo que significa una nueva variable y más codigo.

# newfile = open('test.txt','r')
# f = newfile.read()
# print(f)

# Ahora que hemos entendido los diferentes modos y como usarlos podemos ver que el metodo close() cada vez hace que sea complicado operar con ellos
# para evitar esto usamos lo que se llama un administrador de texto que no es más que un pequeño bloque de texto en el que podemos operar en un modo
# todo lo que queramos:

with open('test.txt','r') as mynewfile:
    myvariable = mynewfile.readlines()

# Aquí estamos en un bloque de código que lee el archivo que queremos en el modo deseado y, dentro del bloque del with podemos operar todo
# lo que queramos sin tener que preocuparnos por cerrar después el archivo. 

print(myvariable)



