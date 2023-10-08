import re


def find_all_words(text: str, word: str) -> list:
    return re.findall(word, text, re.IGNORECASE)


if __name__ == "__main__":
    text = "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0."
    word = "Python"
    print(find_all_words(text, word))
