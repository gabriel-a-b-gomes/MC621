def solve():
    N, K, M = map(int, input().split())

    t = 0
    n = N
    while n * K <= M: 
        t += 1
        n *= K

    print(t)

def main():
    P = int(input())
    
    for _ in range(P):
        solve()

main()