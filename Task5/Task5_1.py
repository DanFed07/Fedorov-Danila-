import string
import random
from pathlib import Path

# создание случайного имя
def genranname(lenght  = 8):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(lenght))

# создание случайных файлов
def genranfile(directory, count = 10, extension = ".txt"):
    path = Path(directory)
    path.mkdir(parents = True, exist_ok = True)
    fullpath = []
    for _ in range(count):
        name = genranname() + extension
        filepath =path / name
        filepath.touch()
        print(filepath.absolute())
        fullpath.append(filepath)
    return fullpath

def main():
    # C:\Users\shora\PycharmProjects\PythonProject3
    directory = input("Введите путь к директории: ")
    files = genranfile(directory)

if __name__ == "__main__":
    main()