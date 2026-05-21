def menu():
    print('''
1.- Sumar
2.- Restar''')

def calculadora(numero1, numero2, opcion):
    if opcion == 1: #suma
        resultado = numero1 + numero2 
    elif opcion == 2: #resta
        resultado = numero1 - numero2
    return resultado
