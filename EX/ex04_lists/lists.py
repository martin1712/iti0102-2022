

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
    result = car_list
    cars = car_make_and_models(all_cars)
    all_makes = []
    a = all_cars.split(",")
    for car in a:
        tokens = car.split(" ", 1)
        for car in car_list:
            if car[0] == tokens[0]:
                if tokens[1] not in car[1]:
                    car[1].append(tokens[1])
    for car in car_list:
        all_makes.append(car[0])
    for car in cars:
        if car[0] not in all_makes:
            car_list.append([car[0], car[1]])
    return car_list


def number_of_cars(all_cars: str) -> list:
    numbers = []
    makes = car_makes(all_cars)
    for car in makes:
        all_cars.count(car)
        numbers.append(all_cars.count(car))
    tuple_result = [(makes[i], numbers[i]) for i in range(0, len(makes))]
    return tuple_result


def car_list_as_string(cars: list) -> str:
    result = ""
    for i in cars:
        if len(i[1]) > 1:
            a = ', '.join(i[1])
            b = a.replace(",", f",{i[0]}")
            result += f"{i[0]}" + " " + f"{b}"
            result += ','
        else:
            result += f"{i[0]}" + " " + f"{' '.join(i[1])}"
    new_result = result.rstrip(',')
    return new_result



print(car_list_as_string([['Audi', ['A4', 'A9']], ['Skoda', ['Superb']]]))
#  "Audi A4,Skoda Superb"


