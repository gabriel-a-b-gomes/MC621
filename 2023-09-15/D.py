def gcd(a, b):
  return a if b == 0 else gcd(b, a % b)

def main():
  n, m = map(int, input().split())
  a = list(map(int, input().split()))
  b = list(map(int, input().split()))

  for j in range(m):
    k = a[0] + b[j]
    for i in range(1, n):
      k = gcd(k, a[i] + b[j])

    print(k, end=" ")
  print()

main()