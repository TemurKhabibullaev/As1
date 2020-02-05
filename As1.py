# Temur Khabibullaev As1
string = 'word'
print(len(string))
print(string[0])
print(string[-1])
print(string.replace(string[2], ''))
print(string.upper())
print(string.title())
if string.isalpha():
    print("We got only alphabetical characters!")
else:
    print("We messed up.")
y = "Hello World I am Temur"
print(y.split()[0])
# Download pyttsx3 library first! Also stay connected to the internet
import pyttsx3
engine = pyttsx3.init()
engine.say("Hello my creator was Temur. I see a great potential in my creator! I wish him luck and success in achieving all of his goals!")
engine.runAndWait()
