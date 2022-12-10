
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


def tic_tac_toe(i: list) -> int:
    if i[0][0] == i[0][1] == i[0][2]:
        return i[0][0]
    elif i[0][0] == i[1][1] == i[2][2]:
        return i[0][0]
    elif i[0][0] == i[1][0] == i[2][0]:
        return i[0][0]
    elif i[1][0] == i[1][1] == i[1][2]:
        return i[1][0]
    elif i[2][0] == i[2][1] == i[2][2]:
        return i[2][0]
    elif i[0][2] == i[1][1] == i[2][0]:
        return i[0][2]
    elif i[0][1] == i[1][1] == i[2][1]:
        return i[0][1]
    elif i[0][2] == i[1][2] == i[2][2]:
        return i[0][2]
    else:
        return 0


if __name__ == '__main__':
    print(tic_tac_toe([[1, 2, 1], [2, 1, 2], [2, 2, 1]]))
