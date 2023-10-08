import re


def replace_spam_words(text: str, spam_words: list) -> str:
    new_text = text

    for word in spam_words:
        new_text = re.sub(word, "*" * len(word), new_text, 0, re.IGNORECASE)

    return new_text

    # try to find out of repl "*" in count of litters
    # str_spam_words = "(" + "|".join(spam_words) + ")"
    # return re.sub(str_spam_words, "****", text, 0, re.IGNORECASE)


if __name__ == "__main__":
    text = "Fuck you! Suck all!"
    spam_words = ["fuck", "suck"]
    print(replace_spam_words(text, spam_words))
