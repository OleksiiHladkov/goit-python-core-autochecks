def read_employees_from_file(path: str) -> list:
    result = []
    fh = open(path, "r")

    while True:
        line = fh.readline()
        if not line:
            break
        result.append(line.replace("\n", ""))

    fh.close()
    return result


if __name__ == "__main__":
    path = "40-file-read-employee.txt"
    print(read_employees_from_file(path))
