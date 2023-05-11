def get_longest_word(line: str) -> str:
   max_word = ''
   max_length = len(max_word)
   words = line.split()
   for word in words:
       if len(word) > max_length:
           max_word = word
           max_length =len(word)
   return max_word 

def read_input() -> str:
    _ = input()
    line = input().strip()
    return line

def print_result(result: str) -> None:
    print(result)
    print(len(result))

print_result(get_longest_word(read_input()))
