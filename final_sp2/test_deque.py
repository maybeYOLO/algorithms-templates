"""
Гоша реализовал структуру данных Дек, максимальный размер которого определяется заданным числом.
Методы push_back(x), push_front(x), pop_back(), pop_front() работали корректно.
Но, если в деке было много элементов, программа работала очень долго.
Дело в том, что не все операции выполнялись за O(1). Помогите Гоше! Напишите эффективную реализацию.

Внимание: при реализации используйте кольцевой буфер.

Формат ввода
В первой строке записано количество команд n — целое число, не превосходящее 100000.
Во второй строке записано число m — максимальный размер дека. Он не превосходит 50000.
В следующих n строках записана одна из команд:

push_back(value) – добавить элемент в конец дека.
Если в деке уже находится максимальное число элементов, вывести «error».
push_front(value) – добавить элемент в начало дека.
Если в деке уже находится максимальное число элементов, вывести «error».
pop_front() – вывести первый элемент дека и удалить его. Если дек был пуст, то вывести «error».
pop_back() – вывести последний элемент дека и удалить его. Если дек был пуст, то вывести «error».
Value — целое число, по модулю не превосходящее 1000.
Формат вывода
Выведите результат выполнения каждой команды на отдельной строке.
Для успешных запросов push_back(x) и push_front(x) ничего выводить не надо.
"""
from deque import Deque, process_command, print_result

print('Пример 1. Ожидаемый вывод: 861 -819')
deque = Deque(4)
print_result(process_command(deque, 'push_front 861'))
print_result(process_command(deque, 'push_front -819'))
print_result(process_command(deque, 'pop_back'))        # 861
print_result(process_command(deque, 'pop_back'))        # -819

print('Пример 2. Ожидаемый вывод: -855 0 844')
deque = Deque(10)
print_result(process_command(deque, 'push_front -855'))
print_result(process_command(deque, 'push_front 0'))
print_result(process_command(deque, 'pop_back'))        # -855
print_result(process_command(deque, 'pop_back'))        # 0
print_result(process_command(deque, 'push_back 844'))
print_result(process_command(deque, 'pop_back'))        # 844
print_result(process_command(deque, 'push_back 823'))

print('Пример 3. Ожидаемый вывод: 20 102')
deque = Deque(6)
print_result(process_command(deque, 'push_front -201'))
print_result(process_command(deque, 'push_back 959'))
print_result(process_command(deque, 'push_back 102'))
print_result(process_command(deque, 'push_front 20'))
print_result(process_command(deque, 'pop_front'))       # 20
print_result(process_command(deque, 'pop_back'))        # 102
