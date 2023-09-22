import sys

if sys.version_info[0] < 3:
    input_func = raw_input
else:
    input_func = input

def main():
  e = input_func()
  t = int(e)

  for _ in range(t):
    e = input_func()
    a, b, n, M = map(int, e.split(" "))

    i = 0
    F = (a + b) ** n

    print(F % M)

  return 0

main()