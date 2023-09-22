def det_luckiness(inp):
    if len(inp) == 0:
        return 0

    max = int(inp[0])
    min = int(inp[0])

    for i in range(1, len(inp)):
        c = int(inp[i])

        if c > max:
            max = c

        if c < min:
            min = c

    return min, max

def find_unluckest(in1, in2):
    a1, b1 = det_luckiness(in1)
    a2, b2 = det_luckiness(in2)

    return 1 if a1 - b1 < a2 - b2 else -1

def main():
    


main()