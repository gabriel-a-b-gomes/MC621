def main():
    while 1:
        try:
            n = int(input())
            o = 11
            c = 2

            while o % n != 0:
                o = o * 10 + 1
                c += 1

            print(c)
        except:
            break

main()