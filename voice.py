import speech_recognition as sr
import easyimap as e
import pyttsx3
import smtplib



unm = "************@gmail.com"    # Login credentials of our email id
pwd = "**********"
r = sr.Recognizer()

engine = pyttsx3.init()  # Defining an engine for text to speech
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)


def speak(str):
    print(str)
    engine.say(str)
    engine.runAndWait()


def listen():  # function for speech for text
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        str = "Speak Now:"
        speak(str)
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            return text
        except:
            str = "Sorry could not recognize what you said"
            speak(str)


def sendmail():

    rec = "*************@gmail.com"

    str = "please speak the body of your email"
    speak(str)
    msg = listen()

    str = "you have spoken ths message"
    speak(str)
    speak(msg)

    server = smtplib.SMTP_SSL("smtp.gmail.com",465)
    server.login(unm, pwd)
    server.sendmail(unm, rec, msg)
    server.quit()

    str = "The email has been Sent"
    speak(str)


def readmail():
    server = e.connect("imap.gmail.com",unm,pwd)
    server.listids()

    str = "please say the Serial Number of the email you wanna read starting for latest"
    speak(str)

    a = listen()
    if (a == "Two"):
        a = "2"

    b = int(a) - 1

    email = server.mail(server.listids()[b])

    str = "The email is form:"
    speak(str)
    speak(email.from_addr)
    str = "The subject of the email is:"
    speak(str)
    speak(email.title)
    str = "The body of email is :"
    speak(str)
    speak(email.boby)


str = "Welcom to voice controlled email service"
speak(str)


while (1):

    str = "What do you want to do?"
    speak(str)

    str = "Speak SEND to send email   speak READ to Read Inbox   Speak EXIT to Exit"
    speak(str)

    ch = listen()

    if (ch == 'send'):
        str = "you have chosen to send an email"
        speak(str)
        sendmail()

    elif (ch == 'read'):
        str = "you have chosen to read email"
        speak(str)
        readmail()

    elif (ch == 'exit'):
        str = "you have chosen to exit, bye bye"
        speak(str)
        exit(1)

    else:
        str = "Invalid choice, you said:"
        speak(str)
        speak(ch)