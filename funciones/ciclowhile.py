#Se aprende el ciclo While 
captura = ''
'''while captura.lower() != 'fin':
    captura = input("Ingresa algo, o escribe fin para terminar")
While que cuenta hasta el numero 5
i =1
while i < 6:
    print('Este es el numero',i)
    if i == 3:
        break
    i = i+1 # i += 1
    
print("While finalizado")'''

print("Dinero a gastar:")
dinero = float(input())
#Mientras exista dinero
while dinero >0:
    print("Cuanto cuesta tu articulo? ")
    costo=float(input())
    if (dinero>= costo):
        dinero= dinero-costo
        print("Te lo puedes comprar, te queda:\n",dinero)
    elif (costo> dinero):
        diferencia = costo - dinero
        print("No te lo puedes comprar, te faltan:\n", diferencia)
    if dinero==0:
        print("No hay dinero")
        break
        