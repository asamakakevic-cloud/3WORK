def function_name(search, status, *args, **kwargs):
    result = []
    result_2 = ""

    if search == "args":
        if status:
            for i in args:
                if isinstance(i, int):
                    result.append(i)
            return result
        else:
            for i in args:
                result_2 = result_2 + str(i)
            return result_2
    elif search == "kwargs":
        for k, v in kwargs.items():
            result_2 = result_2 + f"Key: {k}, Value: {v}; "
        return result_2
    else:
        raise ValueError("Error for search")

print(function_name("args", True, 1, 2, 3, 4, "hello", 5.5))
print(function_name("args", False, 1, 2, 3, "привет"))
print(function_name("kwargs", True, name="Анна", age=20, city="Москва"))