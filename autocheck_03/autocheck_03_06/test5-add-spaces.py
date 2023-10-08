def format_string(string: str, length: int) -> str:
    if length <= len(string):
        return string
    else:
        spaces = " " * ((length - len(string)) // 2)
        return f'{spaces}{string}'


print(format_string(length=15, string='abaa'))
