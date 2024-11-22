"""
Cree una funcion que determine si un color es primario o no, se debe imprimir por
pantalla la leyenda “el color X es primero “ o “el color X no es primario”
"""
def color_analizar(color):
    color = color.lower()
    if color == "rojo" or color == "azul" or color == "amarillo":
        print(f"El color {color} es primario.")
    else:
        print(f"El color {color} no es primario.")

color_ingresado = input("ingresar el color a evaluar " )

color_analizar(color_ingresado)

