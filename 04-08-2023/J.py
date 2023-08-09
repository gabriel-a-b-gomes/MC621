def calcularOperacoes(v):
    k = 0 # operações

    i = 0
    j = len(v) - 1

    while i <= j:
        if (v[i] == 1 and v[j] == 0):
            k += 1
            i += 1
            j -= 1
        else:
            if (v[i] == 0):
                i += 1

            if (v[j] == 1):
                j -= 1

    return k

def main():
    n = int(input())

    for _ in range(n):
        t = int(input())
        a = list(map(int, input().split()))

        print(calcularOperacoes(a))

main()