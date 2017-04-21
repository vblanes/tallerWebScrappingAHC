# crear un diccionario vacio
dicc_vacio1 = dict()
# otra manera
dicc_vacio2 = {}
# crear un diccionario con algunos elementos ya
dicc_edades = {'Vicent' : 24, 'Maria' : 20, 'Damian' : 47}

# recuperar un valor es similar al metodo usado en listas
# solo que en lugar de un indice escribimos su clave
print(dicc_edades['Vicent'])
# esto nos pintaria por pantalla: 24

# anyadir es muy sencillo
dicc_edades['Encarna'] = 50

# si quisieramos eliminar una entrada del diccionario
del dicc_edades['Damian']


# se puede obtener tanto la lista de claves existentes
# en un diccionario como la lista de valores
claves = dicc_edades.keys()
valores = dicc_edades.values()
