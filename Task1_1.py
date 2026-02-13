name = input("Ваше имя: ")
surname  = input("Фамилия: ")
age = int(input("Возраст: "))

if 11 <= age % 100 <= 14:
    year = "лет"
elif age % 10 == 1:
    year = "год"
elif 2 <= age % 10 <= 4:
    year = "года"
else:
    year = "лет"

#format
print("\nРеализация через format")
print("Ваше имя: {}, Фамилия: {}, Возраст: {} {}".format(name, surname, age, year))

#f-string
print("\nРеализация через f-string")
print(f"Ваше имя: {name}, Фамилия: {surname}, Возраст: {age} {year}")