from typing import List
from typing import Tuple

# Aclaración: Debido a la versión de Python del CMS, para el tipo Lista y Tupla, la sintaxis de la definición de tipos que deben usar es la siguiente:
# l: List[int]  <--Este es un ejemplo para una lista de enteros.
# t: Tuple[str,str]  <--Este es un ejemplo para una tupla de strings.
# Respetar esta sintaxis, ya que el CMS dirá que no pasó ningún test si usan otra notación.

def sePuedeLlegar(origen: str, destino: str, vuelos: List[Tuple[str, str]]) -> int :
  res = 0
  salida : str = origen
  fin : bool = False
  vuelo : Tuple[str, str] = ('X', origen)
  while(not fin):
    nuevoVuelo : bool = False
    
    for i in range(len(vuelos)):
      if vuelos[i][0] == salida:
        vuelo : Tuple[str, str] = vuelos[i]
        nuevoVuelo = True
    
    if vuelo[1] == destino:
      fin = True
    
    salida = vuelo[1]

    res += 1

    if not nuevoVuelo:
      res = -1
      fin = True
    
    salida = vuelo[1]

  return res

# def test():
#   vuelos1 = [('A','B'), ('E','F'), ('B', 'A'), ('C','D'), ('D','E')]
#   test1 = sePuedeLlegar('C', 'B', vuelos1)
#   print(test1)
#   test2 = sePuedeLlegar('C', 'F', vuelos1)
#   print(test2)


if __name__ == '__main__':
  origen = input()
  destino = input()
  vuelos = input()
  
  print(sePuedeLlegar(origen, destino, [tuple(vuelo.split(',')) for vuelo in vuelos.split()]))