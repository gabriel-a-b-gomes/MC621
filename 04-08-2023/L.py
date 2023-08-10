def main():
    n = int(input())

    s = input()
    i = 0
    k = 0
    o = 0
    while i < len(s):
        if (s[i] == "8"):
            o += 1

        if i > n - 11:
            break

        i += 1


    if o >= (n - 12) // 2:
        print("YES")
    else:
        print("NO")

main()