
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

    if game[0][0] != 0:

        if game[0][0] == game[0][1] == game[0][2]:
            return game[0][0]

        elif game[0][0] == game[1][1] == game[2][2]:
            return game[0][0]

        elif game[0][0] == game[1][0] == game[2][0]:
            return game[0][0]
        else:
            return 0

    elif game[1][0] != 0:

        if game[1][0] == game[1][1] == game[1][2]:
            return game[1][0]
        else:
            return 0

    elif game[2][0] != 0:

        if game[2][0] == game[2][1] == game[2][2]:
            return game[2][0]
        return 0

    elif game[0][2] != 0:

        if game[0][2] == game[1][1] == game[2][0]:
            return game[0][2]
        return 0

    elif game[0][1] != 0:

        if game[0][1] == game[1][1] == game[2][1]:
            return game[0][1]
        return 0

    elif game[0][2] != 0:

        if game[0][2] == game[1][2] == game[2][2]:
            return game[0][2]
        return 0

    else:
        return 0


if __name__ == '__main__':
    print(tic_tac_toe([[0, 0, 0], [1, 1, 1], [0, 0, 0]]))
