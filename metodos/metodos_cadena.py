cadena1 = "hola, ¿como estas?"
cadena2 = "ESTAMOS PERDIDAAAAASSS"

#dir
print(dir(cadena1)) #esto es una funcion
# devuelve todos los posibles atributos para ese objeto

#-------------------------------------------------------------------------------------

#UPPER 
print(cadena1.upper()) #esto es un metodo
#devuelve toda la cadena en mayuscula

#LOWER
print(cadena2.lower())
#devuelve toda la cadena en minuscula

#CAPITALIZE
print(cadena1.capitalize()) #esto es un metodo
#devuelve la primer letra de la cadena en mayuscula

#----------------------------------------------------------------------------------------

#FIND
print(cadena1.find("hola"))
#devuelve la posicion de lo que se busca, retornando un numero

#INDEX
print(cadena1.index("hola"))
#devuelve la posicion de lo buscado, si no hay coincidencia retorna una ecepcion 

#----------------------------------------------------------------------------------------

#ISNUMERIC
print(cadena2.isnumeric())
#retorna true si es un valor nuerico, false si no lo es

#ISALPHA
print(cadena1.isalpha())
#devuelve true si solo es una cadena con letras (Aa-Zz), sin caracteres especiales

#--------------------------------------------------------------------------------------------

#COUNT
print(cadena1.count("hola"))
#develve la cantidad de coinciencias de una cadena dentro de otra cadena

#LEN
print(len(cadena2))
#cuenta la cantidad de caracteres tiene una cadena

#--------------------------------------------------------------------------------------------

#ENDSWITH
print(cadena1.startswith("hola"))
#devuelve true si la cadena empieza con la cadena dada

#STARTSWITH
print(cadena1.endswith("?"))
#devuelve true si la cadena termina con la cadena dada

#--------------------------------------------------------------------------------------------

#REPLACE
print(cadena1.replace("hola","holiwis"))
#remplaza el valor 1 por el valor 2, si se encuentran coincidencias

#SPLIT
print(cadena1.split(" "))
#devuelve una lista, separados por el parametro dado
