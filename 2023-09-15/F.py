def main():
  while 1:
    try:
      n = int(input())
      if n == 0: raise EOFError

      c = 1
      for i in range(2, n):
        d = n % i
        if (d != 0 and (n % d != 0 or i % d != 0)) or d == 1:
          c += 1

      print(c)

    except:
      break

main()