#Realice una función que permita validar si una palabra es un palíndromo. 
# Condición: No se vale hacer slicing para invertir la palabra y verificar 
# que sea igual a la original.

#El usuario ingresa la palabra y el programa la vuelve una lista
palabra=str(input("Ingrese la palabra que desea validar:"))
lista_palabra=list(palabra)

adelante=0
atras= len(palabra)-1
bandera=True

# se crea la condicion para que mientras la letra de izquierda a derecha este antes
# que la letra que esta en sentido contrario se verifique si estas son iguales, de no ser 
# asi se toma como que no es un palinodromo
while adelante<atras:
    if lista_palabra[adelante]!= lista_palabra[atras]:
        bandera=False
    adelante+=1
    atras-=1

if bandera==True:
    print("La palabra es un palinodromo")
else:
    print("La palabra no es un palinodromo")