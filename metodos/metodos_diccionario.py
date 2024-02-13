dicc = {
    "nombre" : "mar",
    "edad" : 18,
    "casada" : False,
}

# KEY
clave = dicc.keys()
print (clave)
#devuelve las palabras claves de cada elemento en el diccionario

# GET
valor = dicc.get("casada")
print (valor)
#devuelve el elemento dentro de la key en el diccionario
#si no lo encuentra devuelve "none" indicando que no tiene ningun elemento

#POP
dicc.pop("edad")
print(dicc)
#elimina un valor especifico dentro del diccionario

#ITEMS
iteracion_dicc = dicc.items()
print(iteracion_dicc)
#devuelve una lista donde podremos iterar sobre los elementos
    
#CLEAR
dicc.clear()
print(dicc)
#elimina los valores del diccionario

