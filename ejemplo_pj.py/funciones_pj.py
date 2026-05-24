char_class = {
    "nombre": "",
    "vida": "",
    "ataque": "",
    "dexteridad": "",
    "inteligencia": "",
}

def creacion_personaje(nombre, clase):
    nombre_pj = nombre
    clase_pj = clase
    
def clases(selección):
    if selección == 1: #Guerrero
        char_class["vida","ataque","dexteridad","inteligencia"] = 100,150,50,10
        pass
    elif selección == 2: #Arquero
        pass
    elif selección == 3: #Mago
        pass
    elif selección == 4: #Hewi
        pass
    else:
        print('Seleccione una opción valida')
    # return personaje