def main():
  t = int(input())

  for _ in range(t):
    N, B = map(int, input().split())

    choco = 0
    for _ in range(B):
      l = list(map(int, input().split()))

      pre_choco = 1

      for c in range(1, len(l)):
        pre_choco *= l[c]

      choco += pre_choco

    print(choco % N)

main()