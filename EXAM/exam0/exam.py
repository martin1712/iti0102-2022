game = [[1, 2, 1], [2, 1, 2], [2, 1, 0]]


def tic_tac_toe(game: list) -> int:
    zeros = 0
    ones = 0
    twos = 0
    for i in game:
         for j in i:
             if j == 0:
                 zeros += 1
             if j == 1:
                 ones += 1
             elif j == 2:
                 twos += 1

    if ones == twos:
        return 0
    elif ones > twos:
        return 1
    elif twos > ones:
        return 2

result = tic_tac_toe(game)
print(result)