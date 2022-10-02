

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
    last_result = []
    result = car_list
    cars = car_make_and_models(all_cars)
    for car in cars:
        if car[0] not in car_list[0]:
            car_list.append([car[0], car[1]])
        if cars[0][1][0] not in car_list[0][1]:
                car_list[0][1].append(cars[0][1][0])
                last_result.append(result)
    return last_result


print(add_cars([['Audi', ['A4']], ['Skoda', ['Superb']]], "Audi A6,BMW A B C,Audi A4"))
# [['Audi', ['A4', 'A6']], ['Skoda', ['Superb']], ['BMW', ['A B C']]] - result
# [['Audi', ['A6', 'A4']], ['BMW', ['A B C']]] - cars
# [['Audi', ['A4']], ['Skoda', ['Superb']]] - car_list