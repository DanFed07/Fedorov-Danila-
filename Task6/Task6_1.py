def average_num(list_num: list) -> float:
    for ind, el in enumerate(list_num):
        if not isinstance(el, int | float):
            try:
                list_num[ind] = int(el)
            except:
                return "Bad request"
    return round(sum(list_num) / len(list_num), 2)

assert average_num([2, 2]) == 2
assert average_num([2.5, 3.2]) == 2.85

assert average_num(["1", "3", "2"]) == 2
assert average_num(["4", "4"]) == 4

assert average_num(["1", "abc", "2"]) == "Bad request"
assert average_num(["x", "y", "z"]) == "Bad request"
# None не преобразуется в число
assert average_num([1, None, 3]) == "Bad request"
# Список в списке
assert average_num([1, [2], 3]) == "Bad request"

assert average_num(["  42  "]) == 42
assert average_num([6, "-3", -3]) == 0

#print(f"3.175 в памяти: {average_num([2.5, 3.85]):.20f}")
assert average_num([2.5, 3.85]) == 3.17 #3.175 ~ 3.18

assert average_num([True, False, True]) == 0.67
'''
Потому что в bool в Python - это подтип int: True=1, False=0
Функция увидит bool как int и не будет преобразовывать
'''
#assert average_num([])
'''
assert average_num([]) ~ ZeroDivisionError: division by zero
Потому что:
sum([]) = 0
len([]) = 0
0 / 0 → ZeroDivisionError!
'''