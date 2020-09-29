import calendar
import pyttsx3
import speech_recognition as sr
import datetime
import subprocess
import webbrowser


r=sr.Recognizer()

def take_input():
     with sr.Microphone() as source:
        print("start saying...")
        audio=r.listen(source)
        pyttsx3.speak("ok please wait...")
        p=r.recognize_google(audio)
        print(p)
        return p

pyttsx3.speak("how can i help you")
p=take_input()
if "exit" in p or "quit" in p or "close" in p or "don't" in p:
        pyttsx3.speak("ok")
elif "httpd" in p and "status" in p:
        webbrowser.open("http://192.168.43.137/cgi-bin/httpdstatus.py")
elif "OS" in p and "docker" in p and "running" in p:
        webbrowser.open("http://192.168.43.137/cgi-bin/osstatus.py")
elif "docker" in p and "stop" in p:
        webbrowser.open("http://192.168.43.137/osstop.html")
elif "docker" in p and "status" in p:
        webbrowser.open("http://192.168.43.137/cgi-bin/dockerstatus.py")
elif "docker" in p and ("run" in p or "start" in p):
        webbrowser.open("http://192.168.43.137/cgi-bin/dockerrun.py")
elif "Linux commands" in p or "Linux command" in p:
        webbrowser.open("http://192.168.43.137/command.html")
elif ("OS" in p ) and ("run" in p or "launch" in p):
        webbrowser.open("http://192.168.43.137/osrun.html")
elif "OS" in p and "stop" in p:
        webbrowser.open("http://192.168.43.137/cgi-bin/osstop.py")
elif ("Notepad" in p or "editor" in p) and ("open" in p or  "launch" in p):
        subprocess.Popen("C:\\Windows\\System32\\notepad.exe")
elif ("Player" in p or "vlc" in p) and ("open" in p or  "launch" in p):
        subprocess.Popen("C:\\Program Files\\VideoLAN\\VLC\\vlc.exe")
elif ("Paint" in p or "mspaint" in p or "draw" in p) and ("open" in p or  "launch" in p):
        subprocess.Popen("C:\\Windows\\system32\\mspaint.exe")
elif ("calc" in p or "calculator" in p ) and ("open" in p or "launch" in p):
        subprocess.Popen("C:\\Windows\\System32\\calc.exe")
elif ("control panel" in p ) and ("open" in p or "launch" in p):
        subprocess.Popen("C:\\Windows\\System32\\control.exe")
elif ("task manager" in p or "taskmgr" in p) and ("open" in p or "launch" in p):
        subprocess.Popen("C:\\Windows\\System32\\Taskmgr.exe")
elif ("Chrome" in p or "chrome browser" in p) and ("run" in p or "open" in p or  "launch" in p):
        subprocess.Popen("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
elif("msedge" in p or "microsoft edge" in p or "browser" in p or "ms edge" in p) and ("run" in p or "open" in p or  "launch" in p):
        subprocess.Popen("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")
elif ("WhatsApp" in p ) and ("open" in p or "run" in p or "launch" in p):
        subprocess.Popen("C:\\Users\\Narayan singh\\Downloads\\WhatsAppSetup.exe")
elif ("Word" in p ) and ("open" in p or "run" in p or "launch" in p):
        subprocess.Popen("C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE")
elif ("PowerPoint" in p or "power point in p" in p ) and ("open" in p or "run" in p or "launch" in p):
        subprocess.Popen("C:\\Program Files\Microsoft Office\\root\\Office16\\POWERPNT.EXE")
elif ("Excel" in p ) and ("open" in p or "run" in p or "launch" in p):
        subprocess.Popen("C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE")
elif "calendar" in p :
        year = int(input("Please Enter year: "))
        print(calendar.calendar(year,w=2,l=1,c=6))
elif "date"  in p:
        today=datetime.date.today()
        d1=today.strftime("%d-%m-%y")
        print(d1)
elif("time" in p):
        time=datetime.datetime.now()
        t=time.strftime("%I:%M:%S")
        print(t)
elif "google" in p and ("drive" in p )and ("open" in p or "launch" in p ):
        webbrowser.open('https://drive.google.com/drive/')
elif "Google" in p and ("open" in p or "run" in p or "search" in p):
        pyttsx3.speak("please speak your search")
        search=take_input()
        webbrowser.open('https://www.google.com/search?&q='+search)
elif "YouTube" in p and  ("open" in p or "play" in p or "run" in p or "watch"in p or "search" in p):
        pyttsx3.speak("please speak what you want to the search in youtube")
        search=take_input()
        webbrowser.open('https://www.youtube.com/results?search_query='+search)
elif "song" in p and ("play" in p or "listen" in p):
        pyttsx3.speak("please tell me name of the song")
        search=take_input()
        webbrowser.open('https://gaana.com/search/'+search)
elif "Wikipedia" in p and ("search" in p or "open" in p):
        pyttsx3.speak("please speak wikipedia  search")
        search=take_input()
        webbrowser.open('https://en.wikipedia.org/wiki/Special:Search?search='+search)
elif "Gmail" in p and  ( "open" in p or "launch" in p or "run in p"):
        webbrowser.open('https://mail.google.com/mail/u/0/#inbox')
elif "Office" in p and ("open" in p or "launch" in p or "run in p"):
        webbrowser.open('https://www.office.com/?auth=1')
else:
       pyttsx3.speak("sorry ! don't support")

