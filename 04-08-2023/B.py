class TreeMaster:
    def __init__(self, n, a, p) -> None:
        self.n = n
        self.a = a
        self.r = []
        self.p = []

        for i in range(n):
            self.p.append(p[i] - 1)
            self.r.append([0 for _ in range(n)])

    def calc(self, x, y):
        if x < 0 or y < 0:
            return 0
        
        ans = self.a[x] * self.a[y]

        calculed = self._reg_in(self.p[x], self.p[y])

        if calculed == None:
            calculed = self.calc(self.p[x], self.p[y])

            if self.p[x] >= 0 and self.p[y] >= 0:
                self.r[self.p[x]][self.p[y]] = calculed
                self.r[self.p[y]][self.p[x]] = calculed

        ans += calculed
        
        return ans
    
    def _reg_in(self, x_p, y_p):
        if self.r[x_p][y_p] > 0:
            return self.r[x_p][y_p]
        
        if self.r[y_p][x_p] > 0:
            return self.r[y_p][x_p]
            
        return None

def main():
    n, q = map(int, input().split())

    a = list(map(int, input().split()))

    p = [0] + list(map(int, input().split())) # adiciona a raiz

    tr = TreeMaster(n, a, p)

    for _ in range(q):
        x, y = map(int, input().split())
        print(tr.calc(x - 1, y - 1))

main()