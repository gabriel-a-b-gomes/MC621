import math

def solve(n):
  f = math.sqrt(2) + math.sqrt(3) + math.sqrt(6)

  if n == 0:
    return f
  elif n == 1:
    return (f ** 2 - 5) / (2 * f + 4)
  elif n == 2:
    i = 1
    while i <= 2:
      f = (f ** 2 - 5) / (2 * f + 4)
      i += 1
  elif n % 2 == 1:
    i = 1
    while i <= 3:
      f = (f ** 2 - 5) / (2 * f + 4)
      i += 1
  else:
    i = 1
    while i <= 4:
      f = (f ** 2 - 5) / (2 * f + 4)
      i += 1
      
  return f 

def main():
  while 1:
    try:
      n = int(input())

      print(f"{solve(n):.10f}")
    except:
      break

main()