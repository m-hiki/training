
import sys


if __name__ == '__main__':
    argv = sys.argv
    year = int(argv[1])
    print('Year : {0}'.format(year))
    #print(int(year) / 4)
    is_leap_year = False

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                is_leap_year = True
        else:
            is_leap_year = True

    message = ['is not a leap year', 'is a leap year']
    print('{0} {1}'.format(year, message[is_leap_year]))
