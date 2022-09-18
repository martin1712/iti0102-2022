

def find_id_code(text: str) -> str:
    result = ""
    for i in text:
        if i.isdigit():
            result = result + i
            if result < 11:
                return "Not enough numbers!"
        else:
            if result > 11:
                return "Too many numbers!"
    return "result"


if __name__ == '__main__':
    print(find_id_code("12334etrhrty54645"))



