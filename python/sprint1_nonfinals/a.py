def evaluate_function(a: int, b: int, c: int, x: int) -> int:
    # Здесь реализация вашего решения
    pass

    # Вася делает тест по математике: вычисляет значение функций в различных точках. Стоит отличная погода, и друзья зовут Васю гулять. Но мальчик решил сначала закончить тест и только после этого идти к друзьям. К сожалению, Вася пока не умеет программировать. Зато вы умеете. Помогите Васе написать код функции, вычисляющей y = ax2 + bx + c. Напишите программу, которая будет по коэффициентам a, b, c и числу x выводить значение функции в точке x.

    # Формат ввода
    # На вход через пробел подаются целые числа a, x, b, c. В конце ввода находится перенос строки.

    # Формат вывода
    # Выведите одно число — значение функции в точке x.

a, x, b, c = map(int, input().strip().split())
print(evaluate_function(a, b, c, x))
