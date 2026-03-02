from typing import Any, Union, List


def function_name(
        search: str,
        status: bool,
        *args: Any,
        **kwargs: Any) -> Union[List[int], str]:
    """
       Функция обрабатывает аргументы в зависимости от параметров search и status. Она может работать в двух режимах:
       1. "args":
          - Если status=True: возвращает список только целых чисел
          - Если status=False: возвращает строку из всех аргументов
       2. "kwargs":
          - Возвращает строку с парами "Key: Value"
       Параметры:
       - search : str
           - "args" - обработка позиционных аргументов
           - "kwargs" - обработка именованных аргументов
       - status : bool
           Статус обработки (используется только в режиме "args"):
           - True - вернуть список целых чисел
           - False - вернуть строку из всех аргументов
       - *args : Any  - Произвольное количество позиционных аргументов
       - **kwargs : Any  - Произвольное количество именованных аргументов

       Union[List[int], str] - возвращаемое значение, работает в режимах:
           - "args" и status=True: список целых чисел (List[int])
           - "args" и status=False: строка (str)
           - "kwargs": строка с парами ключ-значение (str)
           - В случае ошибки применяется исключение
       Исключение ValueError применяется, если параметр search не равен "args" или "kwargs"
       """
    result: List[int] = []
    result_2: str = ""
    if search == "args":
        if status:
            for i in args:
                if isinstance(i, int):
                    result.append(i)
            return result
        else:
            for i in args:
                result_2 += f"{i}"
            return result_2
    elif search == "kwargs":
        for k, v in kwargs.items():
            result_2 += ("Key: {}, Value: {}; ".format(k, v))
        return result_2
    else:
        raise ValueError("Error for search")

