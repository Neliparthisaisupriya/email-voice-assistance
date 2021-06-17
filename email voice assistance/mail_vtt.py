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
            print('listening....')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()

    except:
        pass

def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('neliparthisaisupriya@gmail.com','supriya 123')
    email = EmailMessage()
    email['from'] = 'neliparthisaisupriya@gmail.com'
    email['to'] = receiver
    email['subject'] = subject
    email.set_content(message)
    server.send_message(email)
    talk('Hey lazy. Your email is sent')
    talk('Do you want to send more email')
    send_more = get_info()
    if 'yes' in send_more:
        get_email_info()


email_list = {
    'naveen': 'naveenn610@gmail.com',
    'supriya': 'narayanasupriya041@gmail.com',
    'pandu': 'pvakiri@gmail.com',
    'jaidev':'jaidevrj1723@gmail.com'

}


def get_email_info():
    talk('to whom you want to send the email')
    name = get_info()
    receiver = email_list[name]
    print(receiver)
    talk('what is the subject of your email?')
    subject = get_info()
    talk('tell me the text in your email')
    message = get_info()

    send_email(receiver, subject, message)

get_email_info()





