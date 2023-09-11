import datetime
from speak import Say
import pywhatkit
import os
import requests
import webbrowser
import Listen
import pyjokes

def Time():
    time = datetime.datetime.now().strftime('%I:%M %p')
    Say(time)

def Date():
    date = datetime.datetime().today()
    Say(date)

def NonInputExecution(query):
    query = str(query)

    if 'time' in query:
        Time()
    
    elif "date" in query:
        Date()

def InputExecution(tag,query):
    if "wikipedia" in tag:
        name = str(query).replace("", "")
        import wikipedia
        result = wikipedia.summary(name,1)
        Say(result)

    elif 'search' in tag:
        query = str(query).replace('search','')
        pywhatkit.search(query)
    elif 'notepad' in tag:
        os.startfile("C:\\Program Files\\Notepad++\\notepad++.exe")
    elif 'cnotepad' in tag:
        os.system("taskkill /f /im notepad++.exe")

    elif 'commandprompt' in tag:
        os.system("start cmd")
    
    elif 'word' in tag:
        os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE")

    elif 'powerpoint' in tag:
        os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE")

    elif 'excel' in tag:
        os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE")

    elif 'brave' in tag:
        os.startfile("C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe")

    elif 'cword' in tag:
        os.system("taskkill /f /im WINWORD.EXE")

    elif 'cpowerpoint' in tag:
        os.system("taskkill /f /im POWERPNT.EXE")

    elif 'cexcel' in tag:
        os.system("taskkill /f /im EXCEL.EXE")
    
    elif 'cbrave' in tag:
         os.system("taskkill /f /im brave.exe")

    elif 'news' in tag:
        Say('give me some time to fetch the top headlines..')
        news_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=637e2a5217e4400999a749d3c304b074'
        main_page = requests.get(news_url).json()
        articles = main_page["articles"]
        head = []
        day=["first","second","third","fourth","fifth"]
        for ar in articles:
            head.append(ar["title"])
        for i in range(len(day)):
            Say(f'todays {day[i]} news is:{head[i]}')

    elif 'play' in tag:
        song = str(query).replace('play', '')
        Say(f"playing {song}")
        pywhatkit.playonyt(song)
    
    elif 'open youtube' in tag:
        Say('opening youtube')
        webbrowser.open('www.youtube.com')

    elif 'open google' in tag:
        Say('What should I Search?')
        search  = str(query).replace('', "")
        webbrowser.open(f'{search}')

    elif 'joke' in tag:
        Say(pyjokes.get_joke())