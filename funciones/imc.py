print("Bienvenido a la calculadora de IMC")
peso= float(input("Cual es tu peso?"))
altura= float(input("Cual es tu altura"))
imc= float(peso/(altura*altura))
if imc <= 18.5:
    print("Tu IMC es: ",imc," tienes bajo peso")
elif imc > 18.6 and imc <=24.9:
    print("Tu IMC es: ",imc," tienes peso normal")
elif imc >=25 and imc <=29.9:
    print("Tu IMC es: ",imc," tienes obesidad")
else :
    print("Tu IMC es: ",imc," tienes obesidad")
    
