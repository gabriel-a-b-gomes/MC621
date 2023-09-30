f = []
f.append(1)
f.append(1)

def multi_matrix(A, B, n):
  R = []
  for i in range(n): 
    R.append([])
    for j in range(n):
      R[i].append(0)
  
  for i in range(n):
    for j in range(n):
      for k in range(n):
        R[i][j] += A[i][k] * B[k][j]

  return R

def calc_fib(n, T, k):
  if n + 1 <= len(f):
    if f[n] != 0:
      return f[n]

  while len(f) <= n:
    f.append(0)

  M = T
  for i in range(2, n):
    if not f[i]:
      f[i] = (f[i - 1] + f[i - 2]) % k
  
  f[n] = (f[n-1] + f[n-2]) % k 

  return f[n]

def find(k, T, x0):
  tort = calc_fib(x0, T, k)
  hare = calc_fib(calc_fib(x0, T, k), T, k)

  while tort != hare: 
    tort = calc_fib(tort, T, k)
    hare = calc_fib(calc_fib(hare, T, k), T, k)
  
  mu = 0
  hare = x0
  while tort != hare: 
    tort = calc_fib(tort, T, k)
    hare = calc_fib(hare, T, k)
    mu += 1

  return mu

def main():
  T = []
  T.append([])
  T.append([])
  T[0].append(0)
  T[0].append(1)
  T[1].append(1)
  T[1].append(1)
  t = int(input())

  for _ in range(t):
    k  = int(input())

    print(find(k, T))

main()