import math

def main():
    N = int(input())
    ans = 0
    for i in range(int(math.sqrt(N)) + 1, 0, -1):
        if N % i == 0: 
            ans = i
            break
    
    print(N - ans if ans > 0 else 0)

main()