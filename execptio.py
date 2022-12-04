import sys

try:
    x = int(input('a: '))
    y = int(input('b: '))

except ValueError:
    print('This is a value error')
    sys.exit(1)

try:

    result = x / y 

except ZeroDivisionError:

    print('Error cannot divide by 0.')

    sys.exit(1)

print(result)