import math

def isPrime(n):
  for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0:
      return False
    
  return True

def main():
  while 1:
    try:
      n = int(input())
      if (n == 0): 
        raise EOFError

      i = 2 * n + 1
      while not isPrime(i):
        i += 2

      nP = isPrime(n)
      if not nP:
        print(i, f"({n} is not prime)")
      else:
        print(i)
    except:
      break 

main()