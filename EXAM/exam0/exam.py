
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
        if 0 not in i:
            if sum(i) / 3 == 1:
                return 1
            if sum(i) / 3 == 2:
                return 2
    if game[0][0] and game[1][1] and game[2][2] != 0 and game[0][0] + game[1][1] + game[2][2] == 3:
        return 1
    if game[0][0] and game[1][1] and game[2][2] != 0 and game[0][0] + game[1][1] + game[2][2] == 6:
        return 2
    if game[0][0] and game[1][0] and game[2][0] != 0 and game[0][0] + game[1][0] + game[2][0] == 3:
        return 1
    if game[0][0] and game[1][0] and game[2][0] != 0 and game[0][0] + game[1][0] + game[2][0] == 6:
        return 2
    if game[0][1] and game[1][1] and game[2][1] != 0 and game[0][0] + game[1][1] + game[2][1] == 3:
        return 1
    if game[0][1] and game[1][1] and game[2][1] != 0 and game[0][0] + game[1][1] + game[2][1] == 6:
        return 2
    if game[0][2] and game[1][2] and game[2][2] != 0 and game[0][2] + game[1][2] + game[2][2] == 3:
        return 1
    if game[0][2] and game[1][2] and game[2][2] != 0 and game[0][2] + game[1][2] + game[2][2] == 6:
        return 2
    return 0


if __name__ == '__main__':
    print(tic_tac_toe([[1, 1, 1],
                       [2, 2, 2],
                       [2, 2, 0]]))
