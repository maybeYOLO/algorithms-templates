NAME_INDEX = 0
SCORE_INDEX = 1
PENALTY_INDEX = 2


def nums_gt(left_value, right_value) -> bool:
    return left_value[SCORE_INDEX] > right_value[SCORE_INDEX] or (
        left_value[SCORE_INDEX] == right_value[SCORE_INDEX]
        and (left_value[PENALTY_INDEX] < right_value[PENALTY_INDEX] or (
            left_value[PENALTY_INDEX] == right_value[PENALTY_INDEX]
            and left_value[NAME_INDEX] < right_value[NAME_INDEX]
        ))
    )


def nums_ge(left_value, right_value) -> bool:
    return left_value[SCORE_INDEX] > right_value[SCORE_INDEX] or (
        left_value[SCORE_INDEX] == right_value[SCORE_INDEX]
        and (left_value[PENALTY_INDEX] < right_value[PENALTY_INDEX] or (
            left_value[PENALTY_INDEX] == right_value[PENALTY_INDEX]
            and left_value[NAME_INDEX] <= right_value[NAME_INDEX]
        ))
    )


assert nums_gt(['a', 5, 7], ['a', 4, 8])
assert nums_gt(['a', 5, 7], ['a', 5, 8])
assert nums_gt(['a', 5, 7], ['a', 6, 8]) == False
assert nums_gt(['a', 5, 8], ['a', 4, 8])
assert nums_gt(['a', 5, 8], ['a', 5, 8]) == False
assert nums_gt(['a', 5, 8], ['a', 6, 8]) == False
assert nums_gt(['a', 5, 9], ['a', 4, 8])
assert nums_gt(['a', 5, 9], ['a', 5, 8]) == False
assert nums_gt(['a', 5, 9], ['a', 6, 8]) == False

assert nums_gt(['a', 5, 7], ['b', 4, 8])
assert nums_gt(['a', 5, 7], ['b', 5, 8])
assert nums_gt(['a', 5, 7], ['b', 6, 8]) == False
assert nums_gt(['a', 5, 8], ['b', 4, 8])
assert nums_gt(['a', 5, 8], ['b', 5, 8])
assert nums_gt(['a', 5, 8], ['b', 6, 8]) == False
assert nums_gt(['a', 5, 9], ['b', 4, 8])
assert nums_gt(['a', 5, 9], ['b', 5, 8]) == False
assert nums_gt(['a', 5, 9], ['b', 6, 8]) == False

assert nums_gt(['b', 5, 7], ['a', 4, 8])
assert nums_gt(['b', 5, 7], ['a', 5, 8])
assert nums_gt(['b', 5, 7], ['a', 6, 8]) == False
assert nums_gt(['b', 5, 8], ['a', 4, 8])
assert nums_gt(['b', 5, 8], ['a', 5, 8]) == False
assert nums_gt(['b', 5, 8], ['a', 6, 8]) == False
assert nums_gt(['b', 5, 9], ['a', 4, 8])
assert nums_gt(['b', 5, 9], ['a', 5, 8]) == False
assert nums_gt(['b', 5, 9], ['a', 6, 8]) == False


assert nums_ge(['a', 5, 7], ['a', 4, 8])
assert nums_ge(['a', 5, 7], ['a', 5, 8])
assert nums_ge(['a', 5, 7], ['a', 6, 8]) == False
assert nums_ge(['a', 5, 8], ['a', 4, 8])
assert nums_ge(['a', 5, 8], ['a', 5, 8])
assert nums_ge(['a', 5, 8], ['a', 6, 8]) == False
assert nums_ge(['a', 5, 9], ['a', 4, 8])
assert nums_ge(['a', 5, 9], ['a', 5, 8]) == False
assert nums_ge(['a', 5, 9], ['a', 6, 8]) == False

assert nums_ge(['a', 5, 7], ['b', 4, 8])
assert nums_ge(['a', 5, 7], ['b', 5, 8])
assert nums_ge(['a', 5, 7], ['b', 6, 8]) == False
assert nums_ge(['a', 5, 8], ['b', 4, 8])
assert nums_ge(['a', 5, 8], ['b', 5, 8])
assert nums_ge(['a', 5, 8], ['b', 6, 8]) == False
assert nums_ge(['a', 5, 9], ['b', 4, 8])
assert nums_ge(['a', 5, 9], ['b', 5, 8]) == False
assert nums_ge(['a', 5, 9], ['b', 6, 8]) == False

assert nums_ge(['b', 5, 7], ['a', 4, 8])
assert nums_ge(['b', 5, 7], ['a', 5, 8])
assert nums_ge(['b', 5, 7], ['a', 6, 8]) == False
assert nums_ge(['b', 5, 8], ['a', 4, 8])
assert nums_ge(['b', 5, 8], ['a', 5, 8]) == False
assert nums_ge(['b', 5, 8], ['a', 6, 8]) == False
assert nums_ge(['b', 5, 9], ['a', 4, 8])
assert nums_ge(['b', 5, 9], ['a', 5, 8]) == False
assert nums_ge(['b', 5, 9], ['a', 6, 8]) == False
