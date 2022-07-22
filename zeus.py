import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import wikipedia

engine = pyttsx3.init('sapi5')
voices =engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
    
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir!!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon sir!!")
    else :
        speak("good Evening sir!!")
    speak("Hello   Sir    I am Zeus you personal   assistent")
    

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..........")
        r.adjust_for_ambient_noise(source,duration=1)
        audio =r.listen(source)
        
    try:
        print("Recognizing..........")
        query = r.recognize_google(audio,Language ='en-in')
        print(f"User Said:{query}\n")
    
    except Exception as e:
        print("can you repeat plz!!")
        return " none "
    return query
    
    
if __name__ == "__main__":
    wishMe()
    while True:
        query = takecommand().lower()
        
        if 'open googke' in query:
            webbrowser.open('google.com')
        
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
            
        elif 'open github.com' in query:
            webbrowser.open('https://github.com/1999-Ary')
        
        if 'wikipedia' in query:
            speak('Searching Results')
            query = query.replace('wikipedia','')
            results = wikipedia.summary(query,sentences=2)
            speak("Sir!! According to search results")
            speak(results)
            print(results)
            
            
            
        