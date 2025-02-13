import numpy #importamos la libreria o biblioteca numpy
             #la biblioteca de python dedicada a las matematicas
             #contiene muchas funciones matematicas y resulta
             #mucho mas practico manejar entidades matematicas como
             #vectores y matrices usando esta libreria
             #esta es la manera mas simple de importar una libreria en python

#dado que la matriz es el objeto matematico que engloba escalares y vectores
#pues todo escalar puede considerarse una matriz 1x1 y un vector ya sea fila
#o columna puede tratarse como una matriz 1xn o nx1
#comenzamos directamente a  ver como manejar esta entidad matematica en python


#creamos una matriz usando numpy
#para ello usamos la funcion array dentro de la libreria numpy
#para usar dicha funcion que pertenece a la libreria numpy
#debemos anteponer numpy. al nombre de la funcion
#se dice asi que se llama a la funcion array de numpy
miMatriz = numpy.array([1, 2, 3, 4, 5])#se trata de una matriz fila 1xn
                                       #o tambien conocido como vector (fila)
print(miMatriz)



