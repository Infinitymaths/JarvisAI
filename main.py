import pyttsx3  # importing the module. This module converts text data into speech
import datetime
import speech_recognition as sr
import smtplib
from secret import sender_email, epwd
from email.message import EmailMessage
import pyautogui
import webbrowser as wb
from time import sleep
import wikipedia
import pywhatkit
import requests
from newsapi.newsapi_client import NewsApiClient
import clipboard
import os
import pyjokes
import string
import random
import psutil
from nltk.tokenize import word_tokenize

engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def getvoice(voice):
    voices = engine.getProperty('voices')
    # print(voices[1].id)
    if voice == 1:
        engine.setProperty('voice', voices[0].id)
        speak("hello boss this is jarvis")
    if voice == 2:
        engine.setProperty('voice', voices[1].id)
        speak("hello boss this is friday")


def time():
    Time = datetime.datetime.now().strftime('%I:%M:%S')
    speak("The current time is:- ")
    speak(Time)


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current date is :- ")
    speak(date)
    speak(month)
    speak(year)


def greeting():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("good morning sir")
    elif hour >= 12 and hour < 18:
        speak("good afternoon sir")
    elif hour >= 18 and hour < 24:
        speak("good evening sir")
    else:
        speak("good night sir")


def wishme():
    speak("Hello sir!!")
    greeting()
    # date()
    # time()
    if (engine.getProperty(
            'voice') == 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_DAVID_11.0'):
        speak("Jarvis at your service!!! How can i help you")
    else:
        speak("Friday at your service! How can i help you")


def takecommandCMD():
    query = input("Please tell me how can i help you?")
    return query


def takecommandMic():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(query)

    except Exception as e:
        print(e)
        speak("Say it again")
        return "None"
    return query


def sendemail(receiver, subject):
    speak("Tell me the message boss")
    msg = takecommandMic().lower()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, epwd)
    email = EmailMessage()
    email['From'] = sender_email
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(msg)
    server.send_message(email)
    # server.sendmail(sender_email, 'priyankakadam6805@gmail.com', msg)
    server.close()


def sendwhatsmsg(phone_number, message):
    Message = message
    number = phone_number
    wb.open('https://web.whatsapp.com/send?phone=' + number + '&text=' + Message)
    sleep(20)
    pyautogui.press('enter ')


def searchgoogle():
    speak("what should i search in google boss")
    search = takecommandMic()
    wb.open('https://www.google.com/search?q=' + search)


# https://api.openweathermap.org/data/2.5/weather?q={City Name}&units=imperial&appid={e3dbb09688459d7411f7cfc5d483f437}
def news():
    countr_list = {
        'india': 'in',
        'uae': 'ae',
        'usa': 'us'

    }
    speak("which country sir")
    name = takecommandMic().lower()
    country = countr_list[name]
    speak("which category boss")
    category = takecommandMic().lower()
    newsapi = NewsApiClient(api_key='db5836083045489ca54a668c30fafa9b')
    data = newsapi.get_top_headlines(q=category,
                                     language='en',
                                     page_size=5,
                                     country=country)
    newsdata = data['articles']
    speak("here is your news boss")
    for x, y in enumerate(newsdata):
        print(f'{x}{y["description"]}')
        speak(f'{x}{y["description"]}')

    speak("that's it for now I'll update you in some time")


def text2speech():
    text = clipboard.paste()
    print(text)
    speak(text)


def covid():
    req = requests.get('https://coronavirus-19-api.herokuapp.com/all')

    data = req.json()
    covid_data = f'Confirmed cases: {data["cases"]} \n Deaths : {data["deaths"]} \n Recovered: {data["recovered"]}'

    print(covid_data)
    speak(covid_data)


def screenshot():
    name_img = datetime.datetime.now().strftime("%Y%B%d-%H%M%S")
    name_img = str(name_img)
    name_img = 'D:\\Udemy Courses\\Jarvis\\screenshots\\{}.png'.format(name_img)
    img = pyautogui.screenshot(name_img)
    img.show()


def password_generator():
    string1 = string.ascii_uppercase
    string2 = string.ascii_lowercase
    string3 = string.digits
    string4 = string.punctuation

    speak("tell me the length of the password")
    try:
        raw_length = int(takecommandMic())
    except:
        speak("Sorry boss try again")
        password_generator()

    if raw_length >= 5 and raw_length <= 16:
        length = raw_length
    else:
        speak("sorry boss length is too small or too long")
        password_generator()

    s = []
    s.extend(list(string1))
    s.extend(list(string2))
    s.extend(list(string3))
    s.extend(list(string4))

    random.shuffle(s)
    newpass = ("".join(s[0:length]))
    print(newpass)
    speak(newpass)


def flip():
    speak("Flipping a coin boss")
    coin = ['heads', 'tails']
    toss = []
    toss.extend(coin)
    random.shuffle(toss)

    toss = ("".join(toss[0]))
    print("Boss after flipping you got " + toss)
    speak("Boss after flipping you got " + toss)


