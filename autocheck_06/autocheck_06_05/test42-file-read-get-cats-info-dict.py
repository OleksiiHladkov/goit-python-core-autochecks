def get_cats_info(path: str) -> list:
    result = []
    keys = ("id", "name", "age")

    with open(path, "r") as fh:
        data_list = fh.readlines()
        for data in data_list:
            values = tuple(data.replace("\n", "").split(","))
            if len(keys) == len(values):
                result.append({keys[i]: values[i]
                              for i, _ in enumerate(values)})

    return result


if __name__ == "__main__":
    path = "test.txt"
    print(get_cats_info(path))
