def getValue(res, i):
    return (res * 10 ** i) % 10

def findCycle(res):
    i = 1

    t = getValue(res, i)
    h = getValue(res, 2 * i)

    while t != h:
        t = getValue(res, i)
        h = getValue(res, 2 * i)
        i += 1
    
    mu = 0
    j = 0
    while t != h:
        t = getValue(res, i)
        h = getValue(res, j)
        i += 1
        j += 1

    ly = 1
    h = getValue(res, t)
    while t != h:
        h = getValue(res, h)
        ly += 1

    return mu, ly

def main():
    while 1:
        try:
            n, m = map(int, input().split())

            res = n - (m * (n % m))
            res = res / m

            m, l = findCycle(res)

            print(l)
        except:
            break

main()