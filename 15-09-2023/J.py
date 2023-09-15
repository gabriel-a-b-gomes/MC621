import math

def sieve(n):
    primes = [1 for _ in range(n + 1)]
    primes[0] = primes[1] = 0

    for i in range(2, n + 1):
        if (primes[i]):
            for j in range(i * i, n + 1, i):
                primes[j] = 0
    
    return primes
            

def main():
    n = int(input())

    primes = sieve(10000000)

    while (n != 0):
        ans  = 0 # considera o 1

        if not primes[n] == 1:
            for i in range(2, n):
                if n % i != 0 :
                    if primes[i] == 1:
                        ans += 1
            if n > 1:
                ans += 1
        else:
            ans = n - 1
        
        print(ans)

        n = int(input())

main()