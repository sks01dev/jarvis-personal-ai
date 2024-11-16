import pyttsx3  # Text-to-speech conversion library
import datetime
import speech_recognition as sr  # Speech recognition library
import wikipedia  # Wikipedia API for Python
import smtplib  # Library for sending emails
import webbrowser as wb  # To open web pages
import psutil  # To access system and battery details
import pyjokes  # For fetching random jokes
import os  # To interact with the operating system
import pyautogui  # For capturing screenshots
import json  # For handling JSON data
import requests  # To send HTTP requests
from urllib.request import urlopen  # For URL operations
import wolframalpha  # For WolframAlpha API integration
import time  # To handle time-based tasks

# Initialize text-to-speech engine
engine = pyttsx3.init()
wolframalpha_app_id = "E24HKL-E88K85RJQE"  # WolframAlpha API Key

# Function to make the assistant speak a given text
def speak(audio):
    """Speak the provided text aloud."""
    engine.say(audio)
    engine.runAndWait()

# Function to announce the current time
def announce_time():
    """Fetch and speak the current time."""
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    speak("The current time is")
    speak(current_time)

# Function to announce the current date
def announce_date():
    """Fetch and speak the current date."""
    today = datetime.datetime.now()
    date_str = f"{today.day} {today.strftime('%B')}, {today.year}"
    speak("The current date is")
    speak(date_str)

# Function to greet the user based on time of day
def greet_user():
    """Greet the user and announce the current time and date."""
    speak("Welcome back, Shivam.")
    announce_time()
    announce_date()

    # Determine greeting based on current hour
    hour = datetime.datetime.now().hour
    if 6 <= hour < 12:
        speak("Good morning, sir!")
    elif 12 <= hour < 18:
        speak("Good afternoon, sir!")
    elif 18 <= hour < 24:
        speak("Good evening, sir!")
    else:
        speak("Good night!")

    speak("Jarvis at your service. Please tell me how I can help you today.")

# Function to take audio command from the user
def take_command():
    """Listen for and recognize user's speech input."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio, language='en-US')
        print(f"User said: {command}")
    except Exception as e:
        print(e)
        print("Could you please say that again?")
        return "None"
    return command.lower()

# Function to send an email
def send_email(to, content):
    """Send an email with the specified content to the specified address."""
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()  # Enable TLS
        server.login('username@gmail.com', 'password')  # Replace with actual credentials
        server.sendmail('sender email address here', to, content)
        server.close()
        speak("Email has been sent.")
    except Exception as e:
        print(e)
        speak("Unable to send email.")

# Function to report CPU usage and battery status
def report_cpu():
    """Speak out the CPU usage percentage and battery level."""
    usage = psutil.cpu_percent()
    speak(f"CPU usage is at {usage} percent.")
    battery = psutil.sensors_battery()
    if battery:
        speak(f"Battery is at {battery.percent} percent.")

# Function to tell a random joke
def tell_joke():
    """Fetch and speak a random joke."""
    joke = pyjokes.get_joke()
    print(joke)
    speak(joke)

# Function to take a screenshot
def take_screenshot():
    """Capture and save a screenshot to the desktop."""
    screenshot = pyautogui.screenshot()
    screenshot.save('C:/Users/dell/Desktop/screenshot.png')
    speak("Screenshot taken and saved on your desktop.")

# Main program loop
if __name__ == "__main__":
    greet_user()

    while True:
        query = take_command()

        # Process commands based on keywords
        if 'time' in query:
            announce_time()

        elif 'date' in query:
            announce_date()

        elif 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace('wikipedia', '')
            result = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(result)
            speak(result)

        elif 'send email' in query:
            speak("What should I say?")
            content = take_command()
            speak("Who is the receiver?")
            receiver = input("Enter receiver's email: ")
            send_email(receiver, content)

        elif 'search in chrome' in query:
            speak("What should I search?")
            chromepath = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
            search_term = take_command()
            wb.get(chromepath).open_new_tab(search_term + '.com')

        elif 'search youtube' in query:
            speak("What should I search on YouTube?")
            search_term = take_command()
            wb.open(f"https://www.youtube.com/results?search_query={search_term}")

        elif 'search google' in query:
            speak("What should I search on Google?")
            search_term = take_command()
            wb.open(f'https://www.google.com/search?q={search_term}')

        elif 'cpu' in query:
            report_cpu()

        elif 'joke' in query:
            tell_joke()

        elif 'screenshot' in query:
            take_screenshot()

        elif 'go offline' in query:
            speak("Going offline. Goodbye!")
            break

        elif 'write a note' in query:
            speak("What should I note down?")
            notes = take_command()
            with open('notes.txt', 'w') as file:
                speak("Should I include the date and time?")
                if 'yes' in take_command():
                    file.write(f"{datetime.datetime.now().strftime('%H:%M:%S')} - {notes}\n")
                else:
                    file.write(notes)
                speak("Note has been taken.")

        elif 'show notes' in query:
            with open('notes.txt', 'r') as file:
                note_content = file.read()
                print(note_content)
                speak(note_content)

        elif 'remember that' in query:
            speak("What should I remember?")
            memory = take_command()
            with open('memory.txt', 'w') as file:
                file.write(memory)
            speak("I will remember that.")

        elif 'do you remember' in query:
            with open('memory.txt', 'r') as file:
                speak("You asked me to remember " + file.read())

        elif 'news' in query:
            try:
                news_url = "https://newsapi.org/v2/top-headlines?country=us&category=entertainment&apiKey=4657224e1bc44901a794649d8107d448"
                response = urlopen(news_url)
                data = json.load(response)
                speak("Here are the top entertainment headlines.")
                for i, article in enumerate(data['articles'], 1):
                    print(f"{i}. {article['title']}")
                    speak(article['title'])
            except Exception as e:
                print(e)

        elif 'where is' in query:
            location = query.replace('where is', '').strip()
            speak(f"Locating {location}")
            wb.open_new_tab(f"https://www.google.com/maps/place/{location}")

        elif 'what is' in query or 'who is' in query:
            client = wolframalpha.Client(wolframalpha_app_id)
            try:
                res = client.query(query)
                answer = next(res.results).text
                speak(answer)
                print(answer)
            except StopIteration:
                speak("I couldn't find an answer.")

        elif 'stop listening' in query:
            speak("For how many seconds should I stop listening?")
            duration = int(take_command())
            time.sleep(duration)

        elif 'logout' in query:
            os.system("shutdown -l")

        elif 'restart' in query:
            os.system("shutdown /r /t 1")

        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")
