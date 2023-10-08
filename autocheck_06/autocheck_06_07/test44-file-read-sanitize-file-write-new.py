def sanitize_file(source:str, output:str):
    text_new =""
    numbers = [str(n) for n in range(10)]

    with open(source, "r") as file_old:
        while True:
            line = file_old.readline()
            if not line:
                break
            for symbol in line:
                # print(symbol, symbol in numbers)
                if symbol not in numbers:
                    text_new += symbol
    
    with open(output, "w") as file_new:
        file_new.write(text_new)


if __name__ == "__main__":
    source = "test.txt"
    output = "test-new.txt"
    print(sanitize_file(source, output))
