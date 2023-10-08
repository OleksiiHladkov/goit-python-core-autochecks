from random import randint


def get_random_password():
    password = ''

    i = 8
    while i > 0:
        random_num = randint(40, 126)
        password += chr(random_num)
        i -= 1

    return password


if __name__ == '__main__':
    print(get_random_password())
