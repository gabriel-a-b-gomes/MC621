def gcd(a, b):
  return a if b == 0 else gcd(b, a % b)

def main():
  n = int(input())
  
  a = list(map(int, input().split()))
  k = a[0]
  for i in range(1, n):
    g = gcd(k, a[i])
    print(f"{k // g}/{a[i] // g}")


main()