def save_applicant_data(source: list[dict], output: str):
    result = []
    
    for item in source:
        line = []
        for value in item.values():
            line.append(str(value))
        
        result.append(",".join(line) + "\n")

    with open(output, "w") as fh:
        fh.writelines(result)


if __name__ == "__main__":
    source = [
                {
                    "name": "Kovalchuk Oleksiy",
                    "specialty": 301,
                    "math": 175,
                    "lang": 180,
                    "eng": 155,
                },
                {
                    "name": "Ivanchuk Boryslav",
                    "specialty": 101,
                    "math": 135,
                    "lang": 150,
                    "eng": 165,
                },
                {
                    "name": "Karpenko Dmitro",
                    "specialty": 201,
                    "math": 155,
                    "lang": 175,
                    "eng": 185,
                },
            ]
    output = "test.txt"
    print(save_applicant_data(source, output))
