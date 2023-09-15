import math

def main():
    n = int(input())

    m = n
    ans = 0

    for i in range(2, int(math.sqrt(n)) + 1):
        while m % i == 0 and m > 1:
            m = m // i
            ans += 1
        if m == 1:
            break

    if m != 1: ans += 1

    print(ans)

main()
