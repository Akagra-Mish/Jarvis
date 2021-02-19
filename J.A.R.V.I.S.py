import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import os
import sys
# import pyaudio

engine = pyttsx3.init('sapi5')

client = wolframalpha.Client('Your_App_ID')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)

def speak(audio):
    print('Jarvis: ' + audio)
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')

    if currentH >= 18 and currentH !=0:
        speak('Good Evening!')

greetMe()

speak('Hello Sir, I am your digital assistant JARVIS!')
speak('How may I help you?')

def myCommand():
   
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                      
        print("Listening...")
        r.pause_threshold =  1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('User said: ' + query + '\n')
        
    except sr.UnknownValueError:
        speak('Sorry sir! I didn\'t get that! Try typing the command!')
        query = str(input('Command: '))

    return query
        

if __name__ == '__main__':

    while True:
    
        query = myCommand();
        query = query.lower()
        
        if 'open youtube' in query:
            speak('okay')
            webbrowser.open('www.youtube.com')

        elif 'open google' in query:
            speak('okay')
            webbrowser.open('www.google.co.in')

        elif 'open gmail' in query:
            speak('okay')
            webbrowser.open('www.gmail.com')

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))

        elif 'email' in query:
            speak('Who is the recipient???')
            recipient = myCommand()

            if 'I' in recipient:
                try:
                    speak('What should I say? ')
                    content = myCommand()
        
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("akagramishra54@gmail.com", 'akagramish')
                    server.sendmail('akagramishra54@gmail.com', "akagra195@gmail.com", 'Subject: hi')
                    server.close()
                    speak('Email sent!')

                except:
                    speak('Sorry Sir! I am unable to send your message at this moment!J')


        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            speak('okay')
            speak('Quitting... Sir, have a good day.')
            sys.exit()

        elif 'Jarvis quit' in query or 'abort' in query or 'stop' in query:
            speak('okay')
            speak('Bye Sir, have a good day.')
            sys.exit() 

        elif 'open firefox' in query:
            speak('okay')
            webbrowser.open('www.firefox.com')       
           
        elif 'hello' in query:
            speak('Hello Sir')

        elif 'hi' in query:
            speak('hi sir')    
        
        elif 'What is my pin code' in query:
            speak('201306')

        elif 'bye' in query:
            speak('Bye Sir, have a good day.')
            sys.exit()
                                    
        elif 'play music' in query:
            music_folder = 'C:\\Users\\Public\\Music\\Sample Music\\Kalimba.mp3'
            music = 'Kalimba'
            random_music = music_folder + random.choice(music) + '.mp3'
            os.system(random_music)
                  
            speak('Okay, here is your music! Enjoy!')

        elif 'open engineers' in query:
            speak('Okay')
            webbrowser.open('www.ska-engineers.in')    
            

        else:
            query = query
            speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('WOLFRAM-ALPHA says - ')
                    speak('Got it.')
                    speak(results)
                    
                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('Got it.')
                    speak('Wikipedia says - ')
                    speak(results)
        
            except:
                webbrowser.open('www.google.com')
        
        speak('Next Command! Sir!')
