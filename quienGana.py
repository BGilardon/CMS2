import sys

def quienGana(j1: str, j2: str) -> str : 
    res : str = ""
    if j1 == j2:
      res = "Empate"

    if j1 == "Piedra":
      if j2 == "Papel":
        res = "Jugador2"
      if j2 == "Tijera":
        res = "Jugador1"

    if j1 == "Papel":
      if j2 == "Tijera":
        res = "Jugador2"
      if j2 == "Piedra":
        res = "Jugador1"

    if j1 == "Tijera":
      if j2 == "Piedra":
        res = "Jugador2"
      if j2 == "Papel":
        res = "Jugador1"

    return res



# def test():
#   PPT = ["Piedra", "Papel", "Tijera"]
#   for j in PPT:
#     for k in PPT:
#       print(f"Jugador 1 = {j} \nJugador 2 = {k} \nResultado = {quienGana(j,k)}\n")




if __name__ == '__main__':
  x = input()
  jug = str.split(x)
  print(quienGana(jug[0], jug[1]))