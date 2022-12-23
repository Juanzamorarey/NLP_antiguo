import re


texto = open("C:/Users/Juan/Desktop/Programación/NLP/Text_basics/texto_prueba.txt","r")
texto_leido = texto.read()


patron_telefono = r'\d{3}\s\d{3}\s\d{3}'

patron_dni = r'\d{8}\D'

patron_correo = r'\w+@\w+.com'

telefonos_en_texto = re.findall(patron_dni,texto_leido)
print(telefonos_en_texto)
# Con findall obtenemos una lista con todos los matches

for match in re.finditer(patron_dni,texto_leido):
    print(match.span())
# El metodo span() indica la posición de los matches pero si lo usamos fuera de un bucle for solo devolverá la primera posición
# COn el metodo finditer nos aparecen una serie de objetos que contienen el objeto encontrado ilegible, la posicion de inicio y final y el objeto
# impreso al final. Si solo quisiéramos obtener la posición de manera que pueda ser leída pondríamos un .span() al match del print.

telefonos_en_texto2 = re.search(patron_dni,texto_leido)
print(telefonos_en_texto2)
# El método search devuelve el primer match que haya en toda la cadena mientras que el metodo match devuelve solo el elemento si este comienza la cadena


