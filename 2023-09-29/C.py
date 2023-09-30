def evaluate(e, x, N, r):
    if x in r.keys():
        return r[x]

    s = []

    for i in range(len(e)):
        if e[i] == "x":
            s.append(x)
        elif e[i] == "N":
            s.append(N)
        elif e[i] == "+":
            e1 = s[-1]
            e2 = s[-2]
            s.pop()
            s.pop()

            s.append(e1 + e2)
        elif e[i] == "*":
            e1 = s[-1]
            e2 = s[-2]

            s.pop()
            s.pop()

            s.append(e1 * e2)
        elif e[i] == "%":
            e1 = s[-1]
            e2 = s[-2]

            s.pop()
            s.pop()

            s.append(e2 % e1)
        else:
            s.append(int(e[i]))

    r[x] = s[0]
    return r[x]

def findCycle(e, n, N, r):
    t = evaluate(e, n, N, r)
    h = evaluate(e, t, N, r)

    while t != h:
        t = evaluate(e, t, N, r)
        h = evaluate(e, evaluate(e, h, N, r), N, r)
    
    mu = 0
    h = n
    while t != h:
        t = evaluate(e, t, N, r)
        h = evaluate(e, h, N, r)

    ly = 1
    h = evaluate(e, t, N, r)
    while t != h:
        h = evaluate(e, h, N, r)
        ly += 1

    return mu, ly


def main():
    while 1:
        try:
            r = {}
            ins = input().split()

            N = int(ins[0])
            n = int(ins[1])

            if N == 0: raise EOFError

            ins = ins[2:]

            mu, ly = findCycle(ins, n, N, r)

            print(ly)
        except:
            break

main()