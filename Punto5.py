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
  try:
    test_list : list = ["roma", "amor", "perro", "ropa", "pora", "mora", "juan", "porre"]
    print(mismas_letras(test_list))
  except TypeError: 
    print("Invalid types")