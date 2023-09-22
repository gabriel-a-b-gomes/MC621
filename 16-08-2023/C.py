def exp(x, p):
    if p == 0:
      return 1
    
    if p % 2 == 0:
       a = exp(x, p / 2)
       return a * a
    
    a = exp(x, (p - 1) / 2)
    return x * a * a

def isTwoSequence(t):
   if t % 2 == 1:
      return False
   
   i = 0
   m = exp(2, i)
   while m < t:
      i += 1
      m = exp(2, i)
      
   return m == t

def main():
    x = int(input())

    ans = 0

    t = x

    if x > 0: 
       ans = 1

    while not isTwoSequence(t):
      t -= 1
      ans += 1

    print(ans)


main()