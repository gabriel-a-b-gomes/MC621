def main():
    n = int(input())

    s = input()

    last = s[-11]

    s = s[:-11]

    o = 0

    for c in s:
        if c == "8":
            o += 1

    if last == "8" and o >= len(s) / 2:
        print("YES")
    else:
        print("NO")

main()