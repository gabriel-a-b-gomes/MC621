class Fatorial:
    def __init__(self, n) -> None:
        self.base = [0 for _ in range(n + 1)] 


    def fat(self, n):
        if n <= 1:
            self.base[n] = 1
            return 1
        
        if self.base[n] > 0:
            return self.base[n]
        
        r = n * self.fat(n - 1)

        self.base[n] = r

        return r

def get_info(entry):
    sum = 0 #soma
    sub = 0 #subtracao
    itr = 0 #interrogacao

    for c in entry:
        if c == "+":
            sum += 1
        elif c == "-":
            sub += 1
        else:
            itr += 1

    return sum, sub, itr

def comb(n, k):
    f = Fatorial(n)

    return f.fat(n) / (f.fat(k) * f.fat(n - k))

def main():
    in1 = input()
    in2 = input()

    sum_base, sub_base, _ = get_info(in1)
    sum_receive, sub_receive, not_receive = get_info(in2)

    ans = 0

    rest = sub_base - sub_receive

    if not (rest < 0 or rest > not_receive):
        ans = comb(not_receive, rest) * (0.5 ** not_receive)
    
    print("{:.10f}".format(ans))
    
main()