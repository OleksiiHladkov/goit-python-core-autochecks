import re


def find_all_links(text):
    result = []
    iterator = re.finditer(
        r"(?:http://|https://)(?!\w*\.\.)[\w_\.]+", text)
    for match in iterator:
        result.append(match.group())
    return result


if __name__ == "__main__":
    text = "The main search site in the world is https://www.google.com The main social network for people in the world is https://www.facebook.com But programmers have their own social network http://github.com There they share their code. some url to check https://www..facebook.com www.facebook.com"
    print(find_all_links(text))
