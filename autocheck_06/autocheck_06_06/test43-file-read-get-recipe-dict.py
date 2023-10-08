def get_recipe(path: str, search_id: str) -> dict|None:
    result = None

    with open(path, "r") as fh:
        while True:
            line = fh.readline()

            if not line:
                break

            if line[:24] == search_id:
                recipe_lst = line.replace("\n", "").split(",")
                result = dict()
                result["id"] = recipe_lst[0]
                result["name"] = recipe_lst[1]
                result["ingredients"] = recipe_lst[2:]

    return result


if __name__ == "__main__":
    path = "test.txt"
    search_id = "60b90c3b13067a15887e1ae4"
    print(get_recipe(path, search_id))
