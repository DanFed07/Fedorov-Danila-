def add(text, filename):
    with open(filename, "a", encoding="utf-8") as file:
        file.write(f"\n{text}")
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()
        print(f"\nЧётные строки файла {filename}:")
        for i in range(1, len(lines), 2):
            print(lines[i].strip())

text = input("Введите что добавить: ")
f = input("Введите название файла: ")

add(text, f)