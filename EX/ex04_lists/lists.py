

"""Great."""


def list_of_cars(all_cars: str) -> list:
    if all_cars == "":
        return []
    return all_cars.split(",")


def car_makes(all_cars: str) -> list:
    all_makes = []
    a = all_cars.split(",")
    for car in a:
        tokens = car.split(" ")
        if tokens[0] not in all_makes:
            all_makes.append(tokens[0])
        if all_cars == "":
            return []
    return all_makes


def car_models(all_cars: str) -> list:
    all_makes = []
    a = all_cars.split(",")
    for car in a:
        tokens = car.split(" ", 1)
        if 1 < len(tokens):
            if tokens[1] not in all_makes:
                all_makes.append(tokens[1])
        if all_cars == "":
            return []
    return all_makes


def search_by_make(all_cars: str, make: str) -> list:
    all_makes = []
    a = all_cars.split(",")
    for car in a:
        tokens = car.split(" ")
        make_lower = make.lower()
        tokens_string = ", ".join(tokens)
        tokens_string_lower = tokens_string.lower()
        if make_lower in tokens_string_lower:
            all_makes.append(" ".join(tokens[:]))
        if all_cars == "":
            return []
    return all_makes


def search_by_model(all_cars: str) -> list:
    all_makes = []
    a = all_cars.split(",")
    for car in a:
        tokens = car.split(" ")
        if tokens[1] in all_cars and 1 < len(tokens):
            all_makes.append(tokens[1])
        if all_cars == "":
            return []
    return a



print(list_of_cars("Audi A4,Skoda Superb,Audi A4"))  # ["Audi A4", "Skoda Superb", "Audi A4"]

print(car_makes("Audi A4,Skoda Super,Skoda Octavia,BMW 530,Seat Leon,Skoda Superb,Skoda Superb,BMW x5"))  # ['Audi', 'Skoda', 'BMW', 'Seat']

print(car_makes("Mazda 6,Mazda 6,Mazda 6,Mazda 6"))  # ['Mazda']

print(car_makes(""))  # []

print(car_models("Audi A4 SUPER,Skoda Superb,Audi A4,Audi A6"))  # ["A4", "Superb", "A6"]

print(search_by_make("Audi A4,audi A5,AUDI a6 A7,Skoda Superb", "Audi"))

print(search_by_model("Audi A4,Audi a4 2021,Audi A40"))
