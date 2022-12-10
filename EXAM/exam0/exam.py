
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


if __name__ == '__main__':
    print(tic_tac_toe([[1, 2, 1], [2, 1, 2], [2, 2, 1]]))
    print(find_capital_letters())