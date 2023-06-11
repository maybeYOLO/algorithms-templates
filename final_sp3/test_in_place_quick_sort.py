from in_place_quick_sort import in_place_quick_sort, Participant

print('Пример 1. Ожидается\ngena timofey alla gosha rita')
participants = [
    Participant('alla', 4, 100),
    Participant('gena', 6, 1000),
    Participant('gosha', 2, 90),
    Participant('rita', 2, 90),
    Participant('timofey', 4, 80),
]
in_place_quick_sort(participants)
print(' '.join(map(lambda x: x.name, participants)))

print('Пример 2. Ожидается\nalla gena gosha rita timofey')
participants = [
    Participant('alla', 0, 0),
    Participant('gena', 0, 0),
    Participant('gosha', 0, 0),
    Participant('rita', 0, 0),
    Participant('timofey', 0, 0),
]
in_place_quick_sort(participants)
print(' '.join(map(lambda x: x.name, participants)))

print('Тест 3. Ожидается\ntimofey rita gosha gena alla')
participants = [
    Participant('alla', 0, 10),
    Participant('gena', 0, 9),
    Participant('gosha', 0, 8),
    Participant('rita', 0, 7),
    Participant('timofey', 0, 0),
]
in_place_quick_sort(participants)
print(' '.join(map(lambda x: x.name, participants)))
