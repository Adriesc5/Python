#Estructura basica de un decorador
def decorador(funcion):
    def funcion_decorada():
        print("Antes de ejecutar la funcion")
        funcion()
        print("Despues de ejecutar la funcion")
    return funcion_decorada

@decorador
def mi_funcion():
    print("Hola Mundo")
mi_funcion()    