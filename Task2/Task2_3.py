data1 = set(input("Введите первый список: ").split())
data2 = set(input("Введите второй список: ").split())
print("Общие элементы: ", " ".join(data1 & data2))