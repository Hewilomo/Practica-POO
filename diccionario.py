#ESTO AUN NO ES PROGRAMACION ORIENTADA AL OBJETO, SINO UN HIBRIDO ALEJADO DE LA MANO DE DIOS

#atributos
list_dic ={
        "nombre": "",
        "vida": "",
        "ataque": "",
        "inteligencia": "", 
        }

#metodos
def crear_personaje(nombre, vida, ataquem, intelgiencia):
    nuevo_char = input('Ingrese su nombre: ')
    list_dic["nombre"] = nuevo_char
    print(list_dic)

#En base a este ejemplo crear un menu de creación de personaje 
#Para practicar modificación de listas
#Chamuyar para que el ejercicio se vea mas complejo
#XOXO

#getter tu obtienes datos para modificarlos en ESA instancia
#setter tu privatizas los datos, haciendolos imposible de alterar y LEER si es que no lo permites
# Getter y Setter permiten Encapsular datos, esto permite que la persona solo pueda modificar PERSONAJE no base de datos
#GETTER Y SETTERS SON EXCLUSIVOS DE PROGRAMACIÓN ORIENTADA AL OBJETO (POO)