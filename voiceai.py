import pyttsx3 as p
import speech_recognition as sr
import webbrowser
import os 
import datetime
from tkinter import Tk,Label
from datetime import date
import app
import random
import pygame
import subprocess
root=Tk()
root.title("AI")
root.geometry("600x600")

today = date.today()
engine = p.init()
rate=engine.getProperty('rate')
engine.setProperty('rate',130)
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[3].id)
def speak(text):
   engine.say(text)
   engine.runAndWait()
def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        print("Good Morning!")
        speak("Good Morning!")
        alternative_sentences = ["I am you voice assistance , how may I help you?","I'm here as your voice assistant. How can I assist you today?","As your voice assistant, I'm ready to help. What do you need?","Here to assist you as your voice companion. How can I be of service?","I'm your voice-enabled assistant, available to help. What can I do for you?","I'm at your service as your voice assistant. What assistance do you require?","Consider me your voice-activated helper. How may I assist you today?","I'm here as your voice-activated aid. What can I help you with?","Your voice assistant is ready and waiting to assist you. What's your request?","Think of me as your voice-operated assistant. How may I be of assistance?","Your voice-activated assistant is standing by to help. What do you need assistance with?"]
        ra=random.choice(alternative_sentences)
        print(f"{ra}")    
        speak(ra)
    elif hour>=12 and hour<18:
        print("Good Afternoon!") 
        speak("Good Afternoon!")   
        alternative_sentences = ["I am you voice assistance , how may I help you?","I'm here as your voice assistant. How can I assist you today?","As your voice assistant, I'm ready to help. What do you need?","Here to assist you as your voice companion. How can I be of service?","I'm your voice-enabled assistant, available to help. What can I do for you?","I'm at your service as your voice assistant. What assistance do you require?","Consider me your voice-activated helper. How may I assist you today?","I'm here as your voice-activated aid. What can I help you with?","Your voice assistant is ready and waiting to assist you. What's your request?","Think of me as your voice-operated assistant. How may I be of assistance?","Your voice-activated assistant is standing by to help. What do you need assistance with?"]
        ra=random.choice(alternative_sentences)
        print(f"{ra}")    
        speak(ra)
        
    else:
        speak("good Evening!")
        print("Good Evening!")  
        alternative_sentences = ["I am you voice assistance , how may I help you?","I'm here as your voice assistant. How can I assist you today?","As your voice assistant, I'm ready to help. What do you need?","Here to assist you as your voice companion. How can I be of service?","I'm your voice-enabled assistant, available to help. What can I do for you?","I'm at your service as your voice assistant. What assistance do you require?","Consider me your voice-activated helper. How may I assist you today?","I'm here as your voice-activated aid. What can I help you with?","Your voice assistant is ready and waiting to assist you. What's your request?","Think of me as your voice-operated assistant. How may I be of assistance?","Your voice-activated assistant is standing by to help. What do you need assistance with?"]
        ra=random.choice(alternative_sentences)
        print(f"{ra}")    
        speak(ra)


def search_location(location):
   try:
      formatted_location_name = location.replace(' ', '+')
      url = f"https://www.google.com/maps/place/{formatted_location_name}"

    # Open the URL in a web browser
      webbrowser.open(url)
      speak('This is what I found Sir')
   except:
      speak('Please check your Internet')
    



def date33():
   today= datetime.date.today()   
   speak(f"Today's date is{today}")
   print("Today's date is:", today)

def takeCommand():
    print("Listenning.....")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.energy_threshold=1000
        r.dynamic_energy_threshold = False
        r.adjust_for_ambient_noise(source,1.2)
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio,language='en-in')
            print(f"User said: {query}") 
            return query
        except Exception as e:
            return "some error Occured sorrry from assistance"


