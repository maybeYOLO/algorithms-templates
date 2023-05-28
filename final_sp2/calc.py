# ID=87769572

from typing import Union
from operator import add, sub, mul, floordiv

OPERATORS = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': floordiv
}
ORD_TO_INT = ord('0')


class Stack():
    def __init__(self) -> None:
        self.data = []

    def push(self, value: int) -> None:
        self.data.append(value)

    def pop(self) -> int:
        if len(self.data) == 0:
            raise StackUnderflowException('Исчерпание стека')
        return self.data.pop()


class StackUnderflowException(Exception):
    pass


def calculate(expr: str) -> int:
    result = 0
    value = 0
    value_met = False
    minus_met = False
    operator_met = False
    symbol_operator = ''
    stack = Stack()
    """
    Действие выполняется когда после числа или оператора встречается пробел
    Для выполнения действия над последним числом или оператором,
    к выражению добавляется оконечный пробел
    """
    for symbol in expr + ' ':
        if symbol in OPERATORS:
            operator_met = True
            symbol_operator = symbol
            if symbol == '-':
                minus_met = True
        elif '0' <= symbol <= '9':
            value = value * 10 + ord(symbol) - ORD_TO_INT
            value_met = True
        elif symbol == ' ':
            if value_met:
                result = -value if minus_met else value
                stack.push(result)
                value = 0
                value_met = False
            elif operator_met:
                operand2nd = stack.pop()
                operand1st = stack.pop()
                result = OPERATORS[symbol_operator](operand1st, operand2nd)
                stack.push(result)
            operator_met = False
            minus_met = False
    return result


if __name__ == '__main__':
    print(calculate(input().strip()))
