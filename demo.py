def func(message):
    def message_sender():

        print(message)

    message_sender()

# Func('accessing the scope')


class Person:

    age = 7
    height = 8


#p = Person()

class Expo:

    side = 8

    def expo1(self):

        return self.side ** 2


e = Expo()
print(e.expo1())

