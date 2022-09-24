

"""Great."""


def list_of_cars(all_cars: str) -> list:
    return all_cars.split(",")


print(list_of_cars("Audi A4,Skoda Superb,Audi A4"))


def car_makes(all_cars: str) -> list:
    all_makes = []
    a = all_cars.split(",")
    for car in a:
        tokens = car.split(" ")
        if tokens[0] not in all_makes:
            all_makes.append(tokens[0])
    return all_makes


def car_models(all_cars: str) -> list:
    all_makes = []
    a = all_cars.split(",")
    for car in a:
        tokens = car.split(" ")
        if tokens[1] not in all_makes:
            all_makes.append(tokens[1])
    return all_makes


print(car_makes("Audi A4,Skoda Super,Skoda Octavia,BMW 530,Seat Leon,Skoda Superb,Skoda Superb,BMW x5"))
print(car_makes("")) # []
print(car_models("Audi A4,Skoda Superb,Audi A4,Audi A6"))  # ["A4", "Superb", "A6"]