import tkinter
from tkinter.constants import COMMAND
import pyttsx3
import datetime
top=tkinter.Tk()
top.title("My alarm")
top.geometry('300x300')
engine=pyttsx3.init()
rate=engine.getProperty('rate')
engine.setProperty('rate',150)
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def alarm(alarm_time):
    while True:
        now=datetime.datetime.now().strftime("%H:%M")
        if alarm_time==now:
            engine.say("Hey your time is up") 
            engine.runAndWait()
            break
hour=tkinter.StringVar()
min=tkinter.StringVar()

def get_time():
    hr=hour.get()
    m=min.get()
    tim=f"{hr}:{m}"
    alarm(tim)

lbl=tkinter.Label(top,text="Set Alarm",foreground="red").place(x=108,y=20)
lbl1=tkinter.Label(top,text="Hour",foreground="green").place(x=95,y=40)
lbl2=tkinter.Label(top,text="Minute",foreground="green").place(x=135,y=40)
lbl3=tkinter.Label(top,text="By Alok").place(x=107,y=240)
entry_hour=tkinter.Entry(top,textvariable=hour).place(x=100,y=60,width=25)
entry_minute=tkinter.Entry(top,textvariable=min).place(x=140,y=60,width=25)
btn=tkinter.Button(top,text="Set",command=get_time).place(x=115,y=160)

top.mainloop()