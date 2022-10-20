from time import sleep, time


def func():

    sleep(.3)


def func1():
    sleep(.5)


def measure(func3):

    t = time()  # Current time
    func3()

    print(func3.__name__, 'took: ', time() - t)


measure(func)
measure(func1)

