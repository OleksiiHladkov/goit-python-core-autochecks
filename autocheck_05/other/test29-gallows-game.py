import random

words = ['banana', 'borsch', 'milk', 'apple', 'pine', 'salo', 'sushi']

gallows = [['-', '-', '-', '-', '-', '-'],
           [' ', '|', ' ', ' ', '|', ' '],
           [' ', '|', ' ', ' ', ' ', ' '],
           [' ', '|', ' ', ' ', ' ', ' '],
           [' ', '|', ' ', ' ', ' ', ' '],
           ['/', ' ', '\\', ' ', ' ', ' ']]


def drow_gallows(step=None):
    if step:
        if step >= 1:
            gallows[2][4] = 'O'
        if step >= 2:
            gallows[3][3] = '/'
        if step >= 3:
            gallows[3][4] = '|'
        if step >= 4:
            gallows[3][5] = '\\'
        if step >= 5:
            gallows[4][3] = '/'
        if step >= 6:
            gallows[4][5] = '\\'

    result = ''
    for i in gallows:
        result += ''.join(i) + '\n'

    return result


def find_all_index(text, substring):
    result = []

    start_position = 0

    for i in range(len(text)):
        position = text.find(substring, start_position)
        if position >= 0:
            result.append(position)
            start_position = position + 1

    return result


def main():

    step = 0

    print(drow_gallows(step))

    word = random.choice(words)
    answer_word = ['_' for _ in range(len(word))]

    print((len(word) * ' _ ').strip())

    while True:
        user_input = input('Give your letter >>> ')
        if len(user_input) > 1:
            print('Give one letter!')
            continue

        if user_input == '':
            break

        if user_input not in word:
            step += 1
            print(drow_gallows(step))
        else:
            print(drow_gallows(step))
            indexes_letter = find_all_index(word, user_input)
            for i in indexes_letter:
                answer_word[i] = user_input

        print(' '.join(answer_word))

        if word == ' '.join(answer_word):
            print('You win!')
            break
        if step >= 6:
            print('You loose!')
            break


if __name__ == '__main__':
    main()
