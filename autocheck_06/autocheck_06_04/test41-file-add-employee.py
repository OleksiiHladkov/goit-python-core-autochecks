def add_employee_to_file(record: str, path: str):
    fh = open(path, "a")

    fh.write(record+"\n")

    fh.close()


if __name__ == "__main__":
    path = "test.txt"
    record = "Drake Mikelsson,19"
    print(add_employee_to_file(record, path))
