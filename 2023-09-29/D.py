def solve(k):
    ans = 1

    while k != 1:
        if k % 2 == 0:
            k = k // 2
        else: 
            k = 3 * k + 1
        ans += 1
    
    return ans

def main():
    ss = {}
    while 1:
        try:
            i, j = map(int, input().split())
            max = 0
            for k in range(i, j + 1):
                if k in ss.keys():
                    s = ss[k]
                else:
                    s = solve(k)
                    ss[k] = s
                if s > max: max = s
            print(i, j, max)
        except:
            break

main()