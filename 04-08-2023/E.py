import math

def isPrime(m):
    for i in range(2, int(math.sqrt(m)) + 1):
        if (m % i == 0):
            return False
    return True

def main():
    n = int(input())

    for m in range(1, 1001):
        if (not isPrime(n * m + 1)):
            return print(m)

main()