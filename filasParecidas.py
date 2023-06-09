from typing import List

# Aclaración: Debido a la versión de Python del CMS, para el tipo Lista, la sintaxis de la definición de tipos que deben usar es la siguiente:
# l: List[int]  <--Este es un ejemplo para una lista de enteros.
# Respetar esta sintaxis, ya que el CMS dirá que no pasó ningún test si usan otra notación.

def filasParecidas(matriz: List[List[int]]) -> bool :
  res : bool = True

  if len(matriz) > 1:
    n : int = matriz[1][0] - matriz[0][0]
    for i in range(1, len(matriz)):
      for j in range(len(matriz[0])):
        if matriz[i][j] != (matriz[i-1][j] + n):
          res = False

  return res



# def test():
#   m1 = [[1]]  #Si es [x] no es una seq<seq<Z>> es una seq<Z>
#   m2 = [[1,2,3]]
#   m2ymedio = [[1,2,3],[4,5,6]]
#   m3 = [[1],[2],[4]]
#   m4 = [[1,2,3],[4,5,6],[7,8,9]]
#   m5 = [[1,2,3],[4,5,6],[7,9,9]]
#   matrices = [m1,m2,m2ymedio,m3,m4,m5]
#   for m in matrices:
#     print(m)
#     print(filasParecidas(m))
#     print()

if __name__ == '__main__':
  filas = int(input())
  columnas = int(input())
 
  matriz = []
 
  for i in range(filas):         
    fila = input()
    if len(fila.split()) != columnas:
      print("Fila " + str(i) + " no contiene la cantidad adecuada de columnas")
    matriz.append([int(j) for j in fila.split()])
  
  print(filasParecidas(matriz))