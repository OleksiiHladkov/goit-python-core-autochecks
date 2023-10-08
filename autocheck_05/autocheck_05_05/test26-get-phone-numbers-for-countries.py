numbers = [str(x) for x in range(10)]
phone_codes = {'JP': '81', 'SG': '65', 'TW': '886', 'UA': '380'}


def sanitize_phone_number(phone: str) -> str:
    new_phone = ''

    for symbol in phone.strip():
        if symbol in numbers:
            new_phone += symbol

    return new_phone


def get_phone_numbers_for_countries(list_phones: list) -> dict:
    phone_dict = {x: [] for x in phone_codes}

    for phone in list_phones:
        new_phone = sanitize_phone_number(phone)

        count = 1
        last_count = len(phone_codes)

        for country, code in phone_codes.items():
            if new_phone[0:1] == code or new_phone[0:2] == code or new_phone[0:3] == code:
                phone_dict[country].append(new_phone)
                break

            if count == last_count:
                phone_dict['UA'].append(new_phone)

            count += 1

    return phone_dict


if __name__ == '__main__':
    list_phones = ['   +65665843111  ', ' +81665843111 ',
                   '+886665843111', '  +380665843111 ', '050 13 23 430', '    22545']
    print(get_phone_numbers_for_countries(list_phones), '\n')
