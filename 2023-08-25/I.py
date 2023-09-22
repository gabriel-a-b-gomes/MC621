_PLUS = 1
_MINUS = -1
_MAXDIGITS = 30

class BigNum:
    def __init__(self) -> None:
        self.digits = [0 for _ in range(_MAXDIGITS)]
        self.decimal = 0
        self.signbit = 0
        self.lastdigit = -1

    def setDecimal(self, d):
        if d[0] == '-':
            self.signbit = _MINUS
            d = d[1:]
        else:
            self.signbit = _PLUS

        self.decimal = int(d)

    def setDecimalN(self, d):
        self.decimal = d

    def showFloat(self):
        sw = ""
        for i in range(self.lastdigit + 1):
            sw += f"{self.digits[i]}"

        return sw

    def convert(self, s):
        for i in range(len(s)):
            self.lastdigit += 1
            self.digits[self.lastdigit] = int(s[i])


def compareBigNum(a: BigNum, b: BigNum):
    if a.signbit == _MINUS and b.signbit == _PLUS: return _PLUS
    if a.signbit == _PLUS and b.signbit == _MINUS: return _MINUS

    for i in range(a.lastdigit + 1):
        if a.digits[i] > b.digits[i]: return _MINUS * a.signbit
        if b.digits[i] > a.digits[i]: return _PLUS * a.signbit

def subtractBigNum(a: BigNum, b: BigNum, c: BigNum):
    if a.signbit == _MINUS or b.signbit == _MINUS:
        b.signbit = -1 * b.signbit
        addBigNum(a, b, c)
        b.signbit = -1 * b.signbit
        return
    
    if compareBigNum(a, b) == _PLUS:
        subtractBigNum(b, a, c)
        c.signbit = _MINUS
        return
    
    c.lastdigit = max(a.lastdigit, b.lastdigit)
    borrow = 0
    for i in range(c.lastdigit, -1, -1):
        v = a.digits[i] - borrow - b.digits[i]
        if a.digits[i] > 0: borrow = 0
        if v < 0:
            v += 10
            borrow = 1

        c.digits[i] = v

    v = a.decimal - borrow - b.decimal
    if v < 0:
        v += 10
    c.setDecimalN(v)


def addBigNum(a: BigNum, b: BigNum, c: BigNum):
    if a.signbit == b.signbit: c.signbit = a.signbit
    else: 
        if a.signbit == _MINUS:
            a.signbit = _PLUS
            subtractBigNum(b, a, c)
            a.signbit = _MINUS
        else:
            b.signbit = _PLUS
            subtractBigNum(a, b, c)
            b.signbit = _MINUS
        return
    
    c.lastdigit = max(a.lastdigit, b.lastdigit)
    carry = 0

    for i in range(c.lastdigit, -1, -1):
        c.digits[i] = (carry + a.digits[i] + b.digits[i]) % 10
        carry = (carry + a.digits[i] + b.digits[i]) // 10

    c.setDecimalN(carry + a.decimal + b.decimal)

def main():
    n = int(input())

    for _ in range(n):
        num = input().split(".")

        ans = BigNum()
        ans.setDecimal(num[0])
        ans.convert(num[1])

        while True:
            num = input().split(".")
            if len(num) == 1 and num[0] == '0': break

            newEntry = BigNum()
            newEntry.setDecimal(num[0])
            newEntry.convert(num[1] if len(num) > 1 else "0")

            addBigNum(ans, newEntry, ans)
        
        print(f"{ans.signbit * ans.decimal}.{ans.showFloat()}")

main()