import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import os
import sys

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 170)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Use female voice

# Set your default PIN code here
DEFAULT_PINCODE = "517501"


def talk(text):
    print("\U0001F399 Hey Bro:", text)
    engine.say(text)
    engine.runAndWait()


def take_command():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print("\U0001F3A7 Listening...")
        listener.adjust_for_ambient_noise(source, duration=1)
        voice = listener.listen(source)
    try:
        command = listener.recognize_google(voice)
        command = command.lower()
        print("\U0001F5E3 You said:", command)
    except sr.UnknownValueError:
        talk("Sorry bro, I didn’t catch that.")
        return ""
    except sr.RequestError:
        talk("Network issue with Google service.")
        return ""
    return command


def run_hey_bro():
    command = take_command()
    if command == "":
        return

    if "hey bro" in command:
        command = command.replace("hey bro", "").strip()

    if any(kw in command for kw in ["play", "music", "song"]):
        song = command.replace("play", "").strip()
        talk(f"Playing {song} on YouTube \U0001F3B6")
        pywhatkit.playonyt(song)

    elif "time" in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk(f"It’s {time} ⏰")

    elif "date" in command:
        date = datetime.datetime.now().strftime('%A, %d %B %Y')
        talk(f"Today is {date} \U0001F4C5")

    elif "pincode" in command or "pin code" in command:
        talk(f"Your default PIN code is {DEFAULT_PINCODE} \U0001F4EE")

    elif "who is" in command:
        person = command.replace("who is", "").strip()
        try:
            info = wikipedia.summary(person, sentences=1)
            talk(info)
        except:
            talk("Sorry, I couldn’t find information about that person.")

    elif "joke" in command:
        talk(pyjokes.get_joke())

    elif "whatsapp" in command:
        talk("Opening WhatsApp \U0001F4F1")
        os.system("start https://web.whatsapp.com/")
        path = "C:\\Users\\satis_asxzdl9\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
        os.startfile(path) if os.path.exists(path) else talk("WhatsApp not found \U0001F61F")

    elif "instagram" in command:
        talk("Opening Instagram \U0001F308")
        os.system("start https://www.instagram.com")

    elif "spotify" in command:
        talk("Opening Spotify \U0001F3B5")
        path = "C:\\Users\\satis_asxzdl9\\AppData\\Roaming\\Spotify\\Spotify.exe"
        os.startfile(path) if os.path.exists(path) else talk("Spotify not found \U0001F61F")

    elif "vs code" in command or "visual studio" in command:
        talk("Opening Visual Studio Code \U0001F4BB")
        path = "C:\\Users\\satis_asxzdl9\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(path) if os.path.exists(path) else talk("VS Code not found \U0001F61F")

    elif "file manager" in command:
        talk("Opening File Manager \U0001F4C1")
        os.system("explorer")

    elif "linkedin" in command:
        talk("Opening LinkedIn \U0001F4BC")
        os.system("start https://www.linkedin.com")

    elif "naukri" in command:
        talk("Opening Naukri.com \U0001F50D")
        os.system("start https://www.naukri.com")

    elif "microsoft word" in command or "open word" in command:
        talk("Opening Microsoft Word \U0001F4DD")
        path = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
        os.startfile(path) if os.path.exists(path) else talk("Word not found \U0001F61F")

    elif "excel" in command:
        talk("Opening Microsoft Excel \U0001F4C8")
        path = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
        os.startfile(path) if os.path.exists(path) else talk("Excel not found \U0001F61F")

    elif "powerpoint" in command:
        talk("Opening Microsoft PowerPoint \U0001F4FD")
        path = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
        os.startfile(path) if os.path.exists(path) else talk("PowerPoint not found \U0001F61F")

    elif "chat gpt" in command:
        talk("Opening ChatGPT \U0001F4AC")
        os.system("start https://chatgpt.com")

    elif "grok" in command:
        talk("Opening Grok by xAI \U0001F916")
        os.system("start https://grok.x.ai")

    elif "youtube" in command and "open" in command:
        talk("Opening YouTube \U0001F3A5")
        os.system("start https://www.youtube.com")

    elif "command prompt" in command or "cmd" in command:
        talk("Opening Command Prompt \U0001F4BB")
        os.system("start cmd")

    elif "notepad" in command:
        talk("Opening Notepad \U0001F4DD")
        os.system("start notepad")

    elif "google colab" in command:
        talk("Opening Google Colab \U0001F680")
        os.system("start https://colab.research.google.com")

    elif "chrome" in command or "google chrome" in command:
        talk("Opening Google Chrome \U0001F4D6")
        path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        os.startfile(path) if os.path.exists(path) else talk("Google Chrome not found \U0001F61F")

    elif "jupyter" in command or "jupyter notebook" in command:
        talk("Opening Jupyter Notebook \U0001F4D3")
        os.system("jupyter notebook")

    elif "zoom" in command:
        talk("Opening Zoom \U0001F4F9")
        path = "C:\\Users\\satis_asxzdl9\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"
        os.startfile(path) if os.path.exists(path) else talk("Zoom not found \U0001F61F")

    elif "google meet" in command:
        talk("Opening Google Meet \U0001F3A5")
        os.system("start https://meet.google.com")

    elif any(word in command for word in ["exit", "stop", "bye"]):
        talk("Okay bro, see you later \U0001F44B")
        sys.exit()

    elif any(word in command for word in ["hello", "hi", "what's up"]):
        talk("Hey bro! I'm here. What can I do for you?")

    else:
        talk("I heard you, but I don’t understand that yet \U0001F605")


# Start the assistant
talk("Yo! I'm Hey Bro – your personal voice assistant \U0001F4A1")
while True:
    run_hey_bro()
