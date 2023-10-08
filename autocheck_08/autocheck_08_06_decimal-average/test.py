from decimal import Decimal, getcontext


def decimal_average(number_list:list, signs_count:int) -> float:

    getcontext().prec = signs_count
    sum = 0
    for i in number_list:
        sum += Decimal(i)

    return float(sum) / len(number_list)





if __name__ == "__main__":
    number_list = [3, 5, 77, 23, 0.57]
    print(decimal_average(number_list, 6))