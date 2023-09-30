import math

def isPrime(n):
  for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0:
      return False
  
  if n == 1: return False

  return True

def isHappy(n):
  ans = n

  while 1:
    curr = 0
    while ans > 0:
      d = ans % 10
      curr += d ** 2
      ans //= 10

    if curr < 10 and curr != 1: return False
    if curr == 1: return True

    ans = curr

def main():
  t = int(input())
  for _ in range(t):
    k, m = map(int, input().split())

    # if isPrime(m) and isHappy(m):
    if isPrime(m):
      print(f"{k} {m} YES")
    else:
      print(f"{k} {m} NO")

main()