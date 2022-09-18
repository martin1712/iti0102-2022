

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


if __name__ == '__main__':
    print("\nFind ID code:")
    print(find_id_code(""))  # -> "Not enough numbers!"
    print(find_id_code("123456789123456789"))  # -> "Too many numbers!"
    print(find_id_code("ID code is: 49403136526"))  # -> "49403136526"
    print(find_id_code("efs4  9   #4aw0h 3r 1a36g5j2!!6-"))  # -> "49403136526"


def the_first_control_number_algorithm(text: str) -> str:
    result = ""
    first_num = result[0]
    second_num = result[1]
    third_num = result[2]
    fourth_num = result[3]
    fifth_num = result[4]
    sixth_num = result[5]
    seventh_num = result[6]
    eight_num = result[7]
    ninth_num = result[8]
    tenth_num = result[9]
    for i in text:
        if i.isdigit():
            result = result + i
            if result != 11:
                return "Incorrect ID code"
            else:
                sum = first_num * 1 + second_num * 2 + third_num * 3 + fourth_num * 4 + fifth_num * 5 + sixth_num * 6 + seventh_num * 7 + eight_num * 8 +  ninth_num * 9 + tenth_num * 1
                if sum % 11 > 10:
                    return "Needs the second algorithm!"
                return "result"
