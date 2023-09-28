def main():
    n = int(input())

    s = input()

    s = s[:-10]

    k = 0

    for c in s:
        if c == "8":
            k += 1

    if k >= len(s) / 2:
        print("YES")
    else:
        print("NO")

main()