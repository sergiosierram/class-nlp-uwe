import speech_recognition as sr
import pyaudio
from gtts import gTTS
import os
import pygame

# Initialize the recognizer
recognizer = sr.Recognizer()

def speak(text):
    # Use Google Text-to-Speech to convert text to speech
    tts = gTTS(text=text, lang='en')
    tts_file = 'response.mp3'
    tts.save(tts_file)

    # Initialize pygame for playing audio
    pygame.mixer.init()
    pygame.mixer.music.load(tts_file)
    pygame.mixer.music.play()

    # Wait until the audio is finished playing
    while pygame.mixer.music.get_busy(): 
        pygame.time.Clock().tick(10)  # Check every 100 ms

    os.remove(tts_file)  # Remove the file after playing

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't understand that.")
            return None
        except sr.RequestError:
            speak("Could not request results from the speech recognition service.")
            return None

def process_command(command):
    if command:
        if "hello" in command:
            speak("Hello! How can I assist you today?")
        elif "your name" in command:
            speak("I am your voice assistant.")
        elif "bye" in command:
            speak("Goodbye! Have a great day!")
            return False  # To exit the loop
        else:
            speak("I can only respond to simple greetings for now.")
    return True  # To continue the loop

def main():
    speak("Hello, I am your voice assistant. How can I help you?")
    while True:
        command = listen()
        if command is None:  # If there was an error in recognition
            continue
        if not process_command(command):
            break

if __name__ == "__main__":
    main()
