articles_dict = [
    {
        "title": "Endless ocean waters.",
        "author": "Jhon Stark",
        "year": 2019,
    },
    {
        "title": "Oceans of other planets are full of silver",
        "author": "Artur Clark",
        "year": 2020,
    },
    {
        "title": "An ocean that cannot be crossed.",
        "author": "Silver Name",
        "year": 2021,
    },
    {
        "title": "The ocean that you love.",
        "author": "Golden Gun",
        "year": 2021,
    },
]


def find_articles(key: str, letter_case: bool = False) -> list:
    list_articles = []

    for item in articles_dict:
        for k, v in item.items():
            if k == 'title' or k == 'author':
                search_v = v if letter_case else v.upper()
                search_key = key if letter_case else key.upper()

                if search_v.find(search_key) >= 0:
                    list_articles.append(item)
                    break

    return list_articles


if __name__ == '__main__':
    while True:
        key = input('Enter reqvest (enter "exit" to abort): ')

        if key == 'exit':
            print('Search aborted by user!')
            break

        user_input = input('Use letter case ("y" - yes, "n" - no): ')
        letter_case = True if user_input == 'y' else False

        print(find_articles(key, letter_case), '\n')
