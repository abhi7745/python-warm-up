import wikipedia
import pyttsx3

reader = pyttsx3.init()

user_input = input('Search Wikipedia/Google : ')
sentence_lines = int(input('How many lines you want : '))


try:
    result = wikipedia.summary(user_input, sentences = sentence_lines)
    print(result)
    reader.say(result)
    reader.runAndWait()

except:
    print('No result found, Please try again')