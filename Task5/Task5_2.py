import math
import random
import statistics

# создание списка случайных чисел
def ranumgen(count):
    return [random.randint(1,100) for _ in range(count)]

def calculate(numbers):
    mean = statistics.mean(numbers)
    median = statistics.median(numbers)
    stdev = round(statistics.stdev(numbers), 2)
    sqrtsum = round(math.sqrt(sum(numbers)), 2)
    print(f"Список чисел: {numbers};"
             f"\nСреднее: {mean};\nМедиана: {median};"
             f"\nСтандартное отклонение: {stdev};"
             f"\nКорень из суммы: {sqrtsum}.")

def main():
    count = int(input("Введите количество чисел: "))
    calculate(ranumgen(count))

if __name__ == '__main__':
    main()