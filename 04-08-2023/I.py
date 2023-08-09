def max(v):
    if (len(v) < 0):
        return None
    
    max = v[0]
    for i in range(1, len(v)):
        if (v[i] > max):
            max = v[i]

    return max

def solve(init, scnd):
    i_max = max(init)
    s_max = max(scnd)

    return i_max >= s_max

def main():
    t = int(input())

    for _ in range(t):
        n = int(input())
        nv = list(map(int, input().split()))
        m = int(input())
        mv = list(map(int, input().split()))

        if (solve(nv, mv)):
            print("Alice")
        else:
            print("Bob")

        if (solve(mv, nv)):
            print("Bob")
        else:
            print("Alice")

main()