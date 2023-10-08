def get_credentials_users(path:str) -> list:
    result = []
    
    with open(path, "rb") as fh:
        while True:
            line = fh.readline()

            if not line:
                break

            result.append(line.decode().replace("\n", ""))
    
    return result

    # text = ""

    # with open(path, "rb") as fh:
    #     text = fh.read().decode().split("\n")

    # return text





if __name__ == "__main__":
    path = "test.bin"
    print(get_credentials_users(path))