#premade modules
import webbrowser#pip install webbrowser
import os
import wikipedia #pip install wikipedia
import pyautogui#pip install pyautogui
import keyboard
import site
import pathlib
from googlesearch import search
import time 
import os.path
import datetime
from dotenv import load_dotenv
import threading
#file modules
from speak import speak
from take_command import takeCommand
from wish_me import wishMe
from askgpt import askGPT
from email_send import email
from music import music
import asyncio

load_dotenv()

EMAIL = os.getenv('EMAIL')
PERSON1 = os.getenv('PERSON1')
PERSON2 = os.getenv('PERSON2')
Teacher = os.getenv('Teacher')

def main():
    if __name__ == "__main__":
        #wishMe()
        while True:
        # if 1:
            global query
            query = takeCommand().lower()
            if 'jarvis' in query:

                query = query.replace('jarvis', '')
                # Logic for executing tasks based on query
                if 'search wikipedia for' in query:
                    speak('Searching Wikipedia...')
                    query = query.replace("wikipedia", "")
                    try:
                        results = wikipedia.summary(query, sentences=2)
                        speak("According to wikipedia")
                        print(results)
                        speak(results)
                    except Exception as e:
                        print('sorry no such results found')
                        speak('sorry no such results found')
                elif 'pause' in query:
                    speak('Paused')
                    os.system("pause")
                elif 'quit' in query:
                    speak('Quitting')
                    os._exit(0) 
                elif 'ask gpt ' in query or 'asked gpt' in query:
                        query = query.replace('ask gpt ', "")
                        askGPT(query)
                        print('\n')
                elif 'open ' in query :
                    query = query.replace('open ','').strip().lower()
                    print(query)
                    if query == 'youtube':
                        webbrowser.open_new_tab("http://www.youtube.com")
                    elif query == 'google':
                        webbrowser.open_new_tab("http://www.google.com")
                    elif query == 'terraria':
                        terrariaPath = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Terraria.exe"
                        os.startfile(terrariaPath)
                    elif query == 'discord':
                        discordPath = "C:\\Users\\divya\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Discord Inc\\Discord.lnk" 
                        os.startfile(discordPath)
                    elif query == 'steam':
                        steamPath = 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Steam\\Steam.lnk'
                        os.startfile(steamPath)
                    elif query == 'bluestacks':
                        bluestacksPath = 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\BlueStacks5.lnk'
                        os.startfile(bluestacksPath)
                        time.sleep(2)
                        keyboard.press('Enter')
                    elif query == 'epicgames':
                        epicgamesPath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Epic Games Launcher.lnk"
                        os.startfile(epicgamesPath)
                    elif query == 'chess':
                        webbrowser.open_new_tab('http://www.chess.com')
                    elif query == 'vs code':
                        codePath = "C:\\Users\\divya\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk"
                        os.startfile(codePath)
                    elif query == 'obs':
                        codePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Streamlabs Desktop.lnk"
                        os.startfile(codePath)
                    else:
                        webbrowser.open_new_tab(query)
                elif 'wish me' in query:
                    wishMe()    
                elif 'time' in query:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                    speak(f"Sir, the time is {strTime}")
                elif 'play music' in query:
                    music("C:\\Users\\divya\\Music\\Music")
                elif 'quit current app' in query or 'close app' in query:
                    pyautogui.hotkey('alt','f4')
                elif 'type' in query: #in progress
                    speak('Typing...')
                    speak("What should I Type?")
                    command = takeCommand()
                    print(command)
                    keyboard.write(command,delay=0.35)
                    if 'enter' or "Enter" in command:
                        keyboard.press('Enter')
                    if "backspace" or "Backspace" in command:
                        keyboard.press('Backspace') 
                elif 'shutdown' in query or "shut down" in query:
                    speak("are you sure sir? this command will shutdown the entire system.")
                    command = takeCommand()
                    if 'yes' in command:
                        speak("Please give me the shutdown password")
                        command = takeCommand().lower()
                        if 'jarvis' in command:
                            os.system("shutdown /s /t 1")
                    else:
                        speak("Command aborted")
                elif 'restart' in query:
                    speak("Are you sure sir? This command will restart this system.")
                    command = takeCommand()
                    if 'yes' in command:
                        os.system("shutdown /r /t 1")
                    else:
                        speak("Command aborted")
                elif 'log out' in query or 'logout' in query:
                    speak("Are you sure sir? This command will log you out of the system")
                    command = takeCommand()
                    if 'yes' in command:
                        os.system("shutdown /l")
                    else:
                        speak("Command aborted")
                elif 'email to mom' in query:
                    email(PERSON1)   
                elif 'email to dad' in query:
                    email(PERSON2)
                elif 'email to myself' in query:
                    email(EMAIL)
                elif 'email to S' in query:
                    email(Teacher)
                else:
                    askGPT(query)
                    print('\n')
main()