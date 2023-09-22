def solve(inp): 
  int = 0
  for i in inp:
    int += 1 if i == '?' else 0

  if inp[0] == '0':
    return 0
  
  if int == 0:
    return 1
  
  ans = 0
  if inp[0] == '?':
    ans = 9
  else:
    ans = 10

  int -= 1

  ans *= 10 ** int

  return ans

def main():
  t = int(input())

  for _ in range(t):
    i = input()
    print(solve(i))

main()