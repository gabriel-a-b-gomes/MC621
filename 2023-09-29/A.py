def main():
    t = int(input())

    for _ in range(t):
        k = int(input())

        finded = 0

        f = {
            2: 2 % k,
            3: 3 % k
        }

        hf = {
            2 % k: 2,
            3 % k: 3
        }

        n = 4

        while not finded:
            f[n] = (f[n - 1] + f[n - 2]) % k

            if f[n] in hf.keys():
                finded = hf[f[n]]
            else:
                hf[f[n]] = n
            n += 1

        print(finded)

main()