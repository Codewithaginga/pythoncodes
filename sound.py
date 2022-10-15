import pyttsx3

sound1 = pyttsx3.init()

name = input('Enter your name: ')

sound1.say(f'hello {name}')

sound1.runAndWait()
