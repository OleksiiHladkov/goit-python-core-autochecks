def is_spam_words(text: str, spam_words: list, space_around: bool = False) -> bool:
    text_lower = text.lower()

    for word in spam_words:
        word_lower = word.lower()

        if space_around:
            if text_lower.find(' ' + word_lower + '.') != -1 or text_lower.find(word_lower + ' ') == 0 or text_lower.find(' ' + word_lower + ' ') != -1:
                return True
            else:
                return False
        else:
            if text_lower.find(word_lower) != -1:
                return True
            else:
                return False


if __name__ == '__main__':
    text = 'Fuck you!'
    spam_words = ['fuck', 'shit']
    space_around = False
    # space_around = True
    print(is_spam_words(text, spam_words, space_around))
