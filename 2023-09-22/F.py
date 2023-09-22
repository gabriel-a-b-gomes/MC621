import sys

if sys.version_info[0] < 3:
    input_func = raw_input
else:
    input_func = input

def main():
  t = int(input_func())

  for _ in range(t):
    a, b, n, M = map(int, input_func().split())

    i = 0
    F = 1
    while i <= n:
      F = a * F + b
      i += 1

    print(F % M)

main()