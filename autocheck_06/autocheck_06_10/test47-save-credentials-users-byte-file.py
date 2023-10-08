def save_credentials_users(path: str, users_info: dict):
    # не приймала автоперевірка
    # row = ""
    # for key, value in users_info.items():
    #     row += f"{key}:{value}\n"

    # with open(path, "wb") as fh:
    #     fh.write(row.encode("utf-8"))

    # автоперевірка прийняла
    auth_lst = []

    for key, value in users_info.items():
        auth_lst.append(f"{key}:{value}\n".encode())

    with open(path, "wb") as fh:
        fh.writelines(auth_lst)




if __name__ == "__main__":
    path = "test.bin"
    users_info = {'andry':'uyro18890D', 'steve':'oppjM13LL9e'}
    save_credentials_users(path, users_info)