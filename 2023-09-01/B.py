def main():
  t = int(input())

  for i in range(t):
    n = int(input())

    d = 0
    p = 1
    while (1 - p) < 0.5:
      d += 1
      p *= (n - d) / n
    
    print(f"Case {i + 1}: {d}")

main()