def total_salary(path: str) -> float:
    result = float(0)

    try:
        fh = open(path, "r")
    except:
        print("Can't open file!")
        return result

    count = 1

    try:
        while True:
            line = fh.readline()
            if not line:
                break
            result += float(line.split(",")[1].strip())
            count += 1
    except:
        print(f"Can't parsing a line number: {count}")
        fh.close()
        return 0

    return result


if __name__ == "__main__":
    path = "test38-file-total-salary.txt"
    total_salar = total_salary(path)
    print(f"Total salary is: {total_salar}")
