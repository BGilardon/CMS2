import sys
from typing import List


#len(l) = n + 1
#l es una secuencia de numeros de fibonacci
#l[len(l)-1] = res
def fibonacciNoRecursivo(n: int) -> int:
  l : List[int] = []
  for i in range(n+1):
    if i == 0:
      l.append(0)
    if i == 1:
      l.append(1)
    if i > 1:
      l.append(l[i-1]+l[i-2])
  return l[len(l)-1]

# def test():
#   K = []
#   for i in range(10):
#     K.append((i, fibonacciNoRecursivo(i)))
#   print(K)

if __name__ == '__main__':
  x = int(input())
  print(fibonacciNoRecursivo(x))