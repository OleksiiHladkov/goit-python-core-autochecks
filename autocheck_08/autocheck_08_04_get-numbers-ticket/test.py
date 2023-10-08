from random import randrange


def get_numbers_ticket(min:int, max:int, quantity:int) -> list:
    result = list()
    
    if min < 1 or max > 1000 or not (min < quantity < max):
        return result

    while len(result) < quantity:
        new_int = randrange(min, max+1)

        if new_int not in result:
            result.append(new_int)

    result.sort()

    return result





if __name__ == "__main__":
    min = 1
    max = 1000
    quantity = 40
    print(get_numbers_ticket(min, max, quantity))