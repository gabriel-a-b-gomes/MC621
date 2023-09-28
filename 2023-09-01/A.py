def main():
    t = int(input())

    for _ in range(t):
        n = int(input())

        if n == 1:
            print("Alice")
        elif (n >= 2 and n <= 4):
            print("Bob")
        else:
            print("Alice")

main()