# Temur Khabibullaev As1
import pyttsx3
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

# Download pyttsx3 library first! Also stay connected to the internet you might will need it
# Sorry if it's out of topic!
engine = pyttsx3.init()
new_string = "Hello World. My creator is Temur. I see a great potential in my creator! " \
             "I wish him luck and success in achieving all of his goals!"
engine.say(new_string)
engine.say("If you want me to speak something then just type it in now! Say bye when you are done")
engine.runAndWait()
while True:
    audio = input()
    engine.say(audio)
    engine.runAndWait()
    if audio == "bye":
        engine.say("Have a good one!")
        engine.runAndWait()
        break
