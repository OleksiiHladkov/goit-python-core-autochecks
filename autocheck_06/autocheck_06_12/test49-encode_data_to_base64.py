import base64


def encode_data_to_base64(data:list[str]) -> list[str]:
    result = []
    for user in data:
        user_byte = user.encode("utf-8")
        user_b64 = base64.b64encode(user_byte)
        result.append(user_b64.decode("utf-8"))

    return result




if __name__ == "__main__":
    data = ['andry:uyro18890D', 'steve:oppjM13LL9e']
    print(encode_data_to_base64(data))