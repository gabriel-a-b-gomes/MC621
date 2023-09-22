def exp(x, p):
    if p == 0:
      return 1
    
    if p % 2 == 0:
       a = exp(x, p / 2)
       return a * a
    
    a = exp(x, (p - 1) / 2)
    return x * a * a

def main():
    n = int(input())
    m = int(input())

    print(m % exp(2, n))

main()