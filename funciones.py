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

def calculadora_notas():
    nota1 = float(input("Ingrese su primera nota: "))
    nota2 = float(input("Ingrese su segunda nota: "))
    nota3 = float(input("Ingrese su tercera nota: "))

    resultado = (nota1 + nota2 + nota3) / 3
    print(f"""El promedio de sus notas:
{nota1}
{nota2}
{nota3}          
promediadas resultan en: {resultado: .1f}""")
    if resultado < 4.0:
        print("Usted reprobó")
    else:
        print("Usted aprobó!")
    return resultado    