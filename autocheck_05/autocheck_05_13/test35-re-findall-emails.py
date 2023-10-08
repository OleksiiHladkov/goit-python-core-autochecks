import re


def find_all_emails(text: str) -> list:
    result = re.findall(
        r"([a-zA-Z]{1}[a-zA-Z0-9_.]{1,}@[a-zA-Z]+\.[a-zA-Z]{2,})", text)

    return result


if __name__ == "__main__":
    text = "My email is a.gladko_ff17@gmail.com or e_gladkova@g.ua"
    print(find_all_emails(text))
