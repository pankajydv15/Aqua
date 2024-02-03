from fileinput import close
from click import command
from winsound import PlaySound
import pyttsx3
import pywhatkit
import speech_recognition as sr
import datetime
import os
import webbrowser
import pyjokes
import keyboard
import pyautogui
import wikipedia
import smtplib
import sys
import sqlite3
from voice import wishMe
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Aqua import Ui_MainWindow

Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty("voices")
print (voices)
Assistant.setProperty('voices',voices[1].id)

def speak(audio):
    print("   ")
    Assistant.say(audio)
    Assistant.runAndWait()

class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        self.Taskexe()

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
            return query.lower()
        
    

    def sendEmail(to, content):
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login('idopankaj@gmail.com', 'pankaj158')
            server.sendmail('idopankaj@gmail.com', to, content)
            server.close()


    def Taskexe(self):
        wishMe()

        def OpenApps():
            speak("ok Sir!")

            if "whatsapp" in self.query:
                os.startfile("C:\\Users\\HP\\AppData\\Local\\WhatsApp\\WhatsApp.exe")

            elif "chrome" in self.query:
                os.startfile("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")

            elif "edge" in self.query:
                os.startfile("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")

            elif "Aqua report" in self.query:
                os.open("C:\\Users\\HP\\Desktop\\Aqua Report")

        def CloseApps():
            speak('ok sir!')

            if "whatsapp" in self.query:
                os.system("taskkill /f /im WhatsApp.exe")

            elif "edge" in self.query:
                os.system("TASKKILL /F /im msedge.exe ")
            
            elif "chrome" in self.query:
                os.system("taskkill /f /im chrome.exe")



        def music():
            speak("which song")
            musicName = self.takeCommand()
        
            if 'Meherbani' in musicName:
                os.startfile('C:\\Users\\HP\\Music\\Meherbaani.mp3')
            
            elif 'believer' in musicName:
                os.startfile('C:\\Users\\HP\\Music\\Believer.mp3')
            
            else:
                pywhatkit.playonyt(musicName)

        def youtubeAuto():
            speak("what is your command ?")
            comm = self.takeCommand()

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
        
        def Whatsapp():
            speak("to whome you want to send message")
            name = self.takeCommand()

            if 'Pankaj New' in name:
                speak('tell me the message')
                msg = self.takeCommand()
                speak('what time')
                speak('time im hour!')
                hour = int(self.takeCommand())
                speak("time in minutes!")
                min = int(self.takeCommand())
                pywhatkit.sendwhatmsg("+919341314249",msg,hour,min,10)
                speak('ok sir , Sending whasapp message !')

            elif 'Ashish' in name:
                speak('tell me the message')
                msg = self.takeCommand()
                speak('what time')
                speak('time im hour!')
                hour = int(self.takeCommand())
                speak("time in minutes!")
                min = int(self.takeCommand())
                pywhatkit.sendwhatmsg("+919852463821",msg,hour,min,10)
                speak('ok sir , Sending whasapp message !')

            else:
                speak('tell me the number')
                phone = int(self.takeCommand())
                speak('tell me the message')
                msg = self.takeCommand()
                speak('what time')
                speak('time im hour!')
                hour = int(self.takeCommand())
                speak("time in minutes!")
                min = int(self.takeCommand())
                pywhatkit.sendwhatmsg(phone,msg,hour,min,10)
                speak('ok sir , Sending whasapp message !')

        while True:

            self.query = self.takeCommand().lower()

            if "hello" in self.query or "hello aqua" in self.query or "hii" in self.query:
                speak("Hello sir!")
                speak("how are you")

            elif "fine" in self.query or "good" in self.query:
                speak("Its good to know that you are fine")

            elif "wake up" in self.query:
                speak("at your service")

            elif "how are you" in self.query:
                speak("I am always good sir")

            elif "what can you do" in self.query:
                speak('''I can help you to make your work easy
                        like, i can tell you time, add a reminder, save your passsword
                        send a mail, launch any app and much more. would you like to try me, 
                        just say play music''')
                
            elif "go to sleep" in self.query:
                speak("Okh sir!")
                break

            elif 'the time' in self.query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                speak(f"Sir, the time is {strTime}")

            elif "open whatsapp" in self.query:
                OpenApps()

            elif "open chrome" in self.query:
                OpenApps()

            elif "open edge" in self.query:
                OpenApps()

            elif "open youtube" in self.query:
                webbrowser.open("youtube.com")

            elif "open google" in self.query:
                webbrowser.open("google.com")

            elif "open facebook" in self.query:
                webbrowser.open("https://www.facebook.com/")

            elif "close whatsapp" in self.query:
                CloseApps()

            elif "close edge" in self.query:
                CloseApps()

            elif "close chrome" in self.query:
                CloseApps()

            elif "song" in self.query or "music" in self.query:
                music()

            elif "what is love" in self.query:
                speak('''Love encompasses a range of strong and positive emotional and mental states,
                    from the most sublime virtue or good habit, the deepest interpersonal affection,
                    to the simplest pleasure.''')

            elif 'search' in self.query:
                speak("what do you want to search for?")
                search = self.takeCommand()
                webbrowser.open("https://www.google.com/search?q=" + search)
                speak("here is what i found for" + search)

            elif " are you there" in self.query:
                speak("At your service sir!")

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

            elif 'youtube search' in self.query:
                    speak("what do you want to search for?")
                    search = self.takeCommand()
                    webbrowser.open("https://www.youtube.com/results?search_query=" + search)
                    speak("here is what i found for" + search)

            elif 'search website' in self.query:
                    speak("tell me the name of website")
                    name = self.takeCommand()
                    web = 'https://www.'+ name + '.com'
                    webbrowser.open(web)

            elif 'wikipedia' in self.query:
                    speak('Searching Wikipedia...')
                    query = query.replace("wikipedia", "")
                    results = wikipedia.summary(query, sentences=2)
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)

            elif 'find a location' in self.query:
                    speak("which location")
                    location = self.takeCommand()
                    webbrowser.open("https://www.google.co.in/maps/@28.6870351,77.0449321,15z" + location + "/&amp;")
                    speak("here is what i found for" + location)

            elif "open aqua report" in self.query:
                OpenApps()

            elif 'email to pankaj' in self.query:
                    try:
                        speak("What should I say?")
                        content = self.takeCommand()
                        to = "idopankaj@gmail.com"    
                        pywhatkit.send_mail(to, content)
                        speak("Email has been sent!")
                    except Exception as e:
                        print(e)    
                        speak("Sorry. I am not able to send this email") 

            elif 'screenshot' in self.query:
                    ok = pyautogui.screenshot()
                    ok.save(f'C:\\Users\\HP\\Desktop\\Vs practice\\vs screenshot')

            elif 'tell me a joke' in self.query:
                speak(pyjokes.get_joke())
                speak("hahahahahahahahahahaha hehehehehehehe")

            elif 'pause' in self.query:
                keyboard.press ('space bar')

            elif "restart" in self.query:
                keyboard.press('0')

            elif 'mute' in self.query:
                keyboard.press ('m')

            elif 'skip' in self.query:
                keyboard.press ('l') 
            
            elif 'full screen' in self.query:
                keyboard.press ('f')

            elif 'youtube tool' in self.query:
                youtubeAuto()

            elif "msg ashish" in self.query:
                Whatsapp()
            
            elif "Pankaj New" in self.query:
                Whatsapp()

            elif "sleep" in self.query or "bye" in self.query:
                speak("ok sir. take Care")
                exit()
    
            

StartExecution = MainThread()

class Gui_start(QMainWindow):

    def __init__(self):
        super().__init__()
        self.Aqua = Ui_MainWindow()
        self.Aqua.setupUi(self)
        self.Aqua.pushButton.clicked.connect(self.startFunc)
        self.Aqua.pushButton_2.clicked.connect(self.close)

    def startFunc(self):

        self.Aqua.movies_2 = QtGui.QMovie("Jarvis_Gui (1)")
        self.Aqua.label_2.setMovie(self.Aqua.movies_2)
        self.Aqua.movies_2.start()


        self.Aqua.movies_3 = QtGui.QMovie("Iron_Template_1.gif")
        self.Aqua.label_3.setMovie(self.Aqua.movies_3)
        self.Aqua.movies_3.start()

        self.Aqua.movies_4 = QtGui.QMovie("initial.gif")
        self.Aqua.label_4.setMovie(self.Aqua.movies_4)
        self.Aqua.movies_4.start()


        self.Aqua.movies_6 = QtGui.QMovie("B.G_Template_1.gif")
        self.Aqua.label_6.setMovie(self.Aqua.movies_6)
        self.Aqua.movies_6.start()

        self.Aqua.movies_7 = QtGui.QMovie("__02-____.gif")
        self.Aqua.label_7.setMovie(self.Aqua.movies_7)
        self.Aqua.movies_7.start()

        StartExecution.start()


Gui_app = QApplication(sys.argv)
Gui_aqua = Gui_start()
Gui_aqua.show()
exit(Gui_app.exec_())
