""""Помогите Васе понять, будет ли фраза палиндромом‎. Учитываются только буквы и цифры, заглавные и строчные буквы считаются одинаковыми.

Решение должно работать за O(N), где N — длина строки на входе.

Формат ввода
В единственной строке записана фраза или слово. Буквы могут быть только латинские. Длина текста не превосходит 20000 символов.

Фраза может состоять из строчных и прописных латинских букв, цифр, знаков препинания.

Формат вывода
Выведите «True», если фраза является палиндромом, и «False», если не является."""

def is_palindrome(line: str) -> bool:
    line = line.upper()
    good_chars = 'ABCDEFGHIJKLMOPQRSTUVWXYZ0123456789'
    result = True
    head = 0
    max_length = len(line) - 1
    tail = max_length
    while head <= max_length:
        while head <= max_length and line[head] not in good_chars:
            head += 1
        while tail >= 0 and line[tail] not in good_chars:
            tail -= 1
        if head <= max_length and line[head] != line[tail]:
            result = False
            head = max_length
        head += 1
        tail -= 1
    return result


print(is_palindrome(input().strip()))
