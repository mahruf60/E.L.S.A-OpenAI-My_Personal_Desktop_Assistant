
# Elsa AI - Virtual Assistant
Elsa AI is an interactive virtual assistant built using Python. The assistant is capable of performing a variety of tasks, such as browsing the web, opening files, playing music, retrieving the current time, and even chatting using OpenAI's GPT-3.5 model. It supports both speech recognition and speech synthesis to allow seamless communication.


## Features

- Voice-based Commands: Elsa AI listens to your voice commands and responds accordingly.
- Web Navigation: Open websites such as YouTube, Google, LinkedIn, Wikipedia, and more.
- Play Music: Play an MP3 file from a specified location on your system.
- Tell Time: Get the current time spoken aloud.
- Open Camera: Launch a camera application through a predefined link.
- Chat with AI: Chat with Elsa, powered by OpenAI's GPT-3.5 model.
- Text-to-Speech: Elsa speaks back to you using pyttsx3 for natural voice output.
- Save Chat Logs: Conversations with Elsa are saved as text files in the "OpenAi" folder.


## Requirements
Before running this project, ensure you have the following libraries installed:

- speechrecognition: For recognizing speech commands.
- pyttsx3: For text-to-speech functionality.
- openai: To interact with the OpenAI API for AI-based responses.
- webbrowser: To open web pages based on voice commands.
- os: For handling system file operations.
- datetime: For retrieving and speaking the current time.
You can install the required libraries by running:

 pip install SpeechRecognition,pyttsx3,openai,pyaudio.


## Setup
1.API Key: To interact with OpenAI, you will need an API key. You can sign up for access here.
Save your API key in a file called config.py:

-apikey = "your-api-key-here"

2.Music File Path: The script plays music from the specified file path. Make sure to update the musicPath variable with the correct file path of the MP3 you want to play:

 -musicPath = r"C:\path\to\your\music.mp3"

 3.Camera Link: The script opens a shortcut to a camera application. Ensure you have the correct path to the camera application shortcut on your machine. 
 -os.system(r"C:\path\to\Camera.lnk")

## Code Structure
### Main Functions
1.chat(query):

- Sends a query to OpenAI's GPT-3.5 model and gets a response.
- Responds through text-to-speech and saves the conversation log.

2.ai(prompt):

- Uses OpenAI's API to generate responses to AI-related queries.
- Saves the responses in a text file under the OpenAi directory.

3.say(text):

- Converts text into speech using pyttsx3.

4.takeCommand():

- Listens for voice commands from the user using the microphone.
- Returns the recognized text or an error message if recognition fails.

## Voice Commands

- Open Websites: Elsa can open predefined websites like YouTube, Google, Wikipedia, etc., using the command "Open [youtube]".

- Play Music: The music file set in the musicPath variable will be played.

- Get Time: Ask Elsa the current time with the command "Els the time now?".

- Open Camera: Open a camera application using a predefined link.

- Chat with AI: Start a conversation with the AI by saying anything like "Chat with me".

- Exit: Say "Elsa Quit" to stop the assistant.


## File Management

- Conversation Logs: All AI responses are saved in the OpenAi folder on your system. Each conversation is saved in a text file, with the filename based on the query prompt.

## Troubleshooting
- If Elsa doesn't respond correctly, make sure your microphone is properly configured and the correct API key is set.

- Ensure your Python environment has all dependencies installed.

- For errors related to speech recognition, check if the microphone and internet connection are functioning properly.# E.L.S.A-OpenAI-My_Personal_Desktop_Assistant
