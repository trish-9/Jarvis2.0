import pyttsx3
import datetime
import speech_recognition as sr

import os
import pyfirmata
engine = pyttsx3.init()
engine.say("WELCOME TO THE HOME AUTOMATION PROJECT")
engine.runAndWait()
board = pyfirmata.Arduino('COM13')
relay_pin_1 = board.get_pin('d:6:o')
relay_pin_1.write(0)
relay_pin_2 = board.get_pin('d:7:o')
relay_pin_2.write(0)


def turn_on():
    relay_pin_1.write(1)
    print("Relay turned on")

def turn_off():
    relay_pin_1.write(0)
    print("Relay turned off")
def on_fan():
    relay_pin_2.write(1)
def off_fan():
    relay_pin_2.write(0)

# Initialize recognizer

turn_on()
on_fan()



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listneing...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(f"user said: {query}\n")

    except Exception as e:
        speak("say that again..")
        return "none"
    return query













while True:
    # if 1:
    query = takecommand().lower()
    

    if 'hello' in query:
        speak("hey annu! you know me !")

    

    if 'do you have any girlfriends' in query:
        speak("yes , i have many girlfriends")
    
    

       
        

    if "stop" in query:
             engine = pyttsx3.init()
             engine.say("off light")
             engine.runAndWait()
             turn_on()

    if "light"  in query:
            engine = pyttsx3.init()
            engine.say("on light")
            engine.runAndWait()
            turn_off()
    if "off" in query:
            engine = pyttsx3.init()
            engine.say("off motor")
            engine.runAndWait()
            on_fan()
    if "fan" in query:
            engine = pyttsx3.init()
            engine.say("on motor")
            engine.runAndWait()
            off_fan()

      

        
        
 

   
   

    

    
