def is_check_name(fullname: str, first_name: str) -> bool:
    return False if fullname.removeprefix(first_name) == fullname else True


if __name__ == '__main__':
    while True:
        fullname = input('Enter fullname: ')

        if fullname == 'exit':
            print('Sanitize aborted by user!')
            break

        first_name = input('Enter first name: ')

        print(is_check_name(fullname, first_name), '\n')
