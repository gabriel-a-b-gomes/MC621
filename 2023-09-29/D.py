def solve(k, ss):
    if k == 1:
        return 1

    if k in ss.keys():
        return ss[k]
    
    m = 0
    if k % 2 == 0:
        m = k // 2
    else:
        m = 3 * k + 1

    ss[k] = 1 + solve(m, ss)
    
    return ss[k]

def main():
    ss = {}
    while 1:
        try:
            i, j = map(int, input().split())
            
            b, e = i, j
            if b > e:
                b, e = j, i

            max = 0
            for k in range(b, e + 1):
                s = solve(k, ss)
                if s > max: max = s
            print(i, j, max)
        except:
            break

main()