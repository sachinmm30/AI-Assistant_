import pyttsx3
import speech_recognition as sr
import datetime, wikipedia, pywhatkit

engine = pyttsx3.init()
engine.say("Hello! I am your AI Assistant.")
engine.runAndWait()

def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        print("Recognizing..")
        command = recognizer.recognize_google(audio)
        print(f"you said: {command}")
    except Exception:
        return "Sorry, i didnt get that."
    return command.lower()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def run_assistant():
    command = take_command()

    if "time" in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speak(f"The current time is : {time}")

    elif "who is" in command:
        person = command.replace('who is', '').strip()
        try:
            info = wikipedia.summary(person, sentence=1)
            speak(info)
        except wikipedia.exceptions.PageError:
            speak("Sorry, i couldn't find sny informaton on that person.")
        except wikipedia.exceptions.DisambiguationError as e:
            speak("That name is too ambigious. please be more specific.")
        except Exception as e:
            speak("An error occured while searching wikipedia.")
            print(e)     

    elif "play" in command:
        song = command.replace('play', '')
        speak(f"palying: {song}")
        pywhatkit.playonyt(song)

    elif "exit" in command:
        speak("Goodbye!")
        exit()

    else:
        speak("Please say the command again.")

if __name__ == "__main__":
    speak("hello! How can i help you")
    while True:
        run_assistant()

print(take_command)