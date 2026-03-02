print("Калькулятор. Для выхода введите: exit")
print(" ________________________")
print("|              CALCULATOR|")
print("|------------------------|")
print("|  +  |  -  |  *   |  /  |")
print("|-----|-----|------|-----|")
print("|  !  |  ^  |  √   |  %  |")
print(" ------------------------ ")

separator = "--------------------------"

# Проверка типов данных с помощью isinstance (требование задания)
def checknum(*args):
    for arg in args:
        if not isinstance(arg, (int, float)):
            raise TypeError(f"Ошибка: {arg} не является числом!")

# Проверка, является ли операция бинарной (требует два аргумента)
def testoperation(operation): return operation in "+-*/^√"

# Проверка, определена ли операция вообще
def testvaloper(operation):
    return operation in ["+", "-", "*", "/", "!", "^", "√", "%"]

# Проверка корректности введенного числа (формат, минусы, разделители)
def testvalnum(number):
    if not number:
        print(separator)
        print("Введено не число")
        return False

    if '-' in number and number[0] != '-':
        print(separator)
        print("Минус должен быть в начале!")
        return False

    if number.count('-') > 1:
        print(separator)
        print("Минус должен быть один!")
        return False

    if (number.count('.') > 1) or (number.count(',') > 1):
        print(separator)
        print("Должен быть только один разделитель (точка или запятая)!")
        return False

    checkdot = '.' in number
    checkcomma = ',' in number

    if number[0] == '-':
        part = number[1:]
    else:
        part = number

    # Проверка целого числа
    if part.isdigit():
        return True

    # Проверка дробного числа
    if checkdot or checkcomma:
        if checkdot:
            p = part.split('.')
        else:
            p = part.split(',')

        # Проверяем, что обе части состоят из цифр
        if len(p) == 2 and p[0].isdigit() and p[1].isdigit():
            return True

    print(separator)
    print("Введено не число")
    return False

# Арифметические операции
def add(x1, x2):
    checknum(x1, x2)
    return x1 + x2

def sub(x1, x2):
    checknum(x1, x2)
    return x1 - x2

def mul(x1, x2):
    checknum(x1, x2)
    return x1 * x2

def pow(x1, x2):
    checknum(x1, x2)
    return x1 ** x2

def procent(x1):
    checknum(x1)
    return x1 / 100

def div(x1, x2):
    checknum(x1, x2)
    if x2 == 0:
        raise ZeroDivisionError("Делить на 0 нельзя!")
    return x1 / x2

# Корень степени N (первое число - число, второе - степень корня)
def sqrt(x1, x2):
    checknum(x1, x2)
    if x2 == 0:
        raise ZeroDivisionError("Степень корня не может быть 0!")
    if x2 < 0:
        raise ValueError("Степень корня должна быть положительной!")
    if x1 < 0:
        if x2 % 2 == 0:
            raise ValueError("Корень четной степени из отрицательного числа не существует!")
        return -(abs(x1) ** (1 / x2))
    if 0 < x2 < 1:
        return pow(x1, x2)
    return x1 ** (1 / x2)

# Факториал числа
def factorial(x1):
    checknum(x1)
    x = int(x1)
    if x != x1:
        raise ValueError("Факториал определен только для целых чисел")
    if x < 0:
        raise ValueError("Факториал определен только для положительных чисел")
    if x <= 1:
        return 1

    result = 1
    for i in range(2, x + 1):
        result *= i
    return result

# Выбор бинарной операции
def operations(x1, x2, operation):
    if operation == "+": return add(x1, x2)
    if operation == "-": return sub(x1, x2)
    if operation == "*": return mul(x1, x2)
    if operation == "/": return div(x1, x2)
    if operation == "^": return pow(x1, x2)
    if operation == "√": return sqrt(x1, x2)

# Выбор унарной операции
def operate(x1, operation):
    if operation == "%": return procent(x1)
    if operation == "!": return factorial(x1)

# Получение числа от пользователя с проверкой
def getnumber(prompt):
    num = input(prompt)

    if not testvalnum(num):
        return None

    # Замена запятой на точку для преобразования в float
    if ',' in num:
        nd = ''
        for i in num:
            if i == ',':
                nd += '.'
            else:
                nd += i
        return float(nd)
    else:
        return float(num)

# Обработка бинарной операции (с двумя аргументами)
def processbinary(x1, operation):
    x2 = getnumber("X2: ")
    if x2 is None:
        return

    print(separator)
    try:
        print(">>> ", "{:.2f}".format(operations(x1, x2, operation)))
    except (ZeroDivisionError, ValueError) as e:
        print(e)

# Обработка унарной операции (с одним аргументом)
def processunary(x1, operation):
    print(separator)
    try:
        print(">>> ", "{:.2f}".format(operate(x1, operation)))
    except ValueError as e:
        print(e)

# Главный цикл программы
def main():
    while True:
        operation = input("Операция: ")

        if operation == "exit":
            break

        if not testvaloper(operation):
            print(separator)
            print("Операция не определена")
            print(separator)
            continue

        x1 = getnumber("X1: ")
        if x1 is None:
            print(separator)
            continue

        if testoperation(operation):
            processbinary(x1, operation)
        else:
            processunary(x1, operation)

        print(separator)

if __name__ == "__main__":
    main()