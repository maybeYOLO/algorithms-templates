# ID=87620780

from typing import Union


class Deque:
    def __init__(self, deque_size):
        self.data = [0] * deque_size
        self.size = deque_size
        self.head = 1
        self.tail = 0
        self.count = 0

    def _increment_index(self, index: int) -> int:
        return index + 1 if index < self.size - 1 else 0

    def _decrement_index(self, index: int) -> int:
        return index - 1 if index > 0 else self.size - 1

    def push_front(self, value: int) -> Union[str, None]:
        if self.count == self.size:
            return 'error'
        self.head = self._decrement_index(self.head)
        self.data[self.head] = value
        self.count += 1

    def push_back(self, value: int) -> Union[str, None]:
        if self.count == self.size:
            return 'error'
        self.tail = self._increment_index(self.tail)
        self.data[self.tail] = value
        self.count += 1

    def pop_front(self) -> Union[int, str]:
        if self.count == 0:
            return 'error'
        value: int = self.data[self.head]
        self.head = self._increment_index(self.head)
        self.count -= 1
        return value

    def pop_back(self) -> Union[int, str]:
        if self.count == 0:
            return 'error'
        value: int = self.data[self.tail]
        self.tail = self._decrement_index(self.tail)
        self.count -= 1
        return value


def process_command(deque: Deque, command: str) -> Union[int, str, None]:
    result = None
    parts = command.split()
    if parts[0] == 'push_front':
        result = deque.push_front(int(parts[1]))
    elif parts[0] == 'push_back':
        result = deque.push_back(int(parts[1]))
    elif parts[0] == 'pop_front':
        result = deque.pop_front()
    elif parts[0] == 'pop_back':
        result = deque.pop_back()
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
