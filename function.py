import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(command)
            
    except:
        print("Nova cannot hear you....")
        talk("Nova cannot hear you")
    return command

question = ["Who is", "Who might", "Who exactly is", "Who are", "What is", "What's", "Can you tell me about" ,"What can you tell me about" ,"Who’s that", "Could you explain", "Who’s", "Do you know who" ,"Who would that be", "Who’s behind", "Who’s the person named", "Whose identity is ", "Who goes by the name"]

def run_nova():
    print("Hi I’m Nova. How can I help you?")
    while True:
        command = take_command()
        print(command)
        if 'play' in command:
            song = command.replace('play', '')
            talk('playing ' + song)
            pywhatkit.playonyt(song)
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time is ' + time)
        elif question in command:
            person = command.replace("What is", '')
            info = wikipedia.summary(person, 1)
            print(info)
            talk(info)     
        elif 'joke' in command:
           talk(pyjokes.get_joke())
        elif 'goodbye' in command or 'good bye' in command:
            break
        else:
            talk('Please say the command again.')


if __name__ == "__main__":
    run_nova()
