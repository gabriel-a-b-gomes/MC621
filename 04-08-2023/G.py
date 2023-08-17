def main():
    n = int(input())

    names = []

    dp = [(0, '') for _ in range(n)]

    ans = 0

    for i in range(n):
        names.append(input())
        
        v = (0, '')

        if names[i][0] == names[i][-1]:
            v = (len(names[i]), names[i][0])

        for j in range(i):
            if names[j][0] == names[i][-1] or names[i][-1] == dp[j][1]:
                letter = dp[j][1] if names[i][-1] == dp[j][1] else names[j][0]

                temp = (dp[j][0] if dp[j][0] > 0 else len(names[j])) + len(names[i])

                if temp > v[0]:
                    v = (temp, letter)

        dp[i] = v

        if dp[i][0] > ans:
            ans = dp[i][0]

    print(ans)

main()
