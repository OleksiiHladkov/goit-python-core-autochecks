ECTS_GRADE = {'F': 1,
              'FX': 2,
              'E': 3,
              'D': 3,
              'C': 4,
              'B': 5,
              'A': 5}

ECTS_DESCR = {'F': 'Unsatisfactorily',
              'FX': 'Unsatisfactorily',
              'E': 'Enough',
              'D': 'Satisfactorily',
              'C': 'Good',
              'B': 'Very good',
              'A': 'Perfectly'}


def get_grade(key):
    return ECTS_GRADE.get(key)


def get_description(key):
    return ECTS_DESCR.get(key)


if __name__ == '__main__':
    user_input = input('Enter ECTS grade: ')
    print(get_grade(user_input))
    print(get_description(user_input))
