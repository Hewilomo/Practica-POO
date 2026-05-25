#ESTO AUN NO ES PROGRAMACION ORIENTADA AL OBJETO, SINO UN HIBRIDO ALEJADO DE LA MANO DE DIOS, terrible

#atributos
list_dic ={
        "nombre": "",
        "vida": "",
        "ataque": "",
        "inteligencia": "", 
        }

#metodos
def crear_personaje(nombre, vida, ataque, inteligencia):
    nuevo_char = input('Ingrese su nombre: ')
    list_dic["nombre"] = nuevo_char
    print(list_dic)

def elegir_clase(vida, ataque, inteligencia):
    while True:    
        eleccion_clase = input("""
        Escoja la clase que desea:
        1.- Mago
        2.- Guerrero
        3.- Arquero
        4.- Hewi
        """)
        if eleccion_clase == 1:
            list_dic["vida": 60, "ataque": 20, "inteligencia": 80]
            break
        elif eleccion_clase == 2:
            list_dic["vida": 100, "ataque": 80, "inteligencia": 20]
            break
        elif eleccion_clase == 3:
            list_dic["vida": 80, "ataque": 50, "inteligencia": 50]
            break
        elif eleccion_clase == 4:
            list_dic["vida": 800, "ataque": 10, "inteligencia": 5000]
            break
        else:
            print("Escoja una opción válida")

print(list_dic)






#En base a este ejemplo crear un menu de creación de personaje 
#Para practicar modificación de listas
#Chamuyar para que el ejercicio se vea mas complejo
#XOXO

#getter tu obtienes datos para modificarlos en ESA instancia
#setter tu privatizas los datos, haciendolos imposible de alterar y LEER si es que no lo permites
# Getter y Setter permiten Encapsular datos, esto permite que la persona solo pueda modificar PERSONAJE no base de datos
#GETTER Y SETTERS SON EXCLUSIVOS DE PROGRAMACIÓN ORIENTADA AL OBJETO (POO)