"""
Задание связано с обратной польской нотацией. Она используется для парсинга арифметических выражений.
Еще её иногда называют постфиксной нотацией.

В постфиксной нотации операнды расположены перед знаками операций.

Пример 1:
3 4 +
означает 3 + 4 и равно 7

Пример 2:
12 5 /
Так как деление целочисленное, то в результате получим 2.

Пример 3:
10 2 4 * -
означает 10 - 2 * 4 и равно 2

Разберём последний пример подробнее:

Знак * стоит сразу после чисел 2 и 4, значит к ним нужно применить операцию,
которую этот знак обозначает, то есть перемножить эти два числа. В результате получим 8.

После этого выражение приобретёт вид:

10 8 -

Операцию «минус» нужно применить к двум идущим перед ней числам, то есть 10 и 8. В итоге получаем 2.

Рассмотрим алгоритм более подробно. Для его реализации будем использовать стек.

Для вычисления значения выражения, записанного в обратной польской нотации,
нужно считывать выражение слева направо и придерживаться следующих шагов:

Обработка входного символа:
Если на вход подан операнд, он помещается на вершину стека.
Если на вход подан знак операции, то эта операция выполняется над требуемым количеством значений,
взятых из стека в порядке добавления. Результат выполненной операции помещается на вершину стека.
Если входной набор символов обработан не полностью, перейти к шагу 1.
После полной обработки входного набора символов результат вычисления выражения находится в вершине стека.
Если в стеке осталось несколько чисел, то надо вывести только верхний элемент.
Замечание про отрицательные числа и деление:
в этой задаче под делением понимается математическое целочисленное деление.
Это значит, что округление всегда происходит вниз.
А именно: если a / b = c, то b ⋅ c — это наибольшее число,
которое не превосходит a и одновременно делится без остатка на b.

Например, -1 / 3 = -1. Будьте осторожны: в C++, Java и Go, например, деление чисел работает иначе.

В текущей задаче гарантируется, что деления на отрицательное число нет.

Формат ввода
В единственной строке дано выражение, записанное в обратной польской нотации.
Числа и арифметические операции записаны через пробел.

На вход могут подаваться операции: +, -, *, / и числа, по модулю не превосходящие 10000.

Гарантируется, что значение промежуточных выражений в тестовых данных по модулю не больше 50000.

Формат вывода
Выведите единственное число — значение выражения.
"""
from calc import calculate

print(calculate('2 1 + 3 *'))       # 9
print(calculate('7 2 + 4 * 2 +'))   # 38
