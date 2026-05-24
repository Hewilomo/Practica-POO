class Usuario:

    def __init__(self,nombre = "", passwd = "", rol = "empleado"):
        self.nombre = nombre
        self.passwd = passwd
        self.rol = rol

    def registrar(self):
        nombre_usuario = input("Por favor ingrese su nombre de usuario: ")
        passwrd = input("Por favor ingrese la contraseña que desea: ")
        rol: 