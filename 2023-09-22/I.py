def main():
    a, b = map(int, input().split())

    print(2 ** (a + b) % 998244353)

main()