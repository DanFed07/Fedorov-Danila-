print("Умножение элементов списка на множитель. Для выхода введите: exit")
while True:
    data = input("Введите список чисел через пробел: ")
    if data == "exit":
        break
    l = []
    l = data.split()
    multiplier = input("Введите множитель (по умолчанию 2): ")
    m = 0
    test1 = True
    if multiplier == "":
        m = 2
    elif multiplier.isdigit() or multiplier.lstrip("-").isdigit():
        m = int(multiplier)
    else:
        test1 = False
    c = 0
    test2 = True
    lnum = []
    listfun = []
    while c < len(l):
        d = l[c]
        if d.isdigit() or d.lstrip("-").isdigit():
            if test2 == True:
                listfun.append(int(d)  * m)
            lnum.append(int(d))
        else:
            test2 = False
        c+=1
    if test1 == False and test2 == False:
        print("Введены не числа")
    elif test1 == False:
        print("Введено не число для множителя")
    elif test2 == False:
        print("Введено(ы) не число(а)")
    elif test1 == True and test2 == True:
        print("Результат (функция):", listfun)
        print("Результат (лямбда-функция): ", list(map(lambda x: x * m, lnum)))