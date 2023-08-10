def main():
    d = input()
    p = 0
    i = 0

    for c in d:
        if c == "+":
            p += 1
        else:
            i += 1

    t = p - i

    e = input()

    p = 0
    i = 0
    n = 0

    for c in e:
        if c == "+":
            p += 1
        elif c == "-":
            i += 1
        else:
            n += 1

    a = p - i # atual
    r = t - a # quanto falta

    ans = 1

    if r == n == 0:
        print("{:.10f}".format(ans))
        return

    aux = n - r
    if (aux > 0):
        if (aux % 2 == 1):
            ans = 0
        else:
            ans = 0.5 ** (aux / 2)
            if (r > 0):
                ans *= 0.5 ** r
    elif (aux == 0):
        ans = 0.5 ** r
    else:
        ans = 0
    
    print("{:.10f}".format(ans))
    
main()