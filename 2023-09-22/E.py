import math

# def fat(n, rmb): 
#   if rmb[n] == 0:
#     i = 1
#     rmb[0] = 1
#     while i <= n:
#       rmb[i] = i * rmb[i - 1]
#       i += 1

#   return rmb[n]

# def comb(n, k):
#   rmb = [0 for _ in range(n + 1)]

#   return fat(n, rmb) / (fat(k, rmb) * fat(n - k, rmb))

def main():
  t = int(input())
  for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    a = sorted(a, reverse=True)

    d = a[k - 1]
    ins = 0
    out = 0
    for i in range(n):
      if (a[i] == d):
        if i < k:
          ins += 1
        out += 1

    res = math.comb(out, ins)
    print(int(res) % (10 ** 9 + 7))

main()