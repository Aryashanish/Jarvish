import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import wikipedia
import os
import random


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voices' , voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning sir")

    elif(hour >=12 and hour < 18):
        speak("Good Afternoon sir")

    else:
        speak("Good Evening sir")

    speak("I am Jarvis Sir How may i help you")
 
def takecommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()

    with sr.Microphone() as source:
        # print("Listening.......")
        # r.pause_threshold = 1
        # r.adjust_for_ambient_noise(source)
        # audio = r.listen(source)
        r.adjust_for_ambient_noise(source)
        print("Say something I Recognizing !!")
        audio = r.listen(source, phrase_time_limit=5)
    
    try:
        print("Recognizing.......")
        # query = r.recognize_google(audio , language='en-in')  #Using google for voice recognition.
        query = r.recognize_google(audio , language='en-in')
        print(f"User said - {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned

    return query
    

if __name__ == "__main__":
    wishme()
    # speak("Hi Acharya juhi lal shansih")
    while (True):
        query = takecommand().lower()    # Logic of executing task
        if 'wikipedia' in query:
            print("Searching Wikipedia........")
            query = query.replace('wikipedia',"")
            result = wikipedia.summary(query , sentences=2)
            print("According To Wikipedia.")
            print(result)
            speak(result)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'play music' in query:
            music_dir = 'D:\\Non-Critical\\@Music'
            songs = os.listdir(music_dir)
            suffle = random.randint(1,100)
            print(songs[suffle])
            os.startfile(os.path.join(music_dir , songs[suffle]))

        elif 'now time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codepath = "C:\\Users\\aryashanish\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)\
        
        elif 'hello jarvis' in query:
            speak("Hallo Sir How may i help you")

        elif 'your name' in query:
            speak("my name is jarvis")

        elif 'exit programe' or 'exit program' in query:
            exit()

    
