import funciones as fun


print('Bienvenido a la calculadora magica!')
primer_numero = int(input('Por favor ingrese su primer numero!: '))
segundo_numero = int(input('Por favor ingrese su segundo numero!: '))
while True:
    fun.menu()
    decision = int(input('Por favor escoja la opción que desea: '))
    respuesta = fun.calculadora(primer_numero,segundo_numero,decision)
    print(f'El resultado de su operacion de {primer_numero} con {segundo_numero} = {respuesta}')