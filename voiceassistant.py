import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

# Microsoft voices : sapi5
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

# selecting male or female voices: id[0]=David ,id[11]=Zira
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")

    else:
        speak("Good Evening!")

    # speak("I am Chhittti the Robot       Speed 1 tera byte...Memory 1 zetaa byte")
    speak("I am Jarvis..Tell me how may I help You")


def takeCommand():
    # it takes microphone input from users and returns string output

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Listening.........')
        # r.pause_threshold=1
        audio = r.listen(source)

    try:
        print('Recognizing.....')
        query = r.recognize_google(audio)
        # print(f"User said:{query}\n")
        print('USER said:', query)

    except Exception as e:
        print(e)
        print('Say that again please....')
        return "None"

    return query


if __name__ == "__main__":
    wishMe()

    while True:
        query = takeCommand().lower()

        # logic for executing tasks on query

        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            print('it takes a little while')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)



        elif 'open youtube' in query:
            webbrowser.open('youtube.com')


        elif 'open google' in query:
            webbrowser.open('google.com')



        elif 'play music' in query:
            music_dir = "C:/Users/yesho/Desktop/songss"
            songs = os.listdir(music_dir)
            # print(songs)
            os.startfile(os.path.join(music_dir, songs[3]))



        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")


        elif 'open code' in query:
            codePath = "C:/Users/yesho/AppData/Local/Programs/Microsoft VS Code/Code.exe"
            os.startfile(codePath)


        # to close the Jarvis Program
        elif 'shutdown' in query:
            speak('Shutting down')
            print('Shutting down')
            break;
