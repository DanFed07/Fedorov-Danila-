print("Возведение в степень. Для выхода введите: exit")
data = input("Введите числа через пробел: ")
b = True
while b:
    #Проверка на выход
    if data == "exit":
        b = False
        break
    lst = []
    lst = data.split()
    l = input("Введите степень: ")
    c = 0
    print("Вывод:", end=" ")
    test = True
    while c < len(lst):
        num = lst[c]
        if l.isdigit():
            level = int(l)
            if num.isdigit() or num.lstrip('-').isdigit():
                h = int(num) ** level
                print(h, end=" ")
            else :
                h = num * level
                print(h, end=" ")
        elif l.lstrip('-').isdigit():
            level = int(l)
            if num.isdigit() or num.lstrip('-').isdigit():
                r = 1 / level
                h = int(num) ** level
                print("{:.2f}".format(h), end=" ")
            else :
                print("o_O", end=" ")
        else:
            test = False
        c = c + 1
    if test == False:
        print("Введено не число для степени", end=" ")
    data = input("\nВведите числа через пробел: ")