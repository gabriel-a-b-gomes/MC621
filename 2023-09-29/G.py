def solve(a, b, n):
  if n == 0:
    return a
  if n == 1:
    return b
  if n == 2:
    return (1 + b) / a
  if n == 3:
    g = (1 + b) / a
    return (1 + g) / b
  
  g0 = (1 + b) / a
  g = (1 + g0) / b

  i = 4
  while i <= n:
    g, g0 = (1 + g) / g0, g
    i += 1

  return g

def main():
  while 1:
    try:
      a, b, n = map(int, input().split())

      if a == b == n == 0: raise EOFError

      n %= 10

      print(f"{solve(a, b, n):.0f}")
    except:
      break

main()