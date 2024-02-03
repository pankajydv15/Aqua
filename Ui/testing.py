from cProfile import label
from distutils.command.clean import clean
from email.mime import audio
from http.client import ImproperConnectionState
from lib2to3.refactor import MultiprocessRefactoringTool
from subprocess import TimeoutExpired
import sys
from pywikihow import search_wikihow
from time import time
from turtle import clear
from winsound import PlaySound
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
import pyautogui
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from AquaUI import Ui_MainWindow
from tasktest import wishMe



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',190)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        self.TaskExecution()


    def wishMe():
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            speak("Good Morning!")

        elif hour>=12 and hour<18:
            speak("Good Afternoon!")   

        else:
            speak("Good Evening!")  

        speak("I am Aqua. Please tell me how may I help you")       

    def takeCommand(self):
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

    
            
    def OpenApps():
        speak("ok sir!")

        if 'whatsapp' in Self.query:
            os.startfile("C:\\Users\\HP\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
        
        elif 'chrome' in self.query:
            os.startfile("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")

    def CloseApps():
        speak('ok sir!')

        if 'Whatsapp' in self.query:
            os.system("TASKKILL /F /im WhatsApp.exe")
        
        elif 'chorme' in self.query:
            os.system("TASKKILL /F /im chrome.exe")

        elif 'google' in self.query:
            os.system("TASKKILL /F /im msedge.exe")
            

    def TaskExecution(self):
        wishMe()

        def music():
            speak("which song")
            musicName = takecommand()
            
            if 'Meherbani' in musicName:
                os.startfile('C:\\Users\\HP\\Music\\Meherbaani.mp3')
            
            elif 'believer' in musicName:
                os.startfile('C:\\Users\\HP\\Music\\Believer.mp3')
            
            else:
                pywhatkit.playonyt(musicName)




        while True:
        
            self.query = self.takeCommand().lower()

            # Logic for executing tasks based on query
            if 'wikipedia' in self.query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)

            elif 'how are you aqua' in self.query:
                speak("I am fine sir. how are you sir?")

            elif 'what can you do' in self.query:
                speak('''I can help you to make your work easy
                        like, i can tell you time, add a reminder, save your passsword
                        send a mail, launch any app and much more. would you like to try me, 
                        just say play music''')
            
            elif 'screenshot' in self.query:
                ok = pyautogui.screenshot()
                ok.save ('C:\\Users\\HP\\Desktop\\Vs practice\\vs screenshot')

            elif 'alarm' in self.query:
                speak('what time sir!')
                Time = input(" what time sir!")

                while True:
                    Time_Ac = datetime.datetime.now()
                    now = Time_Ac.strftime("%H:%M:%S")

                    if now == Time:
                        speak("time to wake up sir!")
                        PlaySound("ringtone.mp3")
                        speak("alarm closed")

                    elif now>Time:
                        break


            elif 'open youtube' in self.query:
                webbrowser.open("youtube.com")

            elif 'youtube search' in self.query:
                speak("what do you want to search for?")
                search = takeCommand()
                webbrowser.open("https://www.youtube.com/results?search_query=" + search)
                speak("here is what i found for" + search)

            elif 'open google' in self.query:
                webbrowser.open("google.com")

            elif 'close Chrome' in self.query:
                CloseApps()

            elif 'close Whatsapp' in self.query:
                CloseApps()

            elif 'close google' in self.query:
                CloseApps()

            elif 'open stack overflow' in self.query:
                webbrowser.open("stackoverflow.com")

            elif 'search website' in self.query:
                speak("tell me the name of website")
                name = takeCommand()
                web = 'https://www.'+ name + '.com'
                webbrowser.open(web)


            elif 'open whatsappweb' in self.query:
                webbrowser.open("web.whatsapp.com")
                

            elif 'play music' in self.query or 'play song' in self.query:
                music()

            elif 'open whatsapp' in self.query:
                OpenApps()

            elif 'open Chorme' in self.query:
                OpenApps()    

            elif 'the time' in self.query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                speak(f"Sir, the time is {strTime}")

            elif ' what is love ' in self.query:
                speak("love is the most beautiful thing in the world,")
                speak("hahaha hahahahahahah hahahahahaha hahahahahaha hahahah hahaha habaha ah ha haahahaha ")

            elif 'open code' in self.query:
                codePath = "C:\\Users\\HP\\Desktop\\New folder\\New folder\\voice assistent"
                os.startfile(codePath)
                

            elif 'Change my name to' in self.query:
                query=query.replace("Change my name to", "")
                assname = query

            elif "change name" in self.query:
                speak("What would you like to call me, Sir ")
                assname = takeCommand()
                speak("Thanks for naming me")

            elif 'monsoon' in self.query:
                speak('which city')
                city= takeCommand()
                print(city)
            
                print("weather report for:- " + city)
                url ="https://wttr.in/{}".format(city)
                res = requests.get(url)
                print(res.text)
                speak(res.text)

            elif 'search' in self.query:
                speak("what do you want to search for?")
                search = takeCommand()
                webbrowser.open("https://www.google.com/search?q=" + search)
                speak("here is what i found for" + search)

            elif 'find a location' in self.query:
                speak("which location")
                location = takeCommand()
                webbrowser.open("https://www.google.co.in/maps/@28.6870351,77.0449321,15z" + location + "/&amp;")
                speak("here is what i found for" + location)

            elif 'good' in self.query or 'fine' in self.query:
                speak("its good to know that you are fine")

            elif 'you need a break' in self.query:
                speak('ok sir! call me anytime')
                speak ("just say wake up aqua")
                break

            elif 'are you there' in self.query:
                speak("At your service sir")

            elif 'tell me a joke' in self.query:
                speak(pyjokes.get_joke())
                speak("hahahahahahahahahahaha hehehehehehehe")

            elif 'how to' in self.query:
                speak('getting that from internet')
                op = query.replace("aqua","")
                max_result = 1
                how_to_func =search_wikihow(op,max_result)
                assert len(how_to_func)==1
                how_to_func[0].print()
                speak(how_to_func[0].summary)

            elif 'email to pankaj' in self.query:
                try:
                    speak("What should I say?")
                    content = takeCommand()
                    to = "idopankaj@gmail.com"    
                    pywhatkit.send_mail(to, content)
                    speak("Email has been sent!")
                except Exception as e:
                    print(e)    
                    speak("Sorry. I am not able to send this email")    
        
            elif 'exit' in self.query or 'bie' in self.query or 'bye' in self.query:
                speak("Ok sir, Take Care.")
                sys.exit(0)

    

startExecution = MainThread()
 
class Gui_start(QMainWindow): 

    def __init__(self):
        super().__init__()
        self. AquaUI = Ui_MainWindow()
        self.AquaUI.setupUi(self)
        self.AquaUI.pushButton.clicked.connect(self.startFunc)
        self.AquaUI.pushButton_2.clicked.connect(self.close)

    def startFunc(self):

        self.AquaUI.movies_2 = QtGui.QMovie("gyhf.jpg")
        self.AquaUI.label_2.setMovie(self.AquaUI.movies_2)
        self.AquaUI.movies_2.start()


        self.AquaUI.movies_3 = QtGui.QMovie("Jarvis_Gui (1).gif")
        self.AquaUI.label_3.setMovie(self.AquaUI.movies_3)
        self.AquaUI.movies_3.start()

        self.AquaUI.movies_4 = QtGui.QMovie("Iron_Template_1.gif")
        self.AquaUI.label_4.setMovie(self.AquaUI.movies_4)
        self.AquaUI.movies_4.start()

        self.AquaUI.movies_5 = QtGui.QMovie("initial.gif")
        self.AquaUI.label_5.setMovie(self.AquaUI.movies_5)
        self.AquaUI.movies_5.start()

        self.AquaUI.movies_6 = QtGui.QMovie("B.G_Template_1.gif")
        self.AquaUI.label_6.setMovie(self.AquaUI.movies_6)
        self.AquaUI.movies_6.start()

        startExecution.start()

        

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time) 



Gui_app = QApplication(sys.argv)
Gui_aqua = Gui_start()
Gui_aqua.show()
exit(Gui_app.exec_())

