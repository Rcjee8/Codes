#My implementation of tts in python
import pyttsx3

engine = pyttsx3.init()
engine.say("Hello")
engine.runAndWait()


while True:
    message = input()
    if message == "quit":
        engine = pyttsx3.init()
        engine.say("Good bye!")
        engine.runAndWait()
        break
    else:
        engine = pyttsx3.init()
        engine.say(message)
        engine.runAndWait()
