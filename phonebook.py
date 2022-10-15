file = open('data.txt', 'r')

contacts = {

    'Brian': ['phone = +2547298179', 'County = Busia, age = 23'],
    'Dad': '+254723098554'
}

file1 = open('data.txt', 'a')
# file1.write()

name = input('Enter the name: ')

if name in contacts:

    number = contacts[name]
    print(f'your info is {number}')

    print(type(number))
