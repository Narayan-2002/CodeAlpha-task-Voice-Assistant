import speech_recognition as sr
import pyttsx3
import os
import subprocess
import wikipedia
import datetime
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()
voices = tts_engine.getProperty('voices')
tts_engine.setProperty('voice', voices[1].id)  

def speak(text):
    tts_engine.say(text)
    tts_engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio)
            print(f"User said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            speak("Sorry, my speech service is down.")
            return ""

def open_application(app_name):
    try:
        if app_name == "youtube":
            speak("Opening YouTube")
            subprocess.Popen(["start", "chrome", "https://www.youtube.com"], shell=True)
        elif app_name == "google":
            speak("Opening Google")
            subprocess.Popen(["start", "chrome", "https://www.google.com"], shell=True)
        elif app_name == "wikipedia":
            speak("Opening Wikipedia")
            subprocess.Popen(["start", "chrome", "https://www.wikipedia.org"], shell=True)
        elif app_name == "time":
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The current time is {current_time}")
        elif app_name == "cmd":
            speak("Opening Command Prompt")
            os.system("start cmd")
        elif app_name == "facebook":
            speak("Opening Facebook")
            subprocess.Popen(["start", "chrome", "https://www.facebook.com"], shell=True)
        elif app_name == "instagram":
            speak("Opening Instagram")
            subprocess.Popen(["start", "chrome", "https://www.instagram.com"], shell=True)
        elif app_name == "file":
            speak("Opening File Explorer")
            os.system("explorer")
        elif app_name == "whatsapp":
            speak("Opening WhatsApp")
            subprocess.Popen(["start", "chrome", "https://web.whatsapp.com"], shell=True)
        elif app_name == "zoomapp":
            speak("Opening Zoom")
            subprocess.Popen(["start", "zoom"], shell=True)
        elif app_name == "vscode":
            speak("Opening Visual Studio Code")
            subprocess.Popen(["code"], shell=True)
        elif app_name == "calculator":
            speak("Opening Calculator")
            os.system("calc")
        elif app_name == "stop":
            speak("Goodbye!")
            return
        else:
            speak("Application not recognized.")
    except Exception as e:
        speak(f"Failed to open {app_name} due to {e}")

def perform_calculation(operation, num1, num2):
    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        result = num1 / num2
    else:
        result = "Invalid operation"
    return result

if __name__ == "__main__":
    speak("Hello, I am Nova, your personal voice assistant. How can I help you today?")
    while True:
        command = listen()

        if "open" in command:
            app_name = command.replace("open", "").strip()
            open_application(app_name)
        elif "calculate" in command:
            speak("What operation would you like to perform? Addition, subtraction, multiplication, or division?")
            operation = listen()
            speak("Please say the first number")
            num1 = float(listen())
            speak("Please say the second number")
            num2 = float(listen())
            result = perform_calculation(operation, num1, num2)
            speak(f"The result of {operation}ing {num1} and {num2} is {result}")
        elif "exit" in command or "bye" in command:
            speak("Goodbye!")
            break
        else:
            speak("I did not understand that command.")
