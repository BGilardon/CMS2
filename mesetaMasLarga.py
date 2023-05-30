from typing import List

# Aclaración: Debido a la versión de Python del CMS, para el tipo Lista, la sintaxis de la definición de tipos que deben usar es la siguiente:
# l: List[int]  <--Este es un ejemplo para una lista de enteros.
# Respetar esta sintaxis, ya que el CMS dirá que no pasó ningún test si usan otra notación.

def mesetaMasLarga(l: List[int]) -> int :
  n : int = 1
  m : int = 0
  for i in range(0, len(l)-1):
    if l[i] == l[i+1]:
      n += 1
      if i == len(l)-2 and n > m:
        m = n
        print("termino")
    else:
      if n > m:
        m = n
      n = 1
  return m


if __name__ == '__main__':
  x = input()
  print(mesetaMasLarga([int(j) for j in x.split()]))