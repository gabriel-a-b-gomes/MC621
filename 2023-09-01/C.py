def main():
    t = int(input())

    for _ in range(t):
        n, p, i = input().split()

        n = int(n)
        p = float(p)
        i = int(i) - 1

        Ps = []
        
        never_occurs = (1 - p) ** n

        for j in range(n):
            Ps.append(p * (1 - p) ** j)

        ans = Ps[i] / (1 - never_occurs)

        print(f"{ans:.4f}")

main()