def main():
    n, m, s, t = map(int, input().split())

    g = {
        "E": [[] for _ in range(n)]
    }

    actual = [s]
    sw = [0 for _ in range(n)]

    sw[s] = 1

    ts = [0 for _ in range(t)]

    for _ in range(m):
        a, b = map(int, input().split())
        g["E"][a].append(b)
        g["E"][b].append(a)

    for i in range(t):
        new_actual = set()

        while len(actual) > 0:
            a = actual[0]
            for b in g["E"][a]:
                new_actual.add(b)
                sw[b] += sw[a]
                ts[i] += sw[a]

            sw[a] = 0

            actual = actual[1:] # tira da fila

        actual = list(map(lambda x: x, new_actual))

    print(ts[-1])

main()