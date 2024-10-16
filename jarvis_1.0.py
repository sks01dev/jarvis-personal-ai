import pyttsx3  # pip install pyttsx3
import datetime
import speech_recognition as sr # pip install SpeechRecognition
import wikipedia # pip install wikipedia
import smtplib
import webbrowser as wb
import psutil # pip install psutil
import pyjokes # pip install pyjokes
import os
import pyautogui # pip install pyautogui
import json
import requests
from urllib.request import urlopen
import wolframalpha # pip install wolframalpha
import time


# Initialize the engine
engine = pyttsx3.init()
wolframalpha_app_id = "E24HKL-E88K85RJQE"

# Function to make the engine speak
def speak(audio):
    engine.say(audio)  # Use the audio parameter instead of hardcoding 'hello world'
    engine.runAndWait()

# Function to announce the current time
def time_():
    Time = datetime.datetime.now().strftime("%H:%M:%S")  # for 12-hour clock use %I, for 24-hour clock use %H
    speak("The current time is")
    speak(Time)

# Function to announce the current date
def date_():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().strftime("%B")  # Get month as full name (e.g., January)
    day = datetime.datetime.now().day
    speak("The current date is")
    speak(f"{day} {month}, {year}")  # Speak the date as a formatted string

def wishme():
    speak("welcome back Shivam")
    time_()
    date_()

    hour = datetime.datetime.now().hour

    if hour>=6 and hour<12:
        speak("Good Morning Sir!")
    elif(hour>=12 and hour<18):
        speak("Good afternoon sir!")
    elif hour>=18 and hour<24:
        speak("good evening sir!")
    else:
        speak("good night!")
        
    speak("jarvis at your service. please tell me how can i help you today")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("recognizing....")
        query = r.recognize_google(audio,language='en-US')
        print(query)

    except Exception as e:
        print(e)
        print("say that again please....")
        return "None"
    return query


def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls() # for this function to work, you must enable low security inn your gmail which you are going to use as a sender
    server.login('username@gmail.com','password')
    server.sendmail('sender email address here',to,content)
    server.close()

def cpu():
    usage = str(psutil.cpu_percent())
    speak("cpu is at"+usage)

    battery = psutil.sensors_battery()
    speak("battery is at")
    speak(battery.percent)
    speak("percent")

def joke():
    joke_ = pyjokes.get_joke()
    print(joke_)
    speak(joke_)

def screenshot():
    img = pyautogui.screenshot()
    img.save('C:/Users/dell/Desktop/screenshot.png')

if __name__ == "__main__":

    wishme()

    while True:
        query = takeCommand().lower()

        # All commands will be stored in lower case for easy recognition

        if 'time' in query:  # tell us time when asked
            time_()

        if 'date' in query:  # tell us date when asked
            date_()

        elif 'wikipedia' in query:
            speak("searching....")
            query = query.replace('wikipedia', '')
            result = wikipedia.summary(query, sentences=3)
            speak("according to wikipedia")
            print(result)
            speak(result)

        elif 'send email' in query:
            try:
                speak("what should i say?")
                content = takeCommand()
                # provide receiver email address
                speak("who is the receiver?")
                receiver = input("Enter receiver's email:")
                to = receiver
                sendEmail(to, content)
                speak(content)
                speak("email has been sent.")
            except Exception as e:
                print(e)
                speak("unable to send email.")

        elif 'search in chrome' in query:
            speak("what should i search?")
            chromepath = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search + '.com')  # only open websites with '.com' at end.

        elif 'search youtube' in query:
            speak("what should i search?")
            search_term = takeCommand().lower()
            speak("here we go to youtube!")
            wb.open("https://www.youtube.com/results?search_query=" + search_term)

        elif 'search google' in query:
            speak("what should i search?")
            search_term = takeCommand().lower()
            speak('searching....')
            wb.open('https://www.google.com/search?q=' + search_term)

        elif 'cpu' in query:
            cpu()

        elif 'joke' in query or 'jokes' in query:
            joke()

        elif 'screenshot' in query:  # Check screenshot command before note-taking
            screenshot()
            speak("Screenshot taken and saved on your desktop.")

        elif 'go offline' in query:
            speak("going offline sir!")
            quit()

        elif 'word' in query:
            speak("opening ms word")
            ms_word = r'C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE'
            os.startfile(ms_word)

        elif 'write a note' in query:
            speak("What should I note, sir?")
            notes = takeCommand()
            file = open('notes.txt', 'w')
            speak("Sir, should I include date and time?")
            ans = takeCommand()
            if 'yes' in ans or 'sure' in ans:
                strTime = datetime.datetime.now().strftime('%H:%M:%S')
                file.write(strTime)
                file.write(":-")
                file.write(notes)
                speak("Done taking notes!")
            else:
                file.write(notes)
            file.close()

        elif 'show notes' in query:
            speak('showing notes')
            file = open('notes.txt', 'r')
            note_text = file.read()
            print(note_text)
            speak(note_text)
            file.close()


        elif 'remember that' in query:
            speak("what should i remember?")
            memory = takeCommand()
            speak("you asked me to remember that"+memory)
            remember = open('memory.txt','w')
            remember.write(memory)
            remember.close()

        elif 'do you remember' in query:
            remember = open('memory.txt','r')
            speak("you asked me to remember that"+remember.read())

        
        elif 'news' in query:
            try:
                jsonObj = urlopen("https://newsapi.org/v2/top-headlines?country=us&category=entertainment&apiKey=4657224e1bc44901a794649d8107d448")
                data = json.load(jsonObj)
                i=1

                speak("here are some top headlines fromm the entertainment industry")
                print("==============TOP HEADLINES============"+'\n')
                for item in data['articles']:
                    print(str(i)+'. '+item['title']+'\n')
                    print(item['description']+'\n')
                    speak(item['title'])
                    i=i+1

            except Exception as e:
                print(str(e))

        elif 'where is' in query:
            query = query.replace('where is','')
            location = query
            speak("you asked to locate"+location)
            wb.open_new_tab("https://www.google.com/maps/place/"+location)

        elif 'what is' in query or 'who is' in query:
            client = wolframalpha.Client(wolframalpha_app_id)
            res = client.query(query)

            try:
                print(next(res.results).text)
                speak(next(res.results).text)

            except StopIteration:
                print ("No Results")

        elif 'stop listening' in query:
            speak("for how many seconds you want me to stop listening to your commands")
            ans = int(takeCommand())
            time.sleep(ans)
            print(ans)

        elif 'logout' in query:
            os.system("shutdown -l")

        elif 'restart' in query:
            os.system("shutdown /r /t 1")

        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")

        
