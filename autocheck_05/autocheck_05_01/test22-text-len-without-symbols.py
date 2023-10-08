NON_WRITE_SYMBOLS = ['\n', '\f', '\r', '\t', '\v']


def real_len(text: str) -> int:
    real_text = ''

    for symbol in text:
        if symbol in NON_WRITE_SYMBOLS:
            continue
        real_text += symbol

    return len(real_text)


if __name__ == '__main__':
    text = 'Alex\nKdfe23\t\f\v.\r'
    print(len(text))
    print(real_len(text))
