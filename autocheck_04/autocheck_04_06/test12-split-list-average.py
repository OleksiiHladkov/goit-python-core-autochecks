def split_list(grade: list) -> tuple:
    count = len(grade)
    lst_less_average = []
    lst_more_average = []

    if count == 0:
        return lst_less_average, lst_more_average

    sum = 0

    for item in grade:
        sum += item

    average = round(sum / count)

    for item in grade:
        if item <= average:
            lst_less_average.append(item)
        else:
            lst_more_average.append(item)

    return lst_less_average, lst_more_average


if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5]
    print(split_list(lst))
