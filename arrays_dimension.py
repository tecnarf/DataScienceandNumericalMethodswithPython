"""
en python las matrices son arrays(arreglos)
una matriz es un arreglo de numeros en dos dimensiones
asi como un vector es un arreglo de numeros en una dimension
un array puede entenderse como una extension del concepto de matriz
teniendose entonces arreglos de numeros en 3 dimensiones hasta n dimensiones

la funcion array de numpy nos permite crear estos arreglos o matrices
cuando usamos dicha funcion se crea un objeto de tipo ndarray(un objeto de numpy)
"""

import numpy as np

escalar=np.array([1])#un escalar es una matriz 1x1 o areglo de dimension cero (lo podemos ver como un punto)
vector=np.array([1,2,3,4,5])#un vector fila es una matriz 1xn y un vector columna una matriz nx1
matriz=np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])#una matriz es como un vector de vectores
matriz_3d=np.array([[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]])
hiper_matriz=np.array([[[[[1, 2], [3, 4]], [[1, 2], [3, 4]]], [[[1, 2], [3, 4]], [[1, 2], [3, 4]]]], [[[[1, 2], [3, 4]], [[1, 2], [3, 4]]], [[[1, 2], [3, 4]], [[1, 2], [3, 4]]]]])
print("Escalar s = ", escalar)
print("Dimension: ", escalar.ndim)#las dimensiones de los array pueden obtenerse con el metodo ndim
print("Vector v = ", vector)
print("Dimension: ", vector.ndim)
print("Matriz M = ", matriz)
print("Dimension: ", matriz.ndim)
print("Matriz 3D = ", matriz_3d)
print("Dimension: ", matriz_3d.ndim)
print("Hiper Matriz 5D = ", hiper_matriz)
print("Dimension: ", hiper_matriz.ndim)

#se pueden crear hipermatrices incompletas poniendo ndim como
#parametro al crear la hipermatriz
arr = np.array([1, 2, 3], ndmin=7) 
 
print("Matriz incompleta: ", arr) 
print("Dimension: ", arr.ndim)






