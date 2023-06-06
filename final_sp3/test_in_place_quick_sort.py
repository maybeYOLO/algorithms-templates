from in_place_quick_sort import in_place_quick_sort

print('Пример 1. Ожидается gena timofey alla gosha rita')
participants = [
    ['alla', 4, 100],
    ['gena', 6, 1000],
    ['gosha', 2, 90],
    ['rita', 2, 90],
    ['timofey', 4, 80],
]
in_place_quick_sort(participants)
for participant in participants:
    print(participant[0])

print('Пример 2. Ожидается alla gena gosha rita timofey')
participants = [
    ['alla', 0, 0],
    ['gena', 0, 0],
    ['gosha', 0, 0],
    ['rita', 0, 0],
    ['timofey', 0, 0],
]
in_place_quick_sort(participants)
for participant in participants:
    print(participant[0])

print('Тест 3. Ожидается timofey rita gosha gena alla')
participants = [
    ['alla', 0, 10],
    ['gena', 0, 9],
    ['gosha', 0, 8],
    ['rita', 0, 7],
    ['timofey', 0, 0],
]
in_place_quick_sort(participants)
for participant in participants:
    print(participant[0])
