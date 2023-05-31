from typing import List
from typing import Tuple

# Aclaración: Debido a la versión de Python del CMS, para el tipo Lista y Tupla, la sintaxis de la definición de tipos que deben usar es la siguiente:
# l: List[int]  <--Este es un ejemplo para una lista de enteros.
# t: Tuple[str,str]  <--Este es un ejemplo para una tupla de strings.
# Respetar esta sintaxis, ya que el CMS dirá que no pasó ningún test si usan otra notación.

def sePuedeLlegar(origen: str, destino: str, vuelos: List[Tuple[str, str]]) -> int :
  res : int = 0
  salida : str = origen
  fin : bool = False
  vuelo : Tuple[str, str] = ()
  if len(vuelos) == 0:
    fin = True
    res = -1
  
  while(not fin):
    nuevoVuelo : bool = False
    
    for i in range(len(vuelos)):
      if vuelos[i][0] == salida:
        vuelo = vuelos[i]
        nuevoVuelo = True
    
    res += 1 #Otro vuelo => +1

    if vuelo[1] == destino: #Llegue a destino => Fin
      fin = True
    
    salida = vuelo[1] #Mi nueva salida es el destino anterior

    if vuelo[1] == origen: #Si volvi al principio no hay camino
      res = -1
      fin = True
    
    if not nuevoVuelo: #Si llegue a un punto final, no hay camino
      res = -1
      fin = True

  return res

# def test():
#   vuelos1 = [('A','B'), ('E','F'), ('F', 'C'), ('B', 'A'), ('C','D'), ('D','E')]
#   vuelosVacios = []
#   VuelosBucle = [('A','B'), ('B', 'C'), ('C', 'D'), ('D','A')]
  
#   test1 = sePuedeLlegar('C', 'B', vuelos1)
#   print(test1)
  
#   test2 = sePuedeLlegar('C', 'F', vuelos1)
#   print(test2)

#   test3 = sePuedeLlegar('A', 'B', vuelosVacios)
#   print(test3)

#   test4 = sePuedeLlegar('A', 'F', VuelosBucle)
#   print(test4)



if __name__ == '__main__':
  origen = input()
  destino = input()
  vuelos = input()
  
  print(sePuedeLlegar(origen, destino, [tuple(vuelo.split(',')) for vuelo in vuelos.split()]))