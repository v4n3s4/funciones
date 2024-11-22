"""
Cree una funcion que determine que numero de una serie de N numeros es mayor

"""

def numero_mayor():
    entrada = input("Por favor, ingrese una serie de números separados por comas: ")
    numeros = entrada.split(',')


    mayor = int(numeros[0])
    
    
    for num in numeros:
        numero = int(num)
        if numero > mayor:
            mayor = numero
    
    print(f"El número mayor de la serie es: {mayor}")

numero_mayor()






