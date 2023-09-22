_mod = 10 ** 9 + 7

def solve(e, m):
    i = 0
    while i < m:
        aux = ""
        for c in e:
            aux += f"{int(c) + 1}"
        e = aux
        i += 1

    return len(e) % _mod
        

def main():
    n = int(input())

    for _ in range(n):
        e, m = input().split()
        print(solve(e, int(m)))

main()