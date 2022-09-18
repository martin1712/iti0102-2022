

def find_id_code(text: str) -> str:
    result = ""
    for i in text:
        if i.isdigit():
            result += i
    a = len(result)
    if a < 11:
        return "Not enough numbers!"
    if a > 11:
        return "Too many numbers!"
    else:
        return result


def the_first_control_number_algorithm(text: str) -> str:
    result = ""
    for i in text:
        if i.isdigit():
            result += i
    a = len(result)
    if a != 11:
        return "Incorrect ID code"
    b = int(result[0]) * 1 + int(result[1]) * 2 + int(result[2]) * 3 + int(result[3]) * 4 + int(result[4]) * 5 + int(result[5]) * 6 + int(result[6]) * 7 + int(result[7]) * 8 + int(result[8]) * 9 + int(result[9]) * 1
    if b % 11 >= 10:
        return "Needs the second algorithm!"
    if b % 11 == int(result[10]):
        return result
