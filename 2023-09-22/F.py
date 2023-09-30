import sys

def extendedMod(x, y, n):
  if y == 0: return 1
  if x == 0: return 0

  v = 0
  if y % 2 == 0:
    v = extendedMod(x, y / 2, n)
    v = (v * v) % n
  else:
    v = x % n
    v = (v * extendedMod(x, y - 1, n)) % n
  
  return (v + n) % n

if sys.version_info[0] < 3:
    input_func = raw_input
else:
    input_func = input

def main():
  e = input_func()
  t = int(e)

  for _ in range(t):
    e = input_func()
    a, b, n, M = map(int, e.split(" "))

    i = 1
    F = 1
    while i <= n:
       i += 1
       F = a * F + b

    print(extendedMod(F, 1, M))

  return 0

main()