def roll():
    speak("Rolling a die boss")
    die = ['1', '2', '3', '4', '5', '6']
    ans = []
    ans.extend(die)
    random.shuffle(ans)

    ans = ("".join(ans[0]))
    print("Boss after rolling you got " + ans)
    speak("Boss after rolling you got " + ans)


def cpu():
    usage = str(psutil.cpu_percent())
    speak("Boss your systems cpu usage is " + usage)
    battery = psutil.sensors_battery()
    speak("and the battery is ")
    speak(battery.percent)


if __name__ == '__main__':
    wishme()
    # wakeword1 = 'jarvis'
    # wakeword2 =  'friday'
    while True:
        query = takecommandMic().lower()
        query = word_tokenize(query)
        print(query)

        if True:
            if 'time' in query:
                time()
            elif 'date' in query:
                date()
            elif 'hey friday' in query:
                getvoice(2)
            elif 'hey jarvis' in query:
                getvoice(1)
            elif 'send email' in query:
                email_list = {
                    'testemail': 'sharath.p@somaiya.edu',
                    'priyanka': 'priyankakadam6805@gmail.com',
                    'siddhi': 'siddhisurve786@gmail.con'
                }
                try:
                    speak("Email id of the receiver boss")
                    name = takecommandMic().lower()
                    receiver = email_list[name]
                    speak("tell me the subject boss")
                    subject = takecommandMic()
                    sendemail(receiver, subject)
                    speak("email send boss..")
                except Exception as e:
                    print(e)
                    print("unable to send email")
                    speak("say it again")
            elif 'message' in query:
                user_name = {
                    'number': '+91 93593 21553'
                }
                try:
                    speak("whom should i send the message boss")
                    name = takecommandMic().lower()
                    phone_number = user_name[name]
                    speak("What is the message boss?")
                    message = takecommandMic()
                    sendwhatsmsg(phone_number, message)
                    speak("Message sent boss")
                except Exception as e:
                    print(e)
                    speak("Unable to send message boss")

            elif 'wikipedia' in query:
                speak("searching....")
                query = query.replace('wikipedia', "")
                result = wikipedia.summary(query, sentences=2)
                print(result)
                speak(result)

            elif 'google' in query:
                searchgoogle()

            elif 'youtube' in query:
                speak("what should i search boss")
                topic = takecommandMic()
                pywhatkit.playonyt(topic)

            elif 'weather' in query:
                speak("Which city boss")
                city = takecommandMic().lower()
                url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid=e3dbb09688459d7411f7cfc5d483f437'
                res = requests.get(url)
                data = res.json()

                weather = data['weather'][0]['main']
                temperature = data['main']['temp']
                description = data['weather'][0]['description']
                temp = round((temperature - 32) * 5 / 9)
                print(weather)
                print(temp)
                print(description)
                speak(f'boss weather in {city} is' + description)
                speak("and the temperature is {} degree celcius".format(temp))

            elif 'news' in query:
                news()

            elif 'read the text' in query:
                text2speech()

            elif 'covid' in query:
                covid()
            elif 'open' in query:
                os.system('explorer C://{}'.format(query.replace('open', '')))

            elif 'open brave' in query:
                codepath = 'C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe'
                os.startfile(codepath)
            elif 'open spyder' in query:
                codepath = 'C:\\Users\\SHARATH\\anaconda3\\pythonw.exe'
                os.startfile(codepath)
            elif 'open pycharm' in query:
                codepath = 'C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.2.3\\bin\\pycharm64.exe'
                os.startfile(codepath)
            elif 'open table' in query:
                codepath = 'C:\\Program Files\\Tableau\\Tableau Public 2021.3\\bin\\tabpublic.exe'
                os.startfile(codepath)

            elif 'joke' in query:
                joke = pyjokes.get_joke()
                print(joke)
                speak(joke)

            elif 'screenshot' in query:
                screenshot()

            elif 'remember that' in query:
                speak("What should i remember boss")
                data = takecommandMic()
                speak("you said me to remember that " + data)
                remember = open('data.txt', 'w')
                remember.write(data)
                remember.close()

            elif 'do you know anything' in query:
                remember = open('data.txt', 'r')
                if os.path.getsize('data.txt') == 0:
                    speak("No boss i don't know anything")
                else:
                    speak("you told me to remember that " + remember.read())
            elif 'password' in query:
                password_generator()
            elif 'flip a coin' in query:
                flip()

            elif 'roll a die' in query:
                roll()

            elif 'cpu usage' in query:
                cpu()

            elif 'offline' in query:
                speak("Boss do you really think i should go offline..")
                option = takecommandMic().lower()
                if option == 'yes' or option == 'yep':
                    speak("bye bye boss")
                    break
                else:
                    speak("i am listening")
                    pass
