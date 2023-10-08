import string

ALPH_LOW = string.ascii_lowercase
ALPH_UPP = string.ascii_uppercase
NUMBERS = [str(x) for x in range(0, 10)]


def is_valid_password(password):
    is_enought_symbols = True
    is_capital_litters = True
    is_small_litters = True
    is_numbers = True

    if len(password) < 8:
        is_enought_symbols = False
    if len(set(password) & set(ALPH_UPP)) < 1:
        is_capital_litters = False
    if len(set(password) & set(ALPH_LOW)) < 1:
        is_small_litters = False
    if len(set(password) & set(NUMBERS)) < 1:
        is_numbers = False

    return is_enought_symbols and is_capital_litters and is_small_litters and is_numbers


if __name__ == '__main__':
    password = 'Ptnh8956'
    print(is_valid_password(password))
