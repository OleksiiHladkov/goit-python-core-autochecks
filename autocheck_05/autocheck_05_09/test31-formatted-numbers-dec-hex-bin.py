def formatted_numbers():
    result = []

    result.append("|{:^10}|{:^10}|{:^10}|".format("decimal", "hex", "binary"))
    for num in range(16):
        result.append("|{:<10d}|{:^10x}|{:>10b}|".format(num, num, num))

    return result


if __name__ == "__main__":
    for i in formatted_numbers():
        print(i)
