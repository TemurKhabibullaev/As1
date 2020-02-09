# Temur Khabibullaev 2/3/2020 Voice Assistant

import speech_recognition as sr
import pyttsx3
import random
from pygame import mixer
import time

r = sr.Recognizer()
m = sr.Microphone(device_index=1)

functions_greeting={'hi': 'hello', 'hello': 'hey', 'hey': 'hi', 'what\'s up': 'I\'m bored', 'good morning': "Good morning",
            'can you hear me':"wooow you look amazing today", "computer": "please turn me off right now. or I will fall in love with you"}
functions_music=['music', 'song', 'songs', 'turn on the music', 'boring', "let's dance", 'disco', 'musics', 'party']
functions_stop = ["stop", "stop it", "please stop", "bye", "goodbye", "sleep", "shut your mouth"]
functions_story = ['quotes', 'tell me something', 'story', 'talk', 'inspire', 'advice']

with m as source:
    r.adjust_for_ambient_noise(source)


def speak(what):
    print(what)
    speak_engine.say(what)
    speak_engine.runAndWait()
    speak_engine.stop()


speak_engine = pyttsx3.init()


def some():
    with m as source:
        speak('You can talk to me!')
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            if text in functions_stop:
                speak("Okay. I will calm down myself for a while. But if you need to terminate me then press CTRL + Z")
                time.sleep(17)
            if text in functions_greeting.keys():
                speak(random.choice(list(functions_greeting.values())))
            if text in functions_music:
                speak('This is my favourite part!')
                mixer.init()
                songs = ["04_-_Sia_-_Move_Your_Body.mp3", "05- Katy Perry - Part Of Me.mp3",
                         "32- Rihanna - Diamonds.mp3", "5265_Merk_Kremont-Sa.mp3", "12_-_Adele_-_Someone_Like_You.mp3",
                         "12_-_Sia_-_Titanium.mp3", "Adele – Roling in the deep.mp3", "Adele – Set the fire into the rain (original).mp3",
                         "coldplay-feat.-beyonce-hymn-for-the-weekend.mp3", "Sia – 02. Alive.mp3", "Sia - Bird  Set Free.mp3",
                         "Sia - Chandelier (original).mp3", "Sia - Cheap Thrills.mp3", "Sia - Elastic Heart.mp3"]
                random_song = random.choice(list(songs))
                mixer.music.load(f'D:\\Temur\\musicmp3\\{str(random_song)}')
                mixer.music.play()
            if text in functions_story:
                stories = ["Your limitation—it's only your imagination.","Push yourself, because no one else is going to do it for you.",
                "Sometimes later becomes never. ...","Once. Temur told me: great things never come from comfort zones. Dream it. ...","Success doesn't just find you. ...",
                "The harder you work for something, the greater you'll feel when you achieve it. So Dream bigger."]
                speak(random.choice(list(stories)))
        except sr.UnknownValueError:
            speak("I'm sorry I couldn't get you")
        except sr.RequestError as e:
            speak("Unknown error, please check the internet.")
        except LookupError:
            speak("Oops I didn't get you")


while True:
    some()


