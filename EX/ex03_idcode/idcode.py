

def find_id_code(text: str):
    num = 0
    for i in text:
        if i.isdigit():
            num += 1
        elif num > 11:
            return "Too many numbers!"
        elif num < 11:
            return "Not enough numbers!"
    return num


def the_first_control_number_algorithm(text: str)