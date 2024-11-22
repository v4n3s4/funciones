""""
Cree una funcion que calcule el Factorial de un numero entero positivo
"""
def factorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

numero = int(input("Ingrese un número entero positivo: "))
if numero >= 0:
    print(f"El factorial de {numero} es {factorial(numero)}.")
else:
    print(" Ingrese un número entero positivo.")
