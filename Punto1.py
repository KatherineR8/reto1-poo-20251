#Crear una función que realice operaciones básicas (suma, resta, multiplicación, división) entre dos números, 
# según la elección del usuario, la forma de entrada de la función será los dos operandos y el caracter usado
# para la operación. entrada: (1,2,"+"), salida (3).
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

