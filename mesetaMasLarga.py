from typing import List

# Aclaración: Debido a la versión de Python del CMS, para el tipo Lista, la sintaxis de la definición de tipos que deben usar es la siguiente:
# l: List[int]  <--Este es un ejemplo para una lista de enteros.
# Respetar esta sintaxis, ya que el CMS dirá que no pasó ningún test si usan otra notación.

def mesetaMasLarga(l: List[int]) -> int:
    current_length: int = 0
    max_length: int = 0
    for i in range(0, len(l)):
        if l[i-1] == l[i]:
            current_length += 1
            if i == len(l)-1 and current_length > max_length:
                max_length = current_length
        else:
            if current_length > max_length:
                max_length = current_length
            current_length = 1
    return max_length


# def test():
#   vacia = []
#   UnElemento1 = [1]
#   DosElementos1 = [1,2]
#   DosElementos2 = [2,2]
#   MesetaAlFinal = [1,2,3,4,5,5,5]
#   MesetaAlPrincipio = [1,1,1,2,3,4,5]
#   MesetaAlMedio = [1,2,3,3,3,4,5]
#   DosMesetas = [1,2,3,3,3,3,4,5,5,5,5,6]

#   Listas = [vacia, UnElemento1, DosElementos1, DosElementos2, MesetaAlFinal, MesetaAlPrincipio, MesetaAlMedio, DosMesetas]

#   for lt in Listas:
#     print(lt, mesetaMasLarga(lt))


if __name__ == '__main__':
  x = input()
  print(mesetaMasLarga([int(j) for j in x.split()]))