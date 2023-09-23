def extModEuclid(a, b):
  if (b == 0):
    x0 = 1
    y0 = 0
    D = a
    return x0, y0, D
  
  x0, y0, D = extModEuclid(b, a % b)

  x1 = y0
  y1 = x0 - a // b * y0

  return x1, y1, D


def main():
  while 1:
    try:
      A, B = map(int, input().split())
      X, Y, D = extModEuclid(A, B)

      print(X, Y, D)
    except:
      break

main()