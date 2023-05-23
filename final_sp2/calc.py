from typing import Union


class Stack():
    def __init__(self) -> None:
        self.data = []

    def push(self, value: int) -> None:
        self.data.append(value)

    def pop(self) -> int:
        return self.data.pop()

def calculate(expr: str) -> int:
    result = 0
    value = 0
    value_met = False
    minus_met = False
    stack = Stack()
    for symbol in expr + ' ':
        if symbol == '+':
            result = stack.pop() + stack.pop()
            stack.push(result)
        elif symbol == '-':
            minus_met = True
        elif symbol == '*':
            result = stack.pop() * stack.pop()
            stack.push(result)
        elif symbol == '/':
            op2 = stack.pop()
            result = stack.pop() // op2
            stack.push(result)
        elif '0' <= symbol <= '9':
            value = value * 10 + int(symbol)
            value_met = True
        elif symbol == ' ':
            if value_met:
                stack.push(-value if minus_met else value)
                value = 0
                value_met = False
            elif minus_met:
                result = -(stack.pop() - stack.pop())
                stack.push(result)
            minus_met = False
    return result


if __name__ == '__main__':
    print(calculate(input().strip()))
