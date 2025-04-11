squares = [x**2 for x in range(1, 6)]
print(f"Квадраты первых 5 натуральных чисел: {squares}")

week = {name: i for i, name in enumerate(["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"])}
print(f"Дни недели: {week}")

tags = ["Django", "PYTHON", "C++", "c#", "Ruby", "Sobol"]
print(f"Теги библиотек в нижнем регистре: {{{' '.join(tag.lower() for tag in tags)}}}")

nums = [1, 3, 4, 87, 98, 15, 7, 4]
print(f"Чётные числа: {[num for num in nums if num % 2 == 0]}")

from math import factorial
print(f"Факториалы чисел: {{{', '.join(f'{i}: {factorial(i)}' for i in range(1, 6))}}}")
