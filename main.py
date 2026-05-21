import funciones as fun

while True:
    print('Bienvenido a la calculadora magica!')
    primer_numero = int(input('Por favor ingrese su primer numero!: '))
    segundo_numero = int(input('Por favor ingrese su segundo numero!: '))

    fun.menu()
    decision = int(input('Por favor escoja la opción que desea: '))
    respuesta, operacion, adjetivo = fun.calculadora(primer_numero,segundo_numero,decision)
    print(f'{primer_numero} {operacion} {segundo_numero} = {respuesta}, {adjetivo if adjetivo else ""}')