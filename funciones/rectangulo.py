"""
Cree una funcion que dibuje un rectangulo de X filas y X columnas determinadas por el
usuario
"""
def dibujar_rectangulo(filas, columnas):
    for i in range(filas):
        print('*' * columnas)

filas = int(input("Ingrese el número de filas: "))
columnas = int(input("Ingrese el número de columnas: "))


dibujar_rectangulo(filas, columnas)