# Function to play music files in a directory
def play_music_in_directory(directory):
    # Initialize pygame mixer
    pygame.mixer.init()

    # Get list of files in the directory
    files = os.listdir(directory)

    # Filter only music files (you can adjust this filter as needed)
    music_files = [f for f in files if f.endswith(('.mp3', '.wav', '.ogg'))]

    # Loop through music files and play them
    for music_file in music_files:
        print("Now playing:", music_file)
        pygame.mixer.music.load(os.path.join(directory, music_file))
        pygame.mixer.music.play()
        # Wait for music to finish playing before moving to the next file
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

if __name__=="__main__":
   wish()
   while True:
      query=takeCommand()
      sites=[["youtube","https://www.youtube.com"],["wikipedia","https://www.wikipedia.org/"],["google","https://www.google.com/"],["facebook","https://www.facebook.com/"],["instagram","https://www.instagram.com/"]]
      for site in sites:
         if f"Open {site[0]}".lower() in query.lower():
            speak(f"opening {site[0]} sir....")
            webbrowser.open(site[1])
      hyy=["hello", "hey", "hi there", "howdy", "greetings"]
      for hi in hyy:
         if hi.lower() in query.lower():
            wish()
      date1=["date","today's date"]
      for dt in date1:
         if dt.lower() in query.lower():
            date33()
      if f"play music".lower() in query.lower():
         play_music_in_directory(r"E:\python\mp3player\music")

      times=["time"]
      for time in times:
         if time.lower() in query.lower():
            strftime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir the time is {strftime}")
      if "open file explorer".lower() in query.lower():
         os.system("explorer")
      bye=["Farewell","Goodbye","Adieu","See you later","good bye","exit","So long","Tata","Adios","Ciao","Auf Wiedersehen","Cheerio","Toodle-oo","Bye-bye"]
      for i in bye:
         if i.lower() in query.lower():
            speak("bye bye sir have a great day")
            exit()
      wha=["what about you","And you","How about yourself","What's your take","Any thoughts from your end","Your perspective","How do you feel about it","Your opinion","And what's your story","What are your feelings on this","Your turn","how are you"]
      for r in wha:
         if r.lower() in query.lower():
            speak(" i am having a good day sir ")
            speak("what can i do for you ?")
      goods =["Morning greetings","good morning","Dawn salutations","AM hellos","Sunrise welcomes","Early day greetings","Daybreak greetings","A.M. greetings","Sunrise salutations","Early morning hellos","Daylight welcomes" ]
      for good in goods:
         if good.lower() in query.lower():
            wish()
      whats= ["What's happening","What's the news","whatsApp","what's up""What's new","Any updates"]
      for what in whats:
         if what.lower() in query.lower():
            replies = ["Not much, just enjoying the morning. How about you?","Just getting started with my day. How about yourself?","Hey there! Just woke up. What's going on?","Hey! Just catching up on some news. How about you?","Morning! Not much, just sipping on some coffee. What's up with you?","Hey, not too much. Just taking it easy. What's happening with you?","Hey! Just getting ready for the day. What's new with you?","Morning! Just enjoying the sunrise. How about you?","Hey! Not much, just getting some work done. What's going on?","Morning! Just woke up. What's the plan for today?"]
            ran=random.choice(replies)
            speak(ran)

      if 'location' in query.lower():
         speak('Which place are you looking for ?')
         temp_audio = takeCommand()
         speak('Locating...')
         location=temp_audio
         search_location(location)
      if "propose" in query.lower():
         speak("My purpose in life is to love you, cherish, and support you through every moment. With you, I have found my reason to strive for greatness, to embrace challenges, and to celebrate every joy. You are the heartbeat of my existence, the inspiration behind my every endeavor, and the light that illuminates my path. Together, lets continue to journey hand in hand, creating memories, overcoming obstacles, and nurturing our love. I am committed to building a future with you, filled with laughter, adventure, and endless love.")

      if "news" in query.lower():
         speak("opening news sir")
         subprocess.run(['python', r'E:\python\mp3player\news.py'])


      
      # Replace 'other_script.py' with the name of the Python file you want to run

    
   
root.mainloop()


