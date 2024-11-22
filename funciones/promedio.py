"""
Cree una funcion que calcule el promedio de N notas
"""
def calcular_promedio():
    suma = 0
    cantidad = 0
    print("Ingrese cada nota una por una. Escriba 'fin' para terminar.")

    while True:
        entrada = input("Ingrese una nota o 'fin' para terminar: ")
        
        if entrada.lower() == 'fin':
            break
        
        try:
            nota = float(entrada)
            suma += nota
            cantidad += 1
        except ValueError:
            print("Por favor, ingrese una nota válida.")
    
    if cantidad > 0:
        promedio = suma / cantidad
        print(f"El promedio de las notas ingresadas es: {promedio}")
    else:
        print("No se ingresaron notas válidas.")

calcular_promedio()

