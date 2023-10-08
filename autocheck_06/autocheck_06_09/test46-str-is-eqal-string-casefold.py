def is_equal_string(utf8_string: bytes, utf16_string: bytes) -> bool:
    return utf8_string.decode("utf-8").casefold() == utf16_string.decode("utf-16").casefold()


if __name__ == "__main__":
    utf8_string = "Hello world!".encode("utf-8")
    utf16_string = "Hello world!".encode("utf-16")
    print(is_equal_string(utf8_string, utf16_string))
