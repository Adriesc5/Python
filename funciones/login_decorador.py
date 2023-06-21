#Se define el metodo que sera el decorador

def verificador_login(funcion):
    user= str(input("Ingresa usuario\n"))
    password= str(input("Ingresa password\n"))
    
    #se declara una funcion retornada por el decorador
    def nueva_funcion():
        if user == "Admin" and password=="1234":
            funcion() # esta func es la que nos dice si pudimos entrar
        else:
            print("Usuario o contrasena incorrectos")
    return nueva_funcion
    
@verificador_login
def mostrar_mensaje():
    print("Login exitoso")
    
#Programa principal. llamado al metodo decorado
mostrar_mensaje()
