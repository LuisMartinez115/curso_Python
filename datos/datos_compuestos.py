#enlistado
lista = ["altura","base",False,18]
lista[3] = "nuevo" #esto es válido
#una lista se puede modificar
print(lista[3])
#tupla 
tupla = ("altura","base",False,18)
#tupla[3] = "nuevo"  esto no es válido
#una tupla no se puede modificar
print(tupla[3])
#conjunto (set)
conjunto = {"altura","base",False,18}
#conjunto[1] = "otra cosa"
#un conjuto no se puede modificar y no se puede acceder mediante un indice
#no almacena datos duplicados
#conjunto = {"altura","base",False,18,"altura"} <- no es valido 

#--------------------------------------------------------------------------------------------------
#creando un diccionario
diccionario = {
    'a' : "altura",
    'b' : "base",
    'bool' : False,
    'edad' : 18,
}
print(diccionario['edad'])