import pyjokes, pyttsx3

tts = pyttsx3.init()
jokes = pyjokes.get_joke()

print(jokes)
tts.say(jokes)
tts.runAndWait()