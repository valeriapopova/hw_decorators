import datetime


def decorator(path):
    def dec(old_function):
        def new_function(*args, **kwargs):
            function_date = datetime.datetime.now()
            result = old_function(*args, **kwargs)
            with open(path, 'a',  encoding='utf-8') as file:
                file.write(f"\nНазвание функции: {old_function.__name__}\n")
                file.write(f"Дата и время вызова функции : {function_date}\n")
                file.write(f"Аргументы функции : {args}, {kwargs}\n")
                file.write(f"Возвращаемое значение: {result}\n")
            return result
        return new_function
    return dec


@decorator('func_log.txt')
def some_function(a, b):
    return a + b


print(some_function(2,9))


