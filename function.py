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

def increase_volume(percent=10):
    """Increase the volume by the specified percentage"""
    current_volume = stream.get_volume()
    new_volume = min(1.0, current_volume + (percent / 100))
    stream.set_volume(new_volume)

def decrease_volume(percent=10):
    """Decrease the volume by the specified percentage"""
    current_volume = stream.get_volume()
    new_volume = max(0.0, current_volume - (percent / 100))
    stream.set_volume(new_volume)

def set_alarm(alarm_time, message):
    print(f"Alarm set for {alarm_time} - {message}")
    while True:
        now = datetime.datetime.now()
        if now.hour == alarm_time.hour and now.minute == alarm_time.minute:
            print(message)
            os.system("start alarm_sound.mp3")
            break

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
            topic = command.replace("What is", '')
            info = wikipedia.summary(topic, 1)
            print(info)
            talk(info)     
        elif 'joke' in command:
            jokes = pyjokes.get_joke()
            talk(jokes)
            print(jokes)
        elif 'goodbye' in command or 'good bye' in command:
            break
        elif "increase" in command and "volume" in command:
            percent = 10
            if "by" in command:
                percent = int(command.split("by")[1].split("%")[0])
            increase_volume(percent)
            print(f"Increased volume by {percent}%")
        elif "decrease" in command and "volume" in command:
            percent = 10
            if "by" in command:
                percent = int(command.split("by")[1].split("%")[0])
            decrease_volume(percent)
            print(f"Decreased volume by {percent}%")
        elif "alarm" in command or "remaind" in command or "notify" in command or "make a note" in command:
            alarm_time = int(time)
            message = command
            set_alarm(alarm_time, message)
        except sr.UnknownValueError:
            print("Sorry, I didn't understand that")
        else:
            talk('Please say the command again.')


if __name__ == "__main__":
    run_nova()
