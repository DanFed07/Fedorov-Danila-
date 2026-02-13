print("Проверка возраста. Для выхода введите: exit")
c = True
while c:
    age = input("Введите ваш возраст: ")
    if age == "exit":
        c = False
        break

    for i in age:
        if i in "-0123456789":
            b = True
        else:
            b = False
            break

    if b == True:
        number = int(age)
        if number >= 18:
            print("Вы совершеннолетний.")
        elif 0 < number < 18:
            print("Вы несовершеннолетний.")
        elif number < 0:
            print("Ошибка: возраст не может быть отрицательным!")
    else:
        print("Ошибка: введено не число!")