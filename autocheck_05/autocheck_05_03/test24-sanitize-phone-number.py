numbers = [str(x) for x in range(10)]


def sanitize_phone_number(phone: str) -> str:
    new_phone = ''

    for symbol in phone.strip():
        if symbol in numbers:
            new_phone += symbol

    return new_phone


if __name__ == '__main__':
    while True:
        phone = input('Enter phone number: ')

        if phone == 'exit':
            print('Sanitize aborted by user!')
            break

        print(sanitize_phone_number(phone), '\n')
