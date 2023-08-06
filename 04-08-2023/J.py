def calcularOperacoes(v, t):
    k = 0 # operações

    i = 0
    j = t - 1

    while i != j:
        if (v[j] < v[i]):
            p = j
            while p < len(v) - 2 and v[p] + v[i] > v[p + 1]:
                p += 1

            v[p] += v[i]
            i += 1
            k += 1
        else:
            j -= 1

    return k

def main():
    n = int(input())

    for _ in range(n):
        t = int(input())
        a = list(map(int, input().split()))

        print(calcularOperacoes(a, t))

main()