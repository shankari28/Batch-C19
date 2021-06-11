import pyttsx3    #pip install pyttsx3
import speech_recognition as sr    #pip install SpeechRecognition
import datetime
import wikipedia    #pip install wikipedia
import webbrowser
import random
import sys
import time 
import os
import os.path
from requests import get
import smtplib   #pip install secure-smtpib
import subprocess
import pywhatkit as kit
import wolframalpha
import pyjokes      #pip install pyjokes
import pyautogui    #pip install pyautogui
import ctypes
import winshell
import simplejson as json
from urllib.request import urlopen
import shutil



MASTER="shankari"
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voices',voices[0].id)
  


#print((sr.Microphone.list_microphone_names()))

#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#to convert voice into text
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=3,phrase_time_limit=5)

    try:
        print("Analysing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        speak("Say that again please")
        return "none"
    return query

#to wish
def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good Morning " + MASTER)
    elif hour>=12 and hour <18:
        speak("Good afternoon " + MASTER)
    else:
        speak("Good evening " + MASTER)
    speak("i am mike. please tell me how can i help you")
    
#to send email
def sendmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremailid', 'password')
    server.sendmail("sender mailid", to, content)
    

speak("loading your AI personal assistant mike")

if __name__=='__main__':
    wish()
    while True:
        
    # if 1:
        
        query = takeCommand().lower()
           
       #logic building for tasks   

        if 'open notepad' in query:
            npath = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(npath)

        elif 'open word' in query:
            npath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office"
            os.startfile(npath)

        elif 'open command prompt' in query:
            os.system('start cmd')

        elif 'play music'in query:
            songs_dir="C:\\Users\\user\\OneDrive\\Desktop\\windows\\music"
            songs=os.listdir(songs_dir)
            print(songs)
            os.startfile(os.path.join(songs_dir,songs[0]))

        elif 'ip address'in query:
            ip = get('https://api.ipify.org').text
            speak(f"your ip address is {ip}")

        elif 'wikipedia' in query:
            speak("Searching wikipedia...")
            query=query.replace("Wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("www.youtube.com")

        elif 'search google'in query:
            speak('shankari, what should i search on google')
            content = takeCommand()
            webbrowser.open(f"{content}")   #if chrom {set chrome_path and webbrowser.get(chrome_path).open()} 

        elif 'open google' in query:
            webbrowser.open("www.google.com")

        elif 'instagram' in query:
            webbrowser.open("www.instagram.com")

        elif 'reddit'in query:
            webbrowser.open("www.reddit.com")

        elif 'news' in query:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')

        elif 'send message' in query:
            speak("What should I send?")
            content = takeCommand()
            kit.sendwhatmsg("+91number", content, 16,46)

        elif 'search youtube' in query:
            speak("What should I search?")
            content = takeCommand()
            kit.playonyt(content)

        elif 'email to mike' in query:
            try:
                speak("What should I send?")
                content = takeCommand() 
                to ="sender mailid"
                sendmail(to, content)
                speak("Mail has been sent succesfully")
                
            except Exception as e:
                print(e)
                speak("sorry sir, i am not able to send this mail")

        elif 'time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"{MASTER} the time is {strTime}")
  
        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, shankari")

        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")

        elif "who made you" in query or "who created you" in query: 
            speak("I have been created by shankari.")

        elif 'why you came to world' in query:
            speak("Thanks to sanky. further It's a secret")

#to find a joke
        elif 'tell me a joke' in query:
            speak(pyjokes.get_joke())
                
        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin Recycled")

        elif 'you can sleep' in query:
            speak("thanks for using me shankari, have a good day")
            sys.exit()

#to close any application
        elif 'close notepad' in query:
            speak("okay shankari, closing notepad")
            os.system('pause')
        
#to set an alarm
        elif 'set alarm' in query:
            nn = int(datetime.datetime.now().hour)
            if nn==22:
                songs_dir ="C:\\Users\\user\\OneDrive\\Desktop\\windows\\music"
                songs = os.listdir(songs_dir)
                os.startfile(os.path.join(songs_dir, songs[0]))

        elif 'shut down the sytem' in query:
            os.system("shutdown /s /t 5")

        elif 'restart the system' in query:
            os.system("shutdown /r /t 5")

        #speak("shankari, do you have any other work")
