class Draw:
    def __init__(self) -> None:
        self.dot = []
        self.black = []
        self.ans = []
        self.n, self.k, self.model = self.read_data()

        for _ in range(self.n ** (self.k - 1)):
            self.dot.append("")
            self.black.append("*" * self.n ** (self.k - 1))

        for _ in range(self.n ** self.k):
            self.ans.append("")


    def make_draw(self, k, row):
        if k <= 1: # quando k for 1, usar o modelo
            for i in range(self.n):
                self.dot[i + row] += self.model[i]
            return
        
        if k == self.k: 
            self.make_draw(k - 1, row)
            return

        for i in range(self.n):

            e = int(row + i * self.n ** (k - 1))

            for j in range(self.n):
                if self.model[i][j] == "*":
                    aux = "*" * self.n ** (k - 1)

                    for u in range(self.n ** (k - 1)):
                        self.dot[u + e] += aux
                else:
                    self.make_draw(k - 1, e)

    def finish_draw(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.model[i][j] == "*":
                    self._apply_ans(i, self.black)
                else:
                    self._apply_ans(i, self.dot)

    def _apply_ans(self, i, base):
        for u in range(self.n ** (self.k - 1)):
            self.ans[u + int(i * self.n ** (self.k - 1))] += base[u]

    def read_data(self):
        with open('input.txt', 'r') as input:
            lines = [line.strip() for line in input]

            n, k = map(int, lines[0].split())

            model = []

            for i in range(n):
                model.append(lines[i + 1])

            input.close()

        return n, k, model
    
    def print_draw(self):
        with open("output.txt", "w") as f:
            for i in range(self.n ** self.k):
                print(self.ans[i], file=f)

            f.close()

def main():
    d = Draw()

    if d.k == 1: # se k == 1 então a resposta é de graça
        d.ans = d.model
    else:
        d.make_draw(d.k, 0)

        d.finish_draw()

    d.print_draw()

main()