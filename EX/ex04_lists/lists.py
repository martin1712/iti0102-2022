

"""Great."""


def list_of_cars(all_cars: str) -> list:
    """Great."""
    if all_cars == "":
        return []
    return all_cars.split(",")


def car_makes(all_cars: str) -> list:
    """Great."""
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
    """Great."""
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
    """Great."""
    all_makes = []
    a = all_cars.split(",")
    for car in a:
        tokens = car.split(" ")
        tokens_string = ", ".join(tokens[:1])
        tokens_string_lower = tokens_string.lower()
        make_lower = make.lower()
        if make_lower in tokens_string_lower:
            all_makes.append(" ".join(tokens[:]))
        if all_cars == "":
            return []
        if make == "":
            return []
    return all_makes


def search_by_model(all_cars: str, model: str) -> list:
    """Great."""
    all_makes = []
    a = all_cars.split(",")
    for car in a:
        tokens = car.split(" ")
        if 1 < len(tokens):
            string_list = [x.lower() for x in tokens]
            model_lower = model.lower()
            if model_lower in string_list[1:]:
                all_makes.append(" ".join(tokens[:]))
        if " " in model:
            return []
        if all_cars == "":
            return []
        if model == "":
            return []
    return all_makes


def car_make_and_models(all_cars: str) -> list:
    """Great."""
    car_make = []
    cars_list = []
    a = all_cars.split(",")
    for car in a:
        tokens = car.split(" ", 1)
        print(tokens)
        if 1 < len(tokens):
            if tokens[0] not in car_make:
                car_make.append(tokens[0])
                cars_list.append([tokens[0], tokens[1:]])
        for car in cars_list:
            if car[0] == tokens[0]:
                if tokens[1] not in car[1]:
                    car[1].append(tokens[1])
        if all_cars == "":
            return []
    return cars_list


def add_cars(car_list: list, all_cars: str) -> list:
    result = car_list
    cars = car_make_and_models(all_cars)
    if cars[0] not in car_list:
        result.append([cars[0], cars[1:]])
    return result


print(car_make_and_models("Audi A4 2007,Skoda Super,Skoda Octavia,BMW 530,Seat Leon,Skoda Superb,Skoda Superb,BMW x5"))
# [['Audi', ['A4']], ['Skoda', ['Super', 'Octavia', 'Superb']], ['BMW', ['530', 'x5']], ['Seat', ['Leon']]]
print(car_make_and_models("Mazda 6,Mazda 6,Mazda 6,Mazda 6")) # [['Mazda', ['6']]]
print(car_make_and_models(""))