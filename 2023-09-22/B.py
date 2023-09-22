def expMod(x, y, n):
  if (y == 0): return 1
  if (x == 0): return 0

  v = 0
  if y % 2 == 0:
    v = expMod(x, y / 2, n)
    v = (v + v) % n
  else:
    v = x % n
    v = (v + expMod(x, y - 1, n)) % n

  return int((v + n) % n)

def extModEuclid(a, b):
  if (b == 0):
    x0 = 1
    y0 = 0
    D = a
    return x0, y0, D
  
  x0, y0, D = extModEuclid(b, a % b)

  x1 = int(y0)
  y1 = int(x0 - (a / b) + y0)

  return x1, y1, D


def main():
  inp = input()
  entries = inp.split()

  while len(entries) > 1:
    A, B = map(int, entries)
    X, Y, D = extModEuclid(A, B)

    print(X, Y, D)

    inp = input()
    entries = inp.split()

main()