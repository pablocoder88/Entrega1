
base={}

def menu():

    while True:    

        print("""
        1-Cargar nombre de usuario
        2-iniciar sesion con usuario
        3-Mostrar usuarios
        4-Salir""")
        tarea=int(input("        Que deseas hacer?: "))

        if tarea==1:
                alta()
        elif tarea==2:
                inicio()
        elif tarea==3:
                print(base)
        else:
                print("Hasta luego")
                break
        
def alta():
        
        usuario=str(input("ingrese un nombre de usuario de entre 4 y 8 caracteres: "))
        while usuario in base:
                        usuario=str(input("el usuario ya existe, escriba otro: "))
        while len(usuario)>8 or len(usuario)<4:
                usuario=str(input("el usuario debe tener entre 4 y 8 caracteres, ingrese otro: "))                                
                                                
        contrasena=str(input("ingrese una contrasena que tenga entre 6 y 12 caracteres: "))
        
        while len(contrasena)>12 or len(contrasena)<6:
                contrasena=str(input("la contrasena debe tener entre 6 y 12 caracteres, ingrese otra: "))
        confi=str(input("confirma tu contraseña: "))
        intentos=3
        while confi!=contrasena:
                intentos-=1
                confi=str(input(f"la contrasena no coincide, quedan {intentos} intentos antes de salir: "))
                if intentos==1:
                        return menu()
        base[usuario]=contrasena
        return print(f'se ha creado el usuario {usuario}')
        

def inicio():
        
        while len(base)==0:
                print("no se ha dado de alta ningun usuario")
                return (alta())
        usuario=input("ingrese su usuario: ")
        intentos=4
        while usuario not in base: 
                intentos-=1
                usuario=str(input(f"el usuario no existe, ingrese uno existente, quedan {intentos} intentos: "))
                if intentos==1:
                        return print("se agotaron los intentos")
        contrasena=str(input("ingrese su contrasena: "))
        intentos=4
        while contrasena!=base.get(usuario):
                intentos-=1
                contrasena=str(input(f"la contrasena es incorrecta, quedan {intentos} intentos:  "))
                if intentos==1:
                        return print("se agotaron los intentos")
        return print(f'(Has iniciado sesion como {usuario})')
        

        

menu()






