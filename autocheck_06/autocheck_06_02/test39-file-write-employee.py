def write_employees_to_file(employee_list: list, path: str):
    fh = open(path, "w")
    text = ""

    for dep in employee_list:
        text += "\n".join(dep) + "\n"

    fh.write(text)
    fh.close()


if __name__ == "__main__":
    path = "test39-file-write-employee.txt"
    employee_list = [['Robert Stivenson,28',
                      'Alex Denver,30'], ['Drake Mikelsson,19']]
    print(write_employees_to_file(employee_list, path))
