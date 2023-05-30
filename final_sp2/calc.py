# ID=87807618

from operator import add, sub, mul, floordiv

OPERATORS = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': floordiv
}


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
    stack = Stack()
    for token in expr.split():
        if token in OPERATORS:
            operand2nd = stack.pop()
            operand1st = stack.pop()
            result = OPERATORS[token](operand1st, operand2nd)
            stack.push(result)
        else:
            result = int(token)
            stack.push(result)
    return result


if __name__ == '__main__':
    print(calculate(input().strip()))
