import math

def main():
  t = int(input())

  for _ in range(t):
    max = 0
    n = int(input())
    isColleting = False

    curr = 0
    for i in range(1, n + 1):
      if n % i == 0:
        isColleting = True
        curr += 1
      elif isColleting:
        break

    if (curr > max): max = curr

    print(max)

main()