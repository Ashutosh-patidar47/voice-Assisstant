import pyttsx3
import datetime 
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pyaudio
import requests


engine=pyttsx3.init('sapi5') #using to take the voice 
voices=engine.getProperty('voice') 
print(voices[1]) #voices[1] is for the male voice 
engine.setProperty('voice', voices[1]) #set the voice

def speak(audio):  #this is speak function 
    engine.say(audio)    #engine is our system and speak the given audio
    engine.runAndWait()  #a function which the run and stop the voice

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif  hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am darak how may i help you")

def takecomand(): #it takes input from the user and return the string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...") #it is the prompt message
        r.pause_threshold = 1
        audio=r.listen(source) #it is the function which listen the audio from the microphone

    try:
        print('recognize....')
        run=r.recognize_google(audio,language='en-in')
        print(f"User said :{run}\n")
    except Exception as e:
        print(e)
        print("say that again please....")
        return "None"
    return run


if __name__ =="__main__":
    wishme()
    while True:
        run=takecomand().lower()

        #logic for executing the tasks based on query
        if "wikipedia" in run:
            speak("searching wikipedia...")
            run=run.replace("wikipedia",'')
            
            result=wikipedia.summary(run,sentences=2)
            speak("according to wikipedia")
            print(result)
            speak(result)

        elif 'open youtube' in run:
            webbrowser.open("www.youtube.com")

        elif 'open whatsup' in run:
            webbrowser.open("www.whatsup.com")

        elif 'open google' in run:
            webbrowser.open("www.google.com")

        elif 'open stackoverflow' in run:
            webbrowser.open("stackoverflow.com")

        elif 'open github' in run:
            webbrowser.open("github.com")
            speak("github opened in your browser")
        
        elif 'play music' in run:
            music_dir='C:\\Users\\DELL\\Music\\Songs'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        
        elif 'open vscode' in run:
            codePath = "C:\\Users\\DELL\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        
        elif 'open notepad' in run:
            notepadPath = "C:\\Windows\\System32\\notepad.exe"
            os.startfile(notepadPath)
        
        elif 'time' in run:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")


        elif 'exit' in run or 'quit' in run or 'bye' in run:
            speak("Goodbye! Have a great day!")
            break

        else:
            speak("I am sorry, I didn't understand that. Can you please repeat?")
        
