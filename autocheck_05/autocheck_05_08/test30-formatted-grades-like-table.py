grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}


def formatted_grades(students: dict) -> list:
    result = []

    count = 1
    for student, str_grade in students.items():
        str_item = "{:>4}|{:<10}|{:^5}|{:^5}".format(
            count, student, str_grade, grades[str_grade])
        result.append(str_item)
        count += 1

    return result


if __name__ == '__main__':
    students = {"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"}
    for i in formatted_grades(students):
        print(i)
