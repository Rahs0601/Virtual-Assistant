import datetime
import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1
].id)


def intro():
    talk('Heya...!, this is Rah\'s virtual assistant')
    talk('built to work as an AI')
    talk('How can I help you')
    return 0


def talk(text):
    engine.say(text)
    engine.runAndWait()
    return 0


def reco():
    try:
        res = ''
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            res = listener.recognize_google(voice)
            res = res.lower()
            print(res)
    except:
        talk('error')
    return res


def action():
    command = reco()
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time1 = datetime.datetime.now().strftime('%I %M %p')
        print(time1)
        talk('Currently in india its' + time1)
    
    elif 'wikipedia' in command:
        person = command.replace('wikipedia', '')
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)
    else:
        google = command.replace('search', '')
        pywhatkit.search(google)
        talk('I found this on google')
    return 0

if __name__ == '__main__':
    intro()
    action()
    talk('thank you')