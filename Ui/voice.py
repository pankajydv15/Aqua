from distutils.command.clean import clean
from email.mime import audio
import sys
from tracemalloc import stop
from turtle import clear
import pyttsx3
import pywhatkit #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import requests
import pyjokes
import keyboard

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices)
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',190)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Aqua. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")
        speak("say that again please")  
        return "none"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('idopankaj@gmail.com', 'pankaj158')
    server.sendmail('idopankaj@gmail.com', to, content)
    server.close()

def music():
    speak("which song")
    musicName = takeCommand()
    
    if 'Meherbani' in musicName:
        os.startfile('C:\\Users\\HP\\Music\\Meherbaani.mp3')
    
    elif 'believer' in musicName:
        os.startfile('C:\\Users\\HP\\Music\\Believer.mp3')
    
    else:
        pywhatkit.playonyt(musicName)
        
def Whatsapp():
    speak("to whome you want to send message")
    name = takeCommand()

    if 'Pankaj New' in name:
        speak('tell me the message')
        msg = takeCommand()
        speak('what time')
        speak('time im hour!')
        hour = int(takeCommand())
        speak("time in minutes!")
        min = int(takeCommand())
        pywhatkit.sendwhatmsg("+919341314249",msg,hour,min,10)
        speak('ok sir , Sending whatsapp message !')

    elif 'Ashish' in name:
        speak('tell me the message')
        msg = takeCommand()
        speak('what time')
        speak('time im hour!')
        hour = int(takeCommand())
        speak("time in minutes!")
        min = int(takeCommand())
        pywhatkit.sendwhatmsg("+919852463821",msg,hour,min,10)
        speak('ok sir , Sending whasapp message !')

    else:
        speak('tell me the number')
        phone = int(takeCommand())
        speak('tell me the message')
        msg = takeCommand()
        speak('what time')
        speak('time im hour!')
        hour = int(takeCommand())
        speak("time in minutes!")
        min = int(takeCommand())
        pywhatkit.sendwhatmsg(phone,msg,hour,min,10)
        speak('ok sir , Sending whasapp message !')

def youtubeAuto():
    speak("what is your command ?")
    comm = takeCommand()

    if 'pause' in comm:
        keyboard.press ('space bar')

    elif "restart" in comm:
        keyboard.press('0')

    elif 'mute' in comm:
        keyboard.press ('m')

    elif 'skip' in comm:
        keyboard.press ('l')
    
    elif 'full screen' in comm:
        keyboard.press ('f')



if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'how are you aqua' in query:
            speak("I am fine sir. how are you sir?")

        elif 'what can you do' in query:
            speak('''I can help you to make your work easy
                      like, i can tell you time, add a reminder, save your passsword
                      send a mail, launch any app and much more. would you like to try me, 
                      just say play music''')
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   

        elif 'open whatsappweb' in query:
            webbrowser.open("web.whatsapp.com")

        elif 'play music' in query or 'play song' in query:
            music()

        elif 'whatapp message' in query or 'send Whatsapp message' in query:
            Whatsapp()
            
        elif 'open whatsapp' in query:
            wpath = 'C:\\Users\\HP\\AppData\\Local\\WhatsApp\\WhatsApp.exe'
            os.startfile(wpath)

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'ok aqua what is love' in query or 'what is love' in query:
            speak("love is the most beautiful thing in the world,")
            speak("hahaha hahahahahahah hahahahahaha hahahahahaha hahahah hahaha habaha ah ha haahahaha ")

        elif 'open code' in query:
            codePath = "C:\\Users\\Hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'Change my name to' in query:
            query=query.replace("Change my name to", "")
            assname = query

        elif "change name" in query:
            speak("What would you like to call me, Sir ")
            assname = takeCommand()
            speak("Thanks for naming me")

        elif 'monsoon' in query:
            speak('which city')
            city= takeCommand()
            print(city)
        
            print("weather report for:- " + city)
            url ="https://wttr.in/{}".format(city)
            res = requests.get(url)
            print(res.text)
            speak(res.text)

        elif 'search' in query:
            speak("what do you want to search for?")
            search = takeCommand()
            webbrowser.open("https://www.google.com/search?q=" + search)
            speak("here is what i found for" + search)

        elif 'find a location' in query:
            speak("which location")
            location = takeCommand()
            webbrowser.open("https://www.google.co.in/maps/@28.6870351,77.0449321,15z" + location + "/&amp;")
            speak("here is what i found for" + location)

        elif 'good' in query or 'fine' in query:
            speak("its good to know that you are fine")

        elif 'you need a break' in query:
            speak('ok sir! call me anytime')
            speak ("just say wake up aqua")
            break

        elif 'are you there' in query:
            speak("At your service sir")

        elif 'tell me a joke' in query:
            speak(pyjokes.get_joke())
            speak("HAheHAheHAheHAheHAheHAheHA hehehehehehehe")

        elif 'email to pankaj' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "idopankaj@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)    
                speak("Sorry. I am not able to send this email")    
        
        elif 'pause' in query:
            keyboard.press ('space bar')

        elif "restart" in query:
            keyboard.press('0')

        elif 'mute' in query:
            keyboard.press ('m')

        elif 'skip' in query:
            keyboard.press ('l')
        
        elif 'full screen' in query:
            keyboard.press ('f')

        elif 'youtube tool' in query:
            youtubeAuto( )

        elif 'exit' in query:
            speak("Ok sir, Take Care.")
            sys.exit(0)


