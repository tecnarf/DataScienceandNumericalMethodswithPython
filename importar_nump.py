#escribir numpy antes de cada funcion que vayamos a utilizar puede
#resultar poco practico, por lo que se tiene alternativas para evitar esto
#una de ellas es mediante el uso de un alias (nombrarlo por un nombre mas corto)
#o usar *

import numpy as np #importamos la libreria o biblioteca numpy con un alias
                   #mucho mas practico que escribir siempre numpy antes de usarsus funciones


#creamos una matriz usando numpy
#para ello usamos la funcion array dentro de la libreria numpy
#para usar dicha funcion que pertenece a la libreria numpy
#ahora solo debemos anteponer np. al nombre de la funcion
#se dice asi que se llama a la funcion array de numpy
miMatriz = np.array([[5, 4, 3, 2, 1], [1, 2, 3, 4, 5]])#se trata de una matriz fila 2x5
print(miMatriz)
print(type(miMatriz))#vemos el tipo de la variable 

"""
Otra forma de ahorrarnos escribir el nombre de la libreria es usar *
pero su uso no es recomendado en caso de que se importe mas de una libreria

from numpy import *

miMatriz=array([1,2,3,4,5])

print(miMatriz)

"""



