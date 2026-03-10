def genfunc(n):
    c = 0
    num = 2
    while c < n:
        b = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                b = False
                break
        if b:
            yield num
            c +=1
        num +=1

print('\n'.join(str(x) for x in genfunc(10)))