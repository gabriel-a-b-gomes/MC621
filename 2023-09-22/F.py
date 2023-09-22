def main():
  t = int(input())

  for _ in range(t):
    a, b, n, M = map(int, input().split())

    i = 0
    F = 1
    while i <= n:
      F = a * F + b
      i += 1

    print(F % M)

main()