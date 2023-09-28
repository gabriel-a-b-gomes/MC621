def main():
    t = int(input())

    for _ in range(t):
        n = int(input())
        r = input()
        b = input()

        r_wins = 0
        b_wins = 0
        equal = 0
        for i in range(len(r)):
            if (r[i] > b[i]):
                r_wins += 1
            elif r[i] == b[i]:
                equal += 1
            elif r[i] < b[i]:
                b_wins += 1

        if r_wins > b_wins:
            print("RED")
        elif r_wins == b_wins or equal == n:
            print("EQUAL")
        else:
            print("BLUE")

main()