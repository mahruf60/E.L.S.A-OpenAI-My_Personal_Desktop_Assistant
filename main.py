import speech_recognition as sr
import os 
import pyttsx3 as ps
import webbrowser
import openai
import datetime
from config import apikey
import random


chatStr = ""
def chat(query):
    global chatStr
    print(chatStr)
    openai.api_key = apikey
    chatStr += f"Shuvo: {query}\n Elsa: "
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        prompt= chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: Wrap this inside of a  try catch block
    say(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]


def ai(prompt):
    openai.api_key = apikey
    text = f"OpenAI response for Prompt: {prompt} \n ****************\n\n"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Ensure this model is used
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )

    # todo: wrap this inside of a try catch block 
    print(response["choices"][0]["message"]["content"])
    text += response["choices"][0]["text"]
    if not os.path.exists(("OpenAi")):
        os.mkdir("OpenAi")
    with open(f"OpenAi/{''.join(prompt.split('intelligence')[1:]).strip() }.txt", "w") as f:
        f.write(text)

def say(text): 
    engine = ps.init()
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.6
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language = "en-US")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from Elsa"

if __name__ == '__main__':
    print("Hello, I am Elsa AI")
    say("Elsa A.I")
    while True:
        print("Listening...")
        query = takeCommand()
        sites = [["youtube","https://www.youtube.com"],["wikipedia","https://www.wikipedia.com"],["google","https://www.google.com"],["linkedin","https://www.linkedin.com"],["messenger","https://www.messenger.com"],["whatsapp","https://www.whatsapp.com"],["github","https://www.github.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
               say(f"Opening {site[0]} sir...")
               webbrowser.open(site[1])

        if "open music" in query:
            musicPath = r"C:\Users\User\Downloads\Maestro Chives, Egzod, Neoni - Royalty [NCS Release].mp3"
            os.startfile(musicPath)

        elif "the time" in query:
            musicPath = r"C:\Users\User\Downloads\Maestro Chives, Egzod, Neoni - Royalty [NCS Release].mp3"
            hour = datetime.datetime.now().strftime("%H")
            miniute = datetime.datetime.now().strftime("%M:")
            seconds = datetime.datetime.now().strftime("%S")
            say(f"Sir time is {hour} hour {miniute} miniutes and {seconds} seconds.")
        
        elif "open camera".lower() in query.lower():
            os.system(r"C:\Users\User\OneDrive\Desktop\Camera.lnk")

        elif "Using Artificial Intelligence".lower() in query.lower():
            ai (prompt=query)
        
        elif "Elsa Quit".lower() in query.lower():
            exit()
        
        elif "reset chat".lower() in query.lower():
            chatStr = ""

        else:
            print("Chatting...")
            chat(query)
        
        # say(query)

