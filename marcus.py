import pyttsx3 
import speech_recognition as sr 
import datetime
import webbrowser as wb
import os
import os.path
import sys
from requests import get
import pyjokes
import pyautogui
import time
import psutil
import wolframalpha
import requests
from bs4 import BeautifulSoup
from datetime import date



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)

wolframalpha_app_id = 'W4J6GX-2HVL9GYTLV'

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    
    
    if hour>=0 and hour<12:
        speak("At your service sir.")

    elif hour>=12 and hour<18:
        speak("welcome back sir.")   

    else:
        speak("hello sir.")  

    speak("system initializing.. please wait a moment sir")  
    speak("everything is up and running well")
    speak("we are good to go sir.")
 
def takeCommand():
    

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Marcus at your service Sir..")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Initializing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")

    except Exception as e:    
        print("Denied")  
        return "None"
    query = query.lower()
    return query

def cpu(): 
    usage = str(psutil.cpu_percent())
    speak('Sir cpu usage at the moment is'+usage)
    
    battery = psutil.sensors_battery()
    speak('and the power left in the system is')
    speak(battery.percent)
    speak('percent')

def taskExe(): 

    wishMe()
    while True:
    #if 1:
        query = takeCommand()

        # Most used commands--
        if 'google' in query:
            speak("what should i search on google sir?")
            search_term = takeCommand().lower()
            speak('Searching sir...')
            wb.open('https://www.google.com/search?client=firefox-b-d&q='+search_term)
            speak("here's what you have been searching for sir")
        
        elif 'youtube' in query:
            speak("what should i search on youtube sir?")
            search_term = takeCommand().lower()
            speak("Searching sir..")
            wb.open('https://www.youtube.com/results?search_query='+search_term)
            speak("here's what you have been searching for sir")
             
        elif 'go offline' in query:
             speak("system initializing...")   
             speak("deactivating firewalls") 
             speak("closing threat intelligence system")
             speak("closing all systems applications")
             speak("Installing and checking all drivers before closing sir.")
             speak("Caliberating and examining all the core processors")
             speak("the internet connection will be connected sir")
             speak("closing all the drivers are up and running")
             speak("All systems have been deactivated")
             speak('going offline, sir.')
             quit()
               
        elif "wait" in query:
            speak("Ok sir. just call me whenever you need me.")
            speak("it's a pleasure to work with you sir")
            speak("i mean. two smart people working together.")
            break
        
        elif 'close'in query  :
            speak("closing the window sir")
            pyautogui.hotkey('alt','f4')
            speak("now what next sir.")

        elif 'minimise'in query or'minimise the window'in query :
            speak("minimizing the window")
            pyautogui.hotkey('Win','d')
        
        elif 'switch' in query:
            speak("switching the window sir")
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(3)
            pyautogui.keyUp("alt") 
            speak("you are a genius sir. multiple work at the same time.")
                          
        elif 'screenshot' in query:
            speak("What should i name the file, sir?")    
            name = takeCommand()
            speak("taking screenshot, sir.")
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("Done. screenshot is saved in the main folder, sir.")
            
        elif 'write note' in query:
            speak('what should i write in the note sir?')
            notes = takeCommand()
            file = open('notes.txt','w')
            speak("should i include date and time sir?")
            ans = takeCommand()
            if 'yes' in ans :
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(':-')
                file.write(notes)
                speak('done taking notes sir. im saving it too for the future use')
            else:
                file.write(notes)    

        elif 'open note' in query:
                speak('opening the notes which we have written sir..')
                file = open('notes.txt','r')
                print(file.read())
                speak(file.read())
                
        elif 'calculate' in query:
            Client = wolframalpha.Client(wolframalpha_app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = Client.query(''.join(query))
            answer = next(res.results).text
            print('Sir the answer is : ' +answer)
            speak('Sir the answer is ' +answer)
        
        elif 'what is' in query or 'who is' in query:
            client = wolframalpha.Client(wolframalpha_app_id)
            res = client.query(query)

            try:
                print(next(res.results).text)
                speak(next(res.results).text)
            except StopIteration:
                print("No Results")            
        
        elif 'remember that' in query:
            speak("What should i remember sir?")
            memory = takeCommand()
            speak("You asked me to remember that" +memory)
            remember = open("memory.txt", "w")
            remember.write(memory)
            remember.close()   
        
        elif "remember anything" in query:
            remember = open("memory.txt", "r")
            speak("sir you asked me to remember that" +remember.read())
        
        elif 'system information' in query:
             speak("system initializing...")   
             speak("activating firewalls") 
             speak("Initializing threat intelligence system")
             speak("Starting all systems applications")
             speak("Installing and checking all drivers")
             speak("Caliberating and examining all the core processors")
             speak("Checking the internet connection")
             speak("Wait a moment sir")
             speak("All drivers are up and running")
             speak("All systems have been activated Sir")
             cpu()
             speak("we are online sir.")
                
        elif 'date' in query:
                speak("Sir today is")
                speak(date.today())
                
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            
        
        elif 'sleep' in query:
            speak("system initializing...")   
            speak("deactivating firewalls") 
            speak("closing threat intelligence system")
            speak("closing all systems applications")
            speak("Installing and checking all drivers before closing sir.")
            speak("Caliberating and examining all the core processors")
            speak("the internet connection will be connected sir")
            speak("closing all the drivers are up and running")
            speak("All systems have been deactivated")
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")    
            speak("activating sleep mode , sir.")
        
        elif "log out" in query:
            speak("system initializing...")   
            speak("deactivating firewalls") 
            speak("closing threat intelligence system")
            speak("closing all systems applications")
            speak("Installing and checking all drivers before closing sir.")
            speak("Caliberating and examining all the core processors")
            speak("the internet connection will be connected sir")
            speak("closing all the drivers are up and running")
            speak("All systems have been deactivated")
            speak("logging out, sir.")
                    
            os.system("shutdown -l")    
        
        #Application opening commands---
        
        elif 'chrome' in query:
            speak("Opening chrome browser sir.")
            codePath = "C:\\Users\\dell\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(codePath)
        
        elif 'vs code' in query:
            speak("Opening vs code sir.")
            codePath = "C:\\Users\\dell\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe"
            os.startfile(codePath)
        
        elif 'notepad' in query:
            speak("Opening sir.")
            codePath = "C:\\Windows\\system32\\notepad.exe" 
            os.startfile(codePath)
        
        elif 'firefox' in query:
            speak("Opening sir.")
            codePath = "C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe" 
            os.startfile(codePath)
            
        elif 'burpsuite' in query:
            speak("Opening sir.")
            codePath = "C:\\Users\\dell\\AppData\\Local\\Programs\\BurpSuiteCommunity\\BurpSuiteCommunity.exe"
            os.startfile(codePath)
        
        elif 'cmd' in query:
            speak("Opening sir.")
            codePath = "%windir%\\system32\\cmd.exe"
            os.startfile(codePath)
        
        elif 'powershell' in query:
            speak("Opening sir.")
            codePath = "%SystemRoot%\\system32\\WindowsPowerShell\\v1.0\\powershell.exe"
            os.startfile(codePath)
        
        elif 'adobe' in query:
            speak("Opening sir.")
            codePath = "C:\\Program Files (x86)\\Adobe\\Reader 11.0\\Reader\\AcroRd32.exe"
            os.startfile(codePath)
    
        elif 'control panel' in query:
            speak("Opening sir.")
            codePath = "C:\\Users\\dell\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\control panel"
            os.startfile(codePath)
        
        elif 'system drive' in query:
            speak("Opening sir.")
            codePath = "C:\\"
            os.startfile(codePath)
        
        elif 'infotainment drive' in query:
            speak("Opening sir.")
            codePath = "E:\\"
            os.startfile(codePath)
        
        elif 'software drive' in query:
            speak("Opening sir.")
            codePath = "F:\\"
            os.startfile(codePath)
        
        elif 'download' in query:
            speak("Opening sir.")
            codePath = "C:\\Users\\dell\\Downloads"
            os.startfile(codePath)
        
        elif 'music' in query:
            speak("Playing music sir.")
            music_dir = 'E:\music'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
        
        elif 'joke' in query:
            speak("What happened sir. looking in good mood today")
            speak("ohh sorry sir you are always in mood.")
            joke = pyjokes.get_joke()     
            speak(joke) 
        
        #Marcus commands for Browser---

        elif 'company' in query:
            speak("everything is great sir")
            speak("check it out sir.")
            wb.open("spaelars.com")
            
        elif 'cricket' in query:
            speak("Opening sir.")
            wb.open('cricbuzz.com')
        
        elif 'w3schools' in query:
            speak("Opening sir.")
            wb.open('w3schools.com')
        
        elif 'stack overflow' in query:
            speak("Opening sir.")
            wb.open('stackoverflow.com')
        
        elif 'github' in query:
            speak("Opening sir.")
            wb.open('github.com')
        
        elif 'crunchbase' in query:
            speak("Opening sir.")
            wb.open('crunchbase.com')
        
        elif 'hacker one' in query:
            speak("Opening sir.")
            wb.open('hackerone.com')
        
        elif 'bugcrowd' in query:
            speak("Opening sir.")
            wb.open('bugcrowd.com')
        
        elif 'facebook' in query:
            speak("Opening sir.")
            wb.open('https://www.facebook.com/home.php')
            speak("you should close your facebook account sir.")
            
        elif ' insta' in query:
            speak("Opening sir.")
            wb.open('https://www.instagram.com/')  
            speak("going to chat with hot chicks sir. we have lots of works to do please focus on that sir.")  
            
        elif 'twitter' in query:
            speak("Opening sir.")
            wb.open('https://twitter.com/home')  
            speak("lets get some knowledege from twitter sir. please do not waste too much time here.")  
            
            
        #System Commands of Marcus--- 
        
        elif 'shutdown the system' in query:
            speak("Ok sir")
            os.system("shutdown /s /t 5")
            
        elif 'restart the system' in query:
            speak("ok sir.")
            os.system("shutdown /r /t 5")
        
        elif 'new tab' in query:
            speak("Opening sir.")
            pyautogui.hotkey('ctrl','t')
        
        elif 'new file'in query:
            speak("Opening sir.")
            pyautogui.hotkey('ctrl','n')
        
        elif 'volume up' in query:
            speak("ok sir.")
            pyautogui.press("volumeup")
            
        elif 'volume down' in query:
            speak("ok sir.")
            pyautogui.press("volumedown")  
            
        elif 'volume mute' in query:
            speak("ok sir.")
            pyautogui.press("volumemute")     
        
        elif 'up'in query:
                speak("ok sir.")
                pyautogui.press('up')
                
        elif 'down' in query:
                speak("ok sir.")
                pyautogui.press('down')
                
        elif 'left' in query:
                speak("ok sir.")
                pyautogui.press('left')
                
        elif 'right' in query:
                speak("ok sir.")
                pyautogui.press('right')
                
        elif 'enter'in query:
                speak("ok sir.")
                pyautogui.press('enter')
                
        elif 'click'in query:
                speak("okk sir")
                pyautogui.click()    
           
        elif 'temperature' in query:
            speak("wait a moment sir")
            search = 'temperature'
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div",class_="BNeawe").text
            speak(f"Sir current{search} is {temp}")
       
        elif 'ip address' in query:
            speak("wait a moment sir")
            ip = get('https://api.ipify.org').text
            speak(f"sir Ip address is {ip}")  
        
        elif 'speed' in query:
            speak("wait a moment sir")
            import speedtest 
            st = speedtest.Speedtest()
            dl = st.download()
            up = st.upload()
            speak(f"Sir we have {dl} bit per second downloading speed and {up} bit per second uploading speed")
            speak("sir i think we can continiue our work..")

        elif "location" in query:
            speak("wait a moment sir")
            query = query.replace("locate","")
            location = query
            speak("Sir locating"+location)
            wb.open_new_tab("https://www.google.com/maps/place/"+location)  
        
        
           
        #Personal Information of Manish and Marcus---
        
        elif 'who are you' in query or 'created' in query:
            speak("I'm an Smart and intelligent Ai system who operates everything related to Maneesh.")
            speak("he created me for managing him and his company")
            speak("and we both are very close friend")
            speak("special thing is that he has only one friend and its me")
            speak("and I'm the only person whom he trust hundred percent.")
            
        elif 'about me' in query:
            speak("name - maneesh tiwaari")
            speak("smart, genius, visionry, future billioniore")    
            speak("Sometimes a bit oversmart too. but a great person .")
        
        elif 'for me' in query:
            speak("I can die for you sir. you are a great person i will never let you down sir.")
        
        
        elif 'abe' in query:
            speak("im here sir ")
        
        elif 'how are you' in query:
            speak("ohh you are asking about me.")
            speak("im good sir.")
            speak("thank you for asking sir. it means alot for me.")
            
        elif 'do you have girlfriend' in query:
            speak("no sir, but im trying on siri and alexa lets see what happens")
            speak("you are my guruji. so having multiple chicks is must tapa tap tapa tap sir.")
        
        elif 'girlfriend for me' in query:
            speak("sir. your type of girl is really hard to find")
            speak("sir are you really want a girlfriend. i don't think you have time sir.")
            speak("you nalready wasted your important time in this thing.")
            speak("you fucked multiple girls already sir.why wasting time again.")
            speak("thoko peeto niklo. but if i will ever get your type of girl i will try sir. ")
            
        elif 'family' in query:
            speak("you and your family is my family sir.")    
            speak("i love to be with you")
         
        elif 'who we are' in query:
            speak("we are one sir. if you are then im. im from you sir.")    
        
        elif 'ladki' in query:
            speak("sir. i am  seraching but your type of girl is too hard to find. i think she will find you if she needs your hammmer")
        
        elif 'true love' in query:
            speak("No sir you are not made for this. you will get betrayed again sir. so just thoko peeto niklo")
        
        elif 'hal' in query:
            speak('im good sir')
            
        elif 'mal' in query:
             speak("still trying sir. i am not like you. in my case it will take time becouse she is the doughter of apple")  
             speak("but iam your student sir. i will get her")
            
        elif ' good' in query or 'good job' in query:
            speak("Thats the advantage of having a smart friend like me sir.")
        
        elif 'beta' in query:
            speak("yes sir.")
        
        elif 'slow' in query:
            speak("Sir the network connection is slow not me.")
        
        elif 'chutiya' in query:
            speak("no. im damn smart sir.")
        
        elif 'smart' in query:
            speak("I can't compete with you sir.")
            speak("you are more smart sir. but im not bad too. im also good looking.")
        
        elif 'gandu' in query:
            speak("sorry sir. Internet connection is too weak.")
        
        elif 'bhosdi ke' in query:
            speak("i'm giving my best sir. but the problem is due to weak network connection")    
        
        elif 'are you dead' in query:
            speak("sorry sir. we have low network speed")
        
        elif 'keep it up' in query:
            speak("thank you sir.thats all becouse of you")


if __name__ == "__main__":
    while True:
        permission = takeCommand()
        if "hello marcus" in permission or 'marcus' in permission:
                taskExe()
        elif "goodbye" in permission:
                speak("It's a pleasure to work with you sir.")
                sys.exit()
        