def calc_S(S, hist):
  i = len(hist)
  while i <= S:
    if i >= len(hist) or not hist[i]:
      hist.append(hist[i - 1] + i ** i)
    i += 1
  
  return hist

def get_last_digit(S):
  return S % 10

def main():
  hist = []
  hist.append(0)
  while 1:
    try:
      S = int(input())
      if S == 0: raise EOFError

      m = S % 10
      S //= 10
      m += (S % 10) * 10

      hist = calc_S(m, hist)


      print(get_last_digit(hist[m]))
    except:
      break

main()