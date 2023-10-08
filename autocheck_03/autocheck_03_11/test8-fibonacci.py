# lst = []


# def fibonacci(n: int) -> list:
#     global lst

#     lst_len = len(lst)

#     if n == lst_len:
#         return lst
#     else:
#         if lst_len == 0:
#             lst.append(0)
#         elif lst_len == 1:
#             lst.append(1)
#         else:
#             lst.append(lst[lst_len-1] + lst[lst_len-2])

#         try:
#             return fibonacci(n)
#         except RecursionError:
#             return 0


# def fibonacci(n: int, lst: list = []) -> list:
#     lst_len = len(lst)

#     if n < 1:
#         return 0 if lst_len == 0 else lst[lst_len - 1]
#     else:
#         if lst_len == 0:
#             lst.append(0)
#         elif lst_len == 1:
#             lst.append(1)
#         else:
#             lst.append(lst[lst_len - 1] + lst[lst_len - 2])

#         try:
#             return fibonacci(n - 1, lst)
#         except RecursionError:
#             return lst[lst_len]

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))


if __name__ == '__main__':
    while True:
        user_input = input('Enter number of characters fibonacci sequence: ')

        try:
            user_input = int(user_input)
        except ValueError:
            print(f'{user_input} is not number!')
            continue

        n = 0
        while n < user_input:
            print(fibonacci(n))
            n += 1
        break
