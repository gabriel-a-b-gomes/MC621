def isYes(s):
    if (len(s) < 3):
        return "NO"

    if (s[0] != 'Y' and s[0] != 'y'):
        return "NO"

    if (s[1] != 'E' and s[1] != 'e'):
        return "NO"
    
    if (s[2] != 'S' and s[2] != 's'):
        return "NO"
    
    return "YES"

def main():
    t = int(input())

    for _ in range(t):
        print(isYes(input()))

main()