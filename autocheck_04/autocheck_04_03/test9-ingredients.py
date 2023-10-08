def format_ingredients(items: list) -> str:
    items_str = ''
    items_last_id = len(items) - 1
    item_id = 0

    while item_id <= items_last_id:

        if item_id == 0:
            symbol = ''
        elif item_id == items_last_id:
            symbol = ' and '
        else:
            symbol = ', '

        items_str += f'{symbol}{items[item_id]}'

        item_id += 1

    return items_str


items = ["2 eggs", "1 liter sugar", "1 tsp salt", "vinegar"]
print(format_ingredients(items))
