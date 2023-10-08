import re


def find_word(text: str, word: str) -> dict:
    match = re.search(word, text)

    result = match != None
    first_index = match.span()[0] if result else None
    last_index = match.span()[1] if result else None

    return {"result": result, "first_index": first_index, "last_index": last_index, "search_string": word, "string": text}


if __name__ == "__main__":
    text = "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0."
    word = "python"
    print(find_word(text, word))
