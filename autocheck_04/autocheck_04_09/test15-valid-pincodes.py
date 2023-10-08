def is_valid_pin_codes(pin_codes: list) -> bool:
    if len(pin_codes) == 0:
        return False

    available_numbers = [str(x) for x in range(0, 10)]

    is_dublicates = True
    is_string = True
    is_four_symbols = True
    is_numbers = True

    pin_id = 1
    for pin in pin_codes:
        # dublicates
        if pin in pin_codes[pin_id:]:
            is_dublicates = False
            break
        # string
        if not isinstance(pin, str):
            is_string = False
            break
        # four symbols
        if len(pin) != 4:
            is_four_symbols = False
            break
        # numbers
        if len(set(pin) - set(available_numbers)) != 0:
            is_numbers = False
            break

        pin_id += 1

    return is_dublicates and is_string and is_four_symbols and is_numbers


if __name__ == '__main__':
    pin_codes = ['1101', '9034', '0011']
    # pin_codes = ['1101', '9034', '1101']
    print(is_valid_pin_codes(pin_codes))
