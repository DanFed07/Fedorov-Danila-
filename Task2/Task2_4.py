data = input("Введите строку: ").lower().split()
sdata = set(data)
for i in sdata:
    c = data.count(i)
    print(i, c)