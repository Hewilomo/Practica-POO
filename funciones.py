def menu():
    print('''
1.- Sumar
2.- Restar
3.- Multiplicar
4.- Dividir''')

def calculadora(numero1, numero2, opcion):
    if opcion == 1: #suma
        resultado = numero1 + numero2
        operacion = "+" 
        adjetivo = "Sopenco"
    elif opcion == 2: #resta
        resultado = numero1 - numero2
        operacion = "-"
        adjetivo = "Aweonao"
    elif opcion == 3: #multiplicación
        resultado = numero1 * numero2
        operacion = "x"
    elif opcion == 4: #división
        resultado = numero1 / numero2
        operacion = "/"

    return resultado, operacion, adjetivo
