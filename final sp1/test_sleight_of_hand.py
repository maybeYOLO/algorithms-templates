from sleight_of_hand import trainer, NUM_PLAYERS

print(trainer(3 * NUM_PLAYERS, ['1231', '2..2', '2..2', '2..2']))   # 2
print(trainer(4 * NUM_PLAYERS, ['1111', '9999', '1111', '9911']))   # 1
print(trainer(4 * NUM_PLAYERS, ['1111', '1111', '1111', '1111']))   # 0