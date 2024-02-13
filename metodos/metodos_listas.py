#LIST
lista = list(["lucas","dalto","mar","amor"])
#funciona para crear una lista (normalmente vacía)
#--------------------------------------------------------------------------------------------

#LEN
cantidad_elementos = len(lista)
print(cantidad_elementos)
#devuelve la cantidad de elementos en la lista
#--------------------------------------------------------------------------------------------

#APPEND
lista.append("cariño")
print(lista)
#agrega un elemento al final de la lista

#INSERT
lista.insert(2,"definicion")
print(lista)
#agrega un elemento en el indice indicado

#EXTEND
lista.extend(["definicion",False,True,"luis"])
print(lista)
#agrega una lista a otra lista
#--------------------------------------------------------------------------------------------

#POP
lista.pop(1)
print(lista)
#elimina el elemento en el indice dado
lista.pop(-1)
print(lista)
#el signo elimina el elemento de derecha a izquierda

#REMOVE
lista.remove("definicion")
print(lista)
#elimina el primer elemento que tenga coincidencia

#CLEAR
lista.clear
print(lista)
#elimina todos los elementos de la lista
#--------------------------------------------------------------------------------------------
lista = list([65,3,2,33,True,False])
#SORT
lista.sort()
print(lista)
#ordena de forma asendente los elementos de la lista 

#REVERSE
lista.reverse()
print(lista)
#invierte el orden de la lista original, el primero pasa a ser el ultimo y sucesivamente


