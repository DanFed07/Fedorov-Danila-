print("Четность числа. Для выхода введите: exit")
c = True
while c:
    num = input("Введите число: ")
    if num == "exit":
        c = False
        break

    for i in num:
        if i == "0" or i == "1" or i == "2" or i == "3" or i == "4" or i == "5" or i == "6" or i == "7" or i == "8" or i == "9":
            b = True
        else:
            b = False
            break

    if b == True:
        number = int(num)
        if (number % 2) == 0:
            print(f"Число {number} является четным")
        else:
            print(f"Число {number} не является четным")
    else:
        print("Ошибка: введено не число")

