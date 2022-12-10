
capital_letter = ""
for i in range(65, 91):
    capital_letter += chr(i)


small_letters = ""
for i in range(97, 123):
    small_letters += chr(i)


def find_capital_letters(input_string):
    output_string = ""
    for letter in input_string:
        if letter in capital_letter:
            output_string += letter
    return output_string


game = [[1, 2, 1], [2, 1, 2], [2, 1, 0]]


def tic_tac_toe(game: list) -> int:
    """
    Find game winner.

    #4

    The 3x3 table is represented as a list of 3 rows, each row has 3 element (ints).
    The value can be 1 (player 1), 2 (player 2) or 0 (empty).
    The winner is the player who gets 3 of her pieces in a row, column or diagonal.

    There is only one winner or draw. You don't have to validate whether the game is in correct (possible) state.
    I.e the game could have four 1s and one 0 etc.

    tic_tac_toe([[1, 2, 1], [2, 1, 2], [2, 2, 1]]) => 1
    tic_tac_toe([[1, 0, 1], [2, 1, 2], [2, 2, 0]]) => 0
    tic_tac_toe([[2, 2, 2], [0, 2, 0], [0, 1, 0]]) => 2

    :param game
    :return: winning player id
    """
    for i in game:
        if 0 not in i and i[0] == i[1] == i[2]:
            return i[0]

    if game[0][0] == game[1][1] == game[2][2] != 0:
        return game[0][0]
    elif game[0][0] == game[1][0] == game[2][0] != 0:
        return game[0][0]
    elif game[2][0] == game[1][1] == game[0][2] != 0:
        return game[2][0]
    elif game[0][2] == game[1][2] == game[2][2] != 0:
        return game[0][2]
    elif game[0][1] == game[1][1] == game[2][1]:
        return game[0][1]
    else:
        return 0


def close_far(a: int, b: int, c: int) -> bool:
    """
    Return if one value is "close" and other is "far".

    #2

    Given three ints, a b c, return true if one of b or c is "close" (differing from a by at most 1),
    while the other is "far", differing from both other values by 2 or more.

    close_far(1, 2, 10) => True
    close_far(1, 2, 3) => False
    close_far(4, 1, 3) => True
    """
    if b - a or a - b >= 2:
        if c - a or a - c in [-1, 0, 1]:
            if b - c >= 2:
                return True
    if b - a or a - b in [-1, 0, 1]:
        if c - a or a - c >= 2:
            if c - b >= 2:
                return True
    return False



if __name__ == '__main__':
    print(close_far(1, 2, 10))
