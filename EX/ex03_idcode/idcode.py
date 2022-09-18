

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
    b = int(result[0] * 1 + result[1] * 2 + result[2] * 3 + result[3] * 4 + result[4] * 5 + result[5] * 6 + result[6] * 7 + result[7] * 8 + result[8] * 9 + result[9] * 1)
    c = b % 11
    if c >= 10:
        return "Needs the second algorithm!"
    if c < 10 and c != result[10]:
        return "Incorrect ID code!"
    if c < 10 and c == result[10]:
        return result
