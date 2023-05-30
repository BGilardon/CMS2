import sys


#len(l) = n + 1
#l es una secuencia de numeros de fibonacci
#l[len(l)-1] = res
def fibonacciNoRecursivo(n: int) -> int:
  l : list = [0,1]
  for i in range(2, n+1):
    l.append(l[i-1]+l[i-2])
  return l[len(l)-1]

# for i in range(6):
#   print(i)
#   print(fibonacciNoRecursivo(i))
#   print()

if __name__ == '__main__':
  x = int(input())
  print(fibonacciNoRecursivo(x))