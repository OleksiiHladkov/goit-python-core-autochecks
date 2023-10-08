import sys


def parse_args():
    result = ""

    count = 1
    for arg in sys.argv:
        if count > 1:
            result += arg if count == 2 else ' ' + arg

        count += 1

    return result


if __name__ == '__main__':
    print(parse_args())
