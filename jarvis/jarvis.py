import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import random
import pywhatkit
import sys


engine = pyttsx3.init('sapi5' )
voices = engine.getProperty('voices')
engine.setProperty('voice' , voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour <12:
        speak("good morning!")
        
    elif hour>=12 and hour <18:
        speak ("good afternoon")

    else:
        speak ('good evening')

    speak("i am jarvis sir please tell me how may i help you")

def takeCommand():


    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=1,phrase_time_limit=5)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")                      
        

    except Exception as e:
        print(e)       

    
        print("Say that again please...")
        return "None" 
    return query



def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('dragmaster019@gmail.com', 'Drag master1234')
    server.sendmail('sarthakmondal999@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("sir,what should i search on google")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")

        elif "send message" in query:
            pywhatkit.sendwhatmsg("+917875721870", "BT20CSE204 PRESENT SIR ",6,00)
            
        elif "play songs on youtube" in query:

            pywhatkit.playonyt("kabira")

        elif 'open stackoverflow' in query:

            webbrowser.open("stackoverflow.com")




        elif 'play music' in query:
            music_dir = "C:\\music"

            songs =os.listdir(music_dir)
            
            rd = random.choice(songs)

            print(songs)
            os.startfile(os.path.join(music_dir, rd))

        elif 'the time' in query:

            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")

        elif'open visual studio code' in query:
            codepath = "C:\\Users\\SARTHAK MONDAL\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif'close vs code' in query:
            speak("closing vs code")
           
            os.startfile("taskkill /f /im Microsoft VS Code\\Code.exe")


        elif 'email to sarthak' in query:
            try:
                speak("what should I say?")
                content = takeCommand()
                to = "dragmaster019@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("sorry sir. I am not able to send this email") 

        elif "you can sleep now" in query:

            speak("thanks for using me sir, have a good day.")
            sys.exit()

        speak("sir, do u have any other work")

        




        


    
    