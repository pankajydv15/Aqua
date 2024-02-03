from distutils.command.clean import clean
from email.mime import audio
from subprocess import TimeoutExpired
import sys
from pywikihow import search_wikihow
from time import time
from tracemalloc import stop
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

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
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

def TaskExe():

    while True:
        query = takeCommand()

        if 'hello' in query:
            speak('how are you')

        elif 'hii' in query:
            speak("yeah")

TaskExe()