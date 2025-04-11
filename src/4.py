def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"Функция {func.__name__} вызванс аргументом:")
        print(f"1 аргумент: {args}")
        print(f"2 аргумент: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Площадь прямоугольника: {result}")
        return result

    return wrapper


def calculate_area(length, width):
    return length * width


# Применяем декоратор вручную
calculate_area = log_call(calculate_area)

# Вызов
calculate_area(10, 50)
