import pyttsx3
import wikipedia
import datetime as dt
import speech_recognition as sr
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')              # creating object of pyttsx3 and sapi5 is driver provided by pyttsx3
voice = engine.getProperty('voices')
engine.setProperty('voice',voice[1].id)     # if you change the voice keyword to voices thr girl voice will change to male voice

         # this function will read the string we pass on to it

def speak(text):           
    engine.say(text)
    engine.runAndWait()

speak("initializing ........Ikea......")

master = 'rajput'

            # this function make ikea to greet me
def wishme():
    hour = int(dt.datetime.now().hour)                  # the datetime function help to gather current hour and int is used to convert it to integer since by default everything is string

    if hour <= 0 and hour > 12:
        speak("good morning" + master)

    elif hour >= 12 and hour < 18 :
        speak("good afternoon" + master)

    else :
        speak("good evening" + master)

# this function take command from microphone

def takecommand() :
    r = sr.Recognizer()                 # recognizer is a function helps to break our speech and make it a sentence using HMM

    with sr.Microphone() as source :        # we are using microphone as our source
        print("listening...")
        audio = r.listen(source)            # listen is a function used as temporary server to form a connection till the approach of message

    try :
        print("recognizing...")
        query = r.recognize_google(audio, Language = 'en-in')       # here en-in means english india
        print("user-->{query}\n")

    except Exception as e :
        print("please! can you say that again??")
        query = None

    return query

def sendemail() :
    port = 587                                   # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = "mr.rajput7547@gmail.com"
    speak("provide reciever email")
    receiver_email = takecommand()
    password = input("Type your password and press enter:")         # asking to type the password to make it secure
    speak("please tell the ms you want to send")
    message = takecommand()

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        try :
            server.ehlo()                            # Can be omitted
            server.starttls(context=context)
            server.ehlo()                           # Can be omitted
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
            return 'email has been sent' 
    
        except Exception as e :             # this can happen due to any reason such as bad internet connection
            return 'something went wrong'

            # main program is here....
wishme()
query = takecommand()

def main() :

    # logics for executing tasks according to query

    if 'wikipedia' in query.lower() :
        speak("searching wikipedia...")
        query = query.replace("wikipedia","")
        results = wikipedia.summary(query , sentences = 3)
        print(results)
        speak(results)

    elif 'open youtube' in query.lower() :      # here .lower() is used so that there must not be any case sensitive conflict
        url = 'youtube.com'
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'      # it is the location of chrome in your system
        webbrowser.get(chrome_path).open(url)

    elif 'open google' in query.lower() :
        url = 'google.com'
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif '.com' in query.lower() :        # this helps to open any website with .com domain
        url = query
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'play music' in query.lower() :
        songs_dir = "E:\\Vikas Rajput\\Music"
        songs = os.listdir(songs_dir)       # here os is module and list directory is a function with the location provided to music folder
        print(songs)
        os.startfile(os.path.join(songs_dir , songs[0]))       # this is a command to play song present in direcory 

    elif 'time' in query.lower() :
        strtime = dt.datetime.now.strftime("%H:%M:%S")      # the time can be given  in any format
        speak("the time is" + strtime)

    elif 'send email' in query.lower() :
            speak(sendmail())

main()

