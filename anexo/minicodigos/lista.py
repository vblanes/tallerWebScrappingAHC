# Manera sencilla de definir listas
lista_vacia1 = list()
# o equivalentemente
lista_vacia2 = []
# tambien podemos inicializarla con algunos valores
primos = [2,3,5,7,9,11]
# en python las listas pueden contener elementos de distintos tipos
# una lista puede contener elementos 'complejos' como otras listas
lista_heterogenea = ['Hola que tal', 42, primos]

# podemos acceder a los elementos de una lista usando []
print(primos[2])
# obtenemos el TERCER elemento y lo mostramos por pantalla
# tambien funciona con indices negativos
print(primos[-1]) #mostraria el ULTIMO elemento


# append anyade un elemento al final de la lista
primos.append(13)
# el estado de la lista 'primos' seria el siguiente
# [2,3,5,7,9,11,13]

# insert requiere dos argumentos, la posicion donde insertar y el elemento
primos.insert(0, 1)
# insertamos el 1 en la primera posicion desplazando el resto
# [1,2,3,5,7,9,11]

# dos formas sencillas de borrar
#1) si conocemos el elemento que queremos eliminar
primos.remove(1) #borra la primera aparicion de 1 en la lista
#2) si conocemos su indice
primos.pop(0) #borrar y duelve el valor en el indice 0
# con cualquiera de los [2,3,5,7,9,11]
