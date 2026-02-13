print("Длина числа. Для выхода введите: exit")

while True:
    num = input("Введите число: → ")
    if num == "exit":
        break

    if num.isdigit():
        print("В этом числе ", len(num))
    elif num.lstrip('-').isdigit():
        print("В этом числе ", len(num) - 1)
    else:
        print("Ошибка: данные не являются числом.")
