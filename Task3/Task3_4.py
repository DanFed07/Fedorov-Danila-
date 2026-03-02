print("                                                                        44               44")
print("            LL      AA   DDDDD    AA       N   N II V   V  AA        44444   XX  XX   44444")
print("            LL     A__A  DD  DD  A__A      N N N II  V V  A__A      44444444   XX    44444444")
print("            LLLLL A    A DDDDD  A    A     N   N II   V  A    A         44   XX  XX      44")
print("")
print("                                   ###############################          ")
print("                                ##             ###              #####            ")
print("                              ##               ###                ######          ")
print("                          ####                 ###                 #######        ")
print("        ####################################################################      ")
print("      ####      #######################________##############################     ")
print("      #############################################################| 4x4 |##      ")
print("       ###           ####################################          ########       ")
print(" #######     ooooo    ################################     ooooo     ###### ####  ")
print("  #####  oooo     oooo  #############################  oooo     oooo  ##### ####  ")
print("        ooo          ooo ############################ ooo          ooo  #         ")
print("        ooo          ooo  #                           ooo          ooo  #         ")
print("         oooo      oooo   #                            oooo      oooo   #         ")
print("             oooooo                                        oooooo                 ")

from datetime import datetime


class LadaNiva:

    # Атрибуты класса (общие для всех экземпляров)
    manufacturer: str = "АвтоВАЗ"
    wheels_drive: str = "Постоянный полный (4x4)"

    def __init__(self, vin: str, color: str, year: int, mileage: float, engine_volume: float = 1.7):
        """
        Магический метод __init__ - инициализация атрибутов объекта
        engine_volume имеет значение по умолчанию 1.7, так как это самый распространенный объем для Нивы
        """
        self.vin = vin  # Уникальный идентификатор
        self.color = color
        self.year = year
        self.mileage = max(0, mileage)  # Пробег не может быть отрицательным
        self.engine_volume = engine_volume

    def __str__(self) -> str:
        """
        Магический метод __str__ - возвращает понятное строковое представление объекта
        Вызывается при print(объект) или str(объект)
        """
        return f"Lada Niva {self.year} года, цвет: {self.color}, пробег: {self.mileage} км"

    def get_info(self) -> str:
        """Метод возвращает полную информацию об автомобиле"""
        info = (
            f"Информация об автомобиле Lada Niva:\n"
            f"  VIN номер: {self.vin}\n"
            f"  Цвет: {self.color}\n"
            f"  Год выпуска: {self.year}\n"
            f"  Пробег: {self.mileage} км\n"
            f"  Объем двигателя: {self.engine_volume} л\n"
            f"  Производитель: {self.manufacturer}\n"
            f"  Привод: {self.wheels_drive}"
        )
        return info

    def paint(self, new_color: str) -> None:
        """Метод для перекраски автомобиля"""
        old_color = self.color
        self.color = new_color
        print(f"Автомобиль перекрашен из {old_color} в {new_color}")

    def update_mileage(self, km: float) -> None:
        """Метод для обновления пробега (только увеличение)"""
        if km < 0:
            print("Ошибка: пробег не может быть отрицательным!")
            return

        if km > self.mileage:
            old_mileage = self.mileage
            self.mileage = km
            print(f"Пробег обновлен: {old_mileage} км -> {self.mileage} км")
        else:
            print(f"Ошибка: cкручивание пробега")

    def is_old_timer(self) -> bool:
        """
        Метод проверяет, является ли автомобиль раритетным (старше 25 лет)
        Возвращает True или False
        """
        current_year = datetime.now().year
        age = current_year - self.year
        return age > 25


# Создаем несколько объектов (экземпляров) класса LadaNiva

print("=" * 50)
print("СОЗДАНИЕ ОБЪЕКТОВ")
print("=" * 50)

# Объект №1: Нива1
niva = LadaNiva(
    vin="XTA212100M1234567",
    color="Золото инков",
    year=2015,
    mileage=120000,
    engine_volume=1.7
)

# Объект №2: Нива2
niva2 = LadaNiva(
    vin="XTA212140K7654321",
    color="Табаско",
    year=2020,
    mileage=45000,
    engine_volume=1.7
)

# Объект №3: Старая Нива (используем значение engine_volume по умолчанию - 1.7)
old_niva = LadaNiva(
    vin="XTA212100T9876543",
    color="Капитан",
    year=1995,
    mileage=350000
)

# Объект №4: Еще одна Нива для демонстрации разных цветов
another_niva = LadaNiva(
    vin="XTA212100A1122334",
    color="Снежно-белый",
    year=2018,
    mileage=75000
)

print("Объекты успешно созданы!\n")

# Демонстрация работы методов
print("=" * 50)
print("ПОКАЗ РАБОТЫ МЕТОДОВ")
print("=" * 50)

# Демонстрируем __str__ метод
print("1. __str__ метода:")
print(str(niva))
print(niva2)  # Можно просто передать объект в print
print(old_niva)
print()

# Демонстрируем get_info()
print("2. get_info():")
print(niva.get_info())
print()

# Демонстрируем paint()
print("3. paint():")
print(f"Текущий цвет niva: {niva.color}")
niva.paint("Матовый хаки")
print(f"Новый цвет niva: {niva.color}")
print()

# Демонстрируем update_mileage()
print("4. update_mileage():")
print(f"Текущий пробег niva2: {niva2.mileage} км")
niva2.update_mileage(50000)  # Нормальное увеличение
print(f"Пробег после поездки: {niva2.mileage} км")
print()
niva2.update_mileage(30000)  # Попытка скрутить пробег
print(f"Пробег после попытки скрутить: {niva2.mileage} км")
print()

# Демонстрируем is_old_timer()
print("5. is_old_timer():")
print(f"niva ({niva.year} года) - старше 25? {niva.is_old_timer()}")
print(f"old_niva ({old_niva.year} года) - старше 25? {old_niva.is_old_timer()}")
print()

# Демонстрируем атрибуты класса
print("=" * 50)
print("АТРИБУТЫ КЛАССА (общие для всех машин)")
print("=" * 50)
print(f"Производитель: {LadaNiva.manufacturer}")
print(f"Привод: {LadaNiva.wheels_drive}")
print()

# Показываем, что атрибуты класса действительно общие
print("Все наши Нивы имеют:")
print(f"  niva: {niva.manufacturer}, {niva.wheels_drive}")
print(f"  niva2: {niva2.manufacturer}, {niva2.wheels_drive}")
print(f"  old_niva: {old_niva.manufacturer}, {old_niva.wheels_drive}")

print("\n" + "=" * 50)
print("ИТОГОВАЯ ИНФОРМАЦИЯ ОБО ВСЕХ МАШИНАХ")
print("=" * 50)

# Собираем все машины в список и выводим информацию
all_nivas = [niva, niva2, old_niva, another_niva]
for i, niva in enumerate(all_nivas, 1):
    print(f"\nМашина #{i}:")
    print(niva)  # Будет вызван __str__ метод
    print(f"Старая: {'Да' if niva.is_old_timer() else 'Нет'}")