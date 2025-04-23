# reto1-poo-20251
### Katherine Restrepo
### Punto 1
Crear una función que realice operaciones básicas (suma, resta, multiplicación, división) entre dos números, 
según la elección del usuario, la forma de entrada de la función será los dos operandos y el caracter usado
para la operación. entrada: (1,2,"+"), salida (3).

```python
def operacion(num1:float, num2:float,operador:str)-> float: #define una funcion que en base al operador recibido realiza una operacion
    if operador== "+":
        resultado= num1+num2
    elif operador=="-":
        resultado= num1-num2
    elif operador=="*":
        resultado= num1*num2
    elif operador== "/":
        resultado= num1/num2
    else:
        print("Los datos de entrada no son validos")
    return resultado


if __name__ == "__main__":
  #El usuario ingresa los valores de las variables
  num1 = float(input("Ingrese el primer numero (en caso de ser esta o division el minuendo o dividendo respectivamente):"))
  num2 = float(input("Ingrese el segundo numero:"))
  operador = str(input("Ingrese el operador de la operacion que desea realizar:"))
  
  #se llama a la funcion y se da el resultado de la operacion
  resultado = operacion(num1,num2,operador)
  print(resultado)
```

### Punto 2
Realice una función que permita validar si una palabra es un palíndromo. 
Condición: No se vale hacer slicing para invertir la palabra y verificar 
que sea igual a la original.

```python
#El usuario ingresa la palabra y el programa la vuelve una lista
palabra=str(input("Ingrese la palabra que desea validar:"))
lista_palabra=list(palabra)

adelante=0
atras= len(palabra)-1
bandera=True

# se crea la condicion para que mientras la letra de izquierda a derecha este antes
# que la letra que esta en sentido contrario se verifique si estas son iguales, de no ser 
# asi se toma como que no es un palinodromo
while adelante < atras:
    if lista_palabra[adelante] != lista_palabra[atras]:
        bandera=False
    adelante += 1
    atras -= 1

if bandera==True:
    print("La palabra es un palinodromo")
else:
    print("La palabra no es un palinodromo")
```
### Punto 3
Escribir una función que reciba una lista de números y devuelva solo aquellos que son primos. 
La función debe recibir una lista de enteros y retornar solo aquellos que sean primos.

### Punto 3
Escribir una función que reciba una lista de números y devuelva solo aquellos que son primos. 
La función debe recibir una lista de enteros y retornar solo aquellos que sean primos.

```python
Escribir una función que reciba una lista de números y devuelva solo aquellos que son primos. 
La función debe recibir una lista de enteros y retornar solo aquellos que sean primos.

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

```

### Punto 4
Escribir una función que reciba una lista de números enteros y retorne la mayor suma entre dos elementos consecutivos.

```python
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
```
### Punto 5
Escribir una función que reciba una lista de string y retorne unicamente aquellos elementos que tengan 
los mismos caracteres. e.g. entrada: ["amor", "roma", "perro"], salida ["amor", "roma"]

```python
def mismas_letras(lista_palabras: list) -> list:

  palabras = {} # diccionario vacio para guardar las palabras con el mismo orden lexicografico
  resultado = [] # lista vacia para palabras con las mismas letras

  for word in lista_palabras:
    valor = "".join(sorted(word)) # Ordena la palabra lexicograficamente y guarda la palabra original
    if valor in palabras.keys():
      palabras[valor] += [word]
    else:
      palabras[valor] = [word]
  
  for value in palabras.values(): # si tiene dos o mas palabras, estas tienen las mismas letras
    if len(value) >= 2:
      resultado += value

  return resultado 

if __name__ == "__main__":

  test_list : list = ["roma", "amor", "perro", "ropa", "pora", "mora", "juan", "porre"]
  print(mismas_letras(test_list))
```
