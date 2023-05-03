# Adrian Escobedo
#primer programa
print("Bienvenido a la calculadora de propinas")
#entradas
cuenta = float(input("Cual es el total de la cuenta?"))
porcentaje =float(input("Que porcentaje de propina desea dar?"))
comensales = float(input("En cuantas personas se dividira la cuenta?"))
porcentajeDecimal = float(porcentaje/100)
propina = float(cuenta * porcentajeDecimal)
totalCuenta = float(cuenta + propina)
pagoPPersona = float(totalCuenta / comensales)
pagoTotal = float(round(pagoPPersona,2))
#salidas
print("Cada persona pagara: ",pagoTotal)
