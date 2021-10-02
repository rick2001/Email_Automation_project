import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def get_info():
    try:
        with sr.Microphone() as source:
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        continue


def send_email(subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    server.login('Sender Mail Id', 'password')
    email = EmailMessage()
    email['From'] = 'Sender mail Id'
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)


email_list = {
    'mono': 'monojitpt2341@gmail.com',
    'rick': 'surojitghosh561@gmail.com',
    'kalpak': 'kanungokalpak@gmail.com',
    'digbijoy': 'optimusprime@gamil.com'
}


def get_email_info():
    talk('To Whom you want to send email')
    name = get_info()
    talk('What is the subject of your email?')
    subject = get_info()
    talk('Tell me the text in your email')
    message = get_info()
    send_email(subject, message)
   


get_email_info()
