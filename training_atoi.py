import sys


if __name__ == '__main__':
    argv = sys.argv
    string = argv[1]
    result = 0

    for c in string:
        a = ord(c)
        i = a - ord('0')
        result = result * 10 + i

    print('{0} {1}'.format(result, type(result)))
