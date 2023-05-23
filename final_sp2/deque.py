from typing import List, Tuple, Union


def process_command(deque: List[int], command: str) -> Union[str, None]:
    pass


def print_result(result: Union[str, None]) -> None:
    if not result is None:
        print(result)


if __name__ == '__main__':


    def read_input() -> None:
        command_count = int(input())
        deque_size = int(input())
        deque = [0] * deque_size
        for _ in range(command_count):
            print_result(process_command(deque, input().strip()))


    read_input()
