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
            print('listening...')   #Updated_By_Kalpak_Kanungo
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass #Updated_By_Kalpak_Kanungo


def send_email(subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    server.login('sender mail id', 'sender password')
    email = EmailMessage()
    email['From'] = 'sender mail id'
    email['To'] = receiver   #Updated_By_Kalpak_Kanungo
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
    receiver = email_list[name]
    print(receiver)                #Updated_By_Kalpak_Kanungo
    talk('What is the subject of your email?')
    subject = get_info()
    talk('Tell me the text in your email')
    message = get_info()
    send_email(subject, message)
    
    #Newly_Updated_By_Kalpak_Kanungo
    #The User can send multiple email at the same time while the code is running as per their requirement if they say "YES"
    talk('Hey lazy boy. Your email is sent')
    talk('Do you want to send more email?')
    send_more = get_info()
    if 'yes' in send_more:
        get_email_info()

get_email_info()
