#Escribir una función que reciba una lista de números enteros y retorne la mayor suma entre dos elementos consecutivos.
def mayor_suma(lista)-> int:
    suma_mayor=lista[0]+lista[1]

    for i in range(1,len(lista)-1):
        suma=lista_num[i]+lista_num[(i+1)]
        if suma>suma_mayor:
            suma_mayor=suma

    return suma_mayor



if __name__ == "__main__":
    lista_num=[]
    cantidad_num=int(input("De la cantidad de numeros que va a ingresar"))
    for n in range(cantidad_num):
        dato = int(input("Ingresa un dato"))
        lista_num.append(dato)
        

    respuesta=mayor_suma(lista_num)
    print(respuesta)
