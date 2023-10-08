lst_m = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]


def flatten(lst):
    new_list = []

    for i in lst:
        if isinstance(i, list):
            new_list.extend(flatten(i))
        else:
            new_list.append(i)

    return new_list


print(flatten(lst_m))
