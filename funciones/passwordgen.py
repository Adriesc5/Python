#Generador random de contrasenhas
#Adriesc57
import random

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
 'Y', 'Z'] 
números = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
símbolos = ['!', '#', '$', '%', '&', '(', ')', '*', '+'] 

print("Bienvenido al generador de contrasenhas")

nrletras = int(input("Cuantas letras tendra la contrasenha?\n"))
nrsimb = int(input("Cuantos simbolos tendra la contrasenha?\n"))
nrnumeros = int(input("Cuantos numeros tendra la contrasenha?\n"))
password =[]

for i in range(nrletras):
    password.append(random.choice(letras))
    
for i in range(nrsimb):
    password.append(random.choice(símbolos))
    
for i in range(nrnumeros):
    password.append(random.choice(números))
#Mezclar los numeros dentro de la lista
random.shuffle(password)

#Convertir lista a texto con funcion join
setPassword ="".join(password)
print(f"Tu nueva contrasenha es: {setPassword}")