#Escribir una función que reciba una lista de números y devuelva solo aquellos que son primos. 
#La función debe recibir una lista de enteros y retornar solo aquellos que sean primos.

def numeros_primos(lista) -> list:
    lista_primos=[]
    
    for n in lista:
        if n < 2:
            continue
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                break
        else:
            lista_primos.append(n)
    return lista_primos


if __name__ == "__main__":
    lista_num=[]
    cantidad_num=int(input("De la cantidad de numeros que va a ingresar"))
    for n in range(cantidad_num):
        dato = int(input("Ingresa un dato"))
        lista_num.append(dato)
        
    primos=numeros_primos(lista_num)
    print(primos)