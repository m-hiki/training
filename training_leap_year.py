
import sys


MESSAGE = ['is not a leap year', 'is a leap year']


if __name__ == '__main__':
    argv = sys.argv
    year = int(argv[1])

    if year % 400 == 0:
        is_leap_year = True
    elif year % 100 == 0:
        is_leap_year = False
    elif year % 4 == 0:
        is_leap_year = True
    else:
        is_leap_year = False

    print('{0} {1}'.format(year, MESSAGE[is_leap_year]))
