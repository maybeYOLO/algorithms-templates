# ID=87726607

from typing import Union


class Deque:
    def __init__(self, deque_size):
        self.data = [0] * deque_size
        self.size = deque_size
        self.head = 1
        self.tail = 0
        self.count = 0

    def _increment_index(self, index: int) -> int:
        return (index + 1) % self.size

    def _decrement_index(self, index: int) -> int:
        return index - 1 if index > 0 else self.size - 1

    def push_front(self, value: int) -> None:
        if self.count == self.size:
            raise DequeOverflowException('Дек переполнен с головы')
        self.head = self._decrement_index(self.head)
        self.data[self.head] = value
        self.count += 1

    def push_back(self, value: int) -> None:
        if self.count == self.size:
            raise DequeOverflowException('Дек переполнен с хвоста')
        self.tail = self._increment_index(self.tail)
        self.data[self.tail] = value
        self.count += 1

    def pop_front(self) -> int:
        if self.count == 0:
            raise DequeUnderflowException('Дек исчерпан с головы')
        value: int = self.data[self.head]
        self.head = self._increment_index(self.head)
        self.count -= 1
        return value

    def pop_back(self) -> int:
        if self.count == 0:
            raise DequeUnderflowException('Дек исчерпан с хвоста')
        value: int = self.data[self.tail]
        self.tail = self._decrement_index(self.tail)
        self.count -= 1
        return value


class DequeOverflowException(Exception):
    pass


class DequeUnderflowException(Exception):
    pass


def process_command(deque: Deque, command: str) -> Union[int, str, None]:
    result = None
    method, *params = command.split()
    try:
        result = getattr(deque, method)(*params)
    except:
        result = 'error'
    return result


def print_result(result: Union[int, str, None]) -> None:
    if not result is None:
        print(result)


if __name__ == '__main__':


    def read_input() -> None:
        command_count = int(input())
        deque_size = int(input())
        deque = Deque(deque_size)
        for _ in range(command_count):
            print_result(process_command(deque, input().strip()))


    read_input()
