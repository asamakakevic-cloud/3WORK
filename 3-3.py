from typing import Any, Union, List

def function_name(search: str, status: bool, *args: Any, **kwargs: Any) -> Union[List[int], str]:
    """
    Обрабатывает аргументы в зависимости от параметров search и status.

    Параметры:
    ----------
    search: str
        Определяет тип обрабатываемых аргументов. Может быть "args" или "kwargs"
    status: bool
        Определяет режим обработки для аргументов типа args
    *args: Any
        Произвольное количество позиционных аргументов
    **kwargs: Any
        Произвольное количество именованных аргументов

    Возвращаемое значение:
    ---------------------
    Union[List[int], str]
        - Если search == "args" и status == True: список целых чисел из args
        - Если search == "args" и status == False: строка из всех args
        - Если search == "kwargs": строка с информацией о ключах и значениях kwargs

    Исключения:
    -----------
    ValueError
        Если search не равен "args" или "kwargs"
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
            result_2 += f"Key: {k}, Value: {v}; "
        return result_2
    else:
        raise ValueError("Error for search")
