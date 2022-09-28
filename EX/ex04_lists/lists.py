

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



print(search_by_model("Audi A4 s6 2021,Audi a4 2021,Audi A40 s6 20220", "audi"))
