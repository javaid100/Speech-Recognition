import pyttsx3
import datetime
import speech_recognition as sr
import os
import re
import webbrowser
import sys

engine = pyttsx3.init('sapi5')
engine.setProperty('voice', "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")

def Speak(audio):
    engine.setProperty('rate', 150)
    engine.say(audio)
    engine.runAndWait()

def Greeting():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning!")
        Speak("Good Morning!")
    elif hour>=12 and hour<18:
        print("Good Afternoon!")
        Speak("Good Afternoon!")
    else:
        print("Good Evening!")
        Speak("Good Evening!")
    print("I am Z Sir. Please tell me how may I help you! \n")    
    Speak("I am Z Sir. Please tell me how may I help you!")
            
def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language= 'en-pk')
        print(f"User said: {query} \n")
    except Exception:
        print("Please! Say that again...\n")
        Speak("Please! Say that again...")
        return "None"
    return query

def Assistant(command):       
    if 'hello' in command:
        Greeting()
    elif 'shutdown' in command:
        print('Bye Sir. Have a nice day')
        Speak('Bye Sir. Have a nice day')
        sys.exit()        
    elif 'open' in command:
        reg_ex = re.search('open (.+)', command)
        if reg_ex:
            domain = reg_ex.group(1)
            print(domain)
            url = 'https://www.' + domain
            webbrowser.open(url)
            print("")
            Speak('The website you have requested has been opened for you Sir.')
        else:
            pass
    elif 'play music' in command:
            Speak("Enjoy the Music Sir!")
            music_dir = 'D:/AUDIO MOVIE SONGS/2020 AUDIO SONGS/LOVE AAJ KAL 2'
            songs = os.listdir(music_dir)
            print(songs)
            print(len(songs))
            os.startfile(os.path.join(music_dir, songs[15]))
            sys.exit()    
    elif 'play video' in command:
            Speak("Enjoy the Video Sir!")
            video_dir = 'D:\\VIDEO MOVIE SONGS\\FAST AND FURIOUS SONGS'
            videos = os.listdir(video_dir)
            print(videos)    
            os.startfile(os.path.join(video_dir, videos[7]))
            sys.exit()
    elif 'time' in command:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Sir, The time is {strTime}\n")
            Speak(f"Sir, The time is {strTime}")        
    elif 'search' in command:
         command = command.replace("search", "")
         webbrowser.open('https://www.google.com/search?q=' + command)   
         Speak("That's what I found on web according to " + command)
         sys.exit()
    elif 'exit' in command:
         sys.exit()
    
while True:
    Assistant(TakeCommand())  