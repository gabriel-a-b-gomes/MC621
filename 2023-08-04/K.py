def media(v, i, j):
    m = 0
    for k in range(i, j): 
        m += v[k]
    
    return m // (j - i)

def modulo(a, b):
    if (a - b < 0):
        return (-1) * (a - b)
    
    return a - b

def solve():
    n, x = map(int, input().split())

    a = list(map(int, input().split()))


    v = a[0] + x
    if (n > 1):
        v = media(a, 0, 2)

    k = 0

    for i in range(1, n):
        if modulo(v, a[i]) > x:
            v = media(a, i, len(a))
            k += 1

    print(k)

def main():
    t = int(input())

    for _ in range(t):
        solve()

main()