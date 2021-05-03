import speech_recognition as sr
import pyttsx3
import pywhatkit
from googletrans import Translator
import subprocess
from color_printer import *
import datetime
import pyjokes_hebrew

from tkinter import *
import tkinter as tk

root = tk.Tk()
root.configure(background="#4285f4")
root.title('היי אביב')


#, command=openMashovAndClosPopUp

printComm = ""


numbers={
  "לאמא": "+972542323167",
  "לאלון": "+972 58-350-1228",
  "לאחי": "+972 58-477-0076",
  "לעידן": "+972 58-477-0076",
  "לאחותי": "+972 50-321-9900",
  "לליאור": "+972 50-321-9900",
}

def trans(text):
    return Translator().translate(text, dest="en").text



    #subprocess.Popen(["notepad.exe", "feedback"])

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty('rate', 160)
engine.setProperty("voice", voices[1].id)
#engine.setProperty('rate', voices[1].id, newVoiceRate)

def talk(text):
    engine.say(text)
    engine.runAndWait()

#talk("Aviv Hears you")
def hi_aviv():
    global printComm
    try:
        with sr.Microphone() as source:
            printGreen("listening... (:")
            voice = listener.listen(source)
            command = listener.recognize_google(voice, language="he")
            print(command)

    except:
        print("ops")
        hi_aviv()

    printComm = command
    return command


def run_aviv():
    command = hi_aviv()

    if "נגן" in command:
        song = command.replace("נגן", "")
        songEn = trans(song)
        talk("aviv play " + songEn)

        pywhatkit.playonyt(song)

    elif "תרגם" in command:
        text = command.replace("תרגם", "")
        talk(trans(text))

    elif "פתח" in command or "תפתח" in command:
        openApp = command.replace("פתח", "")
        openApp = openApp.replace("תפתח", "")
        #if 'league' in openApp:
         #   subprocess.Popen(["C:\\Users\\avivv\Desktop\League of Legends.lnk"])
        if "גוגל" in openApp:
            talk("opening google")
            subprocess.Popen(["C:\Program Files\Google\Chrome Beta\Application\chrome.exe"])
        elif "דיסקורד" in openApp or "דיס" in openApp:
            talk("opening discord")
            subprocess.Popen(["C:\\Users\\avivv\AppData\Local\Discord\\Update.exe"])
        elif "פוטושופ" in openApp:
            talk("opening photoshop")
            subprocess.Popen(["C:\Program Files\Adobe\Adobe Photoshop 2020\photoshop.exe"])

        else:
            talk("Aviv does not recognize the software")
    elif "בדיחה" in command or "jokes" in command:
        joke = pyjokes_hebrew.get_random_joke()
        print(joke)
        talk(trans(joke))
    elif "מה אתה יכול לעשות" in command or "מה את יכולה לעשות" in command:
        talk("not much now, but if you have a good idea i would like you to send me feedback")

    elif "שלח הודעה" in command or "תשלח הודעה" in command or "שלח וואטסאפ" in command:

        timeH = datetime.datetime.now().strftime("%H")
        timeM = datetime.datetime.now().strftime("%M")
        timeM1 = int(timeM) + 1
        person = command.split()[2]
        meseg = command.split()[3:]
        mesegTxt = ' '.join(meseg)
        print(person)
        print(mesegTxt)
        print(numbers[person])
        pywhatkit.sendwhatmsg(numbers[person], mesegTxt, int(timeH), timeM1, 10)
    elif "משוב" in command:
        feedback = open("feedback.txt", "a")
        feed = trans(command)
        feedback.write("\n" + feed)
        feedback.close()


def strat():

    run_aviv()
    inputprintComm.configure(text=printComm)
    print(printComm)

canvass = tk.Canvas(root, width=300, height=150, background="#4285f4", highlightthickness=0)

canvass.pack()

idFrame = tk.Frame(canvass, bg="#4285f4")
idFrame.place(height=150, width=300)


inputprintComm = Label(idFrame, text=printComm + "", bg="#4285f4", fg="white")
inputprintComm.pack()


photo = PhotoImage(file = "C:\\Users\\avivv\Pictures\\20210421_163757.png")
startAviv = tk.Button(idFrame, image=photo, text='הפעלת אביב', padx=30, pady=15, fg="white", bg="#1c4f2b", command=strat)#picture="C:\Users\avivv\Downloads\logo_students.png", command=masov()
startAviv.pack()



root.mainloop()
#pyinstaller -F main.py --hidden-import=pyttsx3.drivers --hidden-import=pyttsx3.drivers.dummy --hidden-import=pyttsx3.drivers.espeak --hidden-import=pyttsx3.drivers.nsss --hidden-import=pyttsx3.drivers.sapi5