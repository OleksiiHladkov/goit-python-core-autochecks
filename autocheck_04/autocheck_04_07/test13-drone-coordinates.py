points = {
    (0, 1): 2,
    (0, 2): 3.8,
    (0, 3): 2.7,
    (1, 2): 2.5,
    (1, 3): 4.1,
    (2, 3): 3.9,
}


def calculate_distance(coordinates: list[int]) -> float:
    count = len(coordinates)
    distance = 0

    if count == 0 or count == 1:
        return distance

    x, y = 0, 1

    while True:
        if y > count - 1:
            return distance
        else:
            couple_coordinates = coordinates[x:y+1]
            couple_coordinates.sort()
            distance += points.get(tuple(couple_coordinates))
            x, y = x + 1, y + 1


if __name__ == '__main__':
    lst = [0, 1, 3, 2, 0]
    print(calculate_distance(lst))
