def printRhombus(a, b=1, *symbols):
    m = list(range(1, a + 1, 2))
    n = list(range(a - 2, 0, -2))
    x=0
    y=0
    for i in m + n:
        if 2 * b < i:
            for x in range(0,len(symbols)):
                if x==0:
                    print(' ' * int((a - i) / 2), symbols[x] * b, ' ' * (i - 2 * b), symbols[x] * b, sep='', end='')
                else:
                    print(' ' * int((a - i)), symbols[x] * b, ' ' * (i - 2 * b), symbols[x] * b, sep='', end='')
            print()
        else:
            for y in range(0, len(symbols)):
                if y==0:
                    print(' ' * int((a - i) / 2), symbols[y] * i, sep='', end='')
                else:
                    print(' ' * int((a - i)), symbols[y] * i, sep='',end='')
            print()

printRhombus(11, 3, "*","?")
