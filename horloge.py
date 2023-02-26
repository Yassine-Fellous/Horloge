import datetime
from time import sleep
from tkinter import *
import tkinter as tk

root = tk.Tk()
root.geometry("650x400+100+200")
root.resizable(False,False)
root.config(background="#04ed52")

value = 1
alarm_time = None

def open_window():#fonction pour ouvrir une fenètre secondaire, afin de changer l'heure
    global window, entryun, entrydeu, entrytroi
    window = tk.Toplevel(root)
    window.title("Sous-fenêtre")
    window.geometry("200x200")
    entryun = Entry(window, width=50, bg='#FFFFFF', fg='#000000', font=('Arial', 16), bd=5)  # notre entrée pour marquer la somme
    entryun.pack()
    entrydeu = Entry(window, width=50, bg='#FFFFFF', fg='#000000', font=('Arial', 16), bd=5)  # notre entrée pour marquer la somme
    entrydeu.pack()
    entrytroi = Entry(window, width=50, bg='#FFFFFF', fg='#000000', font=('Arial', 16), bd=5)  # notre entrée pour marquer la somme
    entrytroi.pack()
    Button(window, text="change", width=5, height=1, font=('arial', 30, 'bold'), command=change).place(x=100, y=200)


def change():#fonction pour vérifier si les valeur des entrés sont valide
    global value
    hours = entryun.get()
    minutes = entrydeu.get()
    seconds = entrytroi.get()
    if hours.isdigit() and minutes.isdigit() and seconds.isdigit():
        hours = int(hours)
        minutes = int(minutes)
        seconds = int(seconds)
        if hours >= 0 and hours <= 23 and minutes >= 0 and minutes <= 59 and seconds >= 0 and seconds <= 59:
            value = 2
            horloge()
            root.after(1000, horloge)
    global alarm_time
    alarm_time = current_time.time()

def horloge():#fonctionne pour afficher l'heure et vérifier si l'heure correpond a l'alarme définie
    global value, alarm_time, current_time
    if value == 1:
        current_time = datetime.datetime.now().time()
        time = "{}:{}:{}".format(current_time.hour, current_time.minute, current_time.second)
        oui.config(text=time)
        if alarm_time is not None and current_time >= alarm_time:
            alarme.config(text="alarme!")
        root.after(1000, horloge)
    elif value == 2:
        heures = int(entryun.get())
        minutes = int(entrydeu.get())
        secondes = int(entrytroi.get())
        current_time = datetime.datetime.now().replace(hour=heures, minute=minutes, second=secondes)
        actualiser(current_time)

def actualiser(current_time):#fonction pour mettre a jour l'heure
    while value == 2:
        current_time = current_time + datetime.timedelta(seconds=1)
        time = "{}:{}:{}".format(current_time.hour, current_time.minute, current_time.second)
        oui.config(text=time)
        root.update()
        root.after(1000, actualiser, current_time)
        sleep(1)

def set_alarm():#fonction qui vérifie si les valeurs entré son valide et définie l'alarme
    global alarm_time
    hours = alarm_entryun.get()
    minutes = alarm_entrydeu.get()
    seconds = alarm_entrytroi.get()
    if hours.isdigit() and minutes.isdigit() and seconds.isdigit():
        hours = int(hours)
        minutes = int(minutes)
        seconds = int(seconds)
        if hours >= 0 and hours <= 23 and minutes >= 0 and minutes <= 59 and seconds >= 0 and seconds <= 59:
            alarm_time = datetime.time(hours, minutes, seconds)
            print("Alarm set for:", alarm_time)


def open_alarm_window():#fontion qui est utiliser pour ouvrir une fenètre afin que l'utilisateur rentre les valeur de l'alarme
    global alarm_time, alarm_entryun, alarm_entrydeu, alarm_entrytroi
    alarm_window = tk.Toplevel(root)
    alarm_window.title("Alarme")
    alarm_window.geometry("200x200")
    alarm_entryun = Entry(alarm_window, width=50, bg='#FFFFFF', fg='#000000', font=('Arial', 16), bd=5)  
    alarm_entryun.pack()
    alarm_entrydeu = Entry(alarm_window, width=50, bg='#FFFFFF', fg='#000000', font=('Arial', 16), bd=5)  
    alarm_entrydeu.pack()
    alarm_entrytroi = Entry(alarm_window, width=50, bg='#FFFFFF', fg='#000000', font=('Arial', 16), bd=5)  
    alarm_entrytroi.pack()
    Button(alarm_window, text="Set Alarm", width=10, height=1, font=('arial', 16, 'bold'), command=set_alarm).place(x=50, y=150)




oui = Label(root, text="", background="#04ed52", font=('arial', 70, 'bold'), fg="#646966")
oui.place(x=150, y=70)

horloge()

Button(root, text="changer l'heur", width=14, height=1, font=('arial', 16, 'bold'), command=open_window).place(x=10, y=200)
Button(root, text="mettre une Alarme", width=14, height=1, font=('arial', 16, 'bold'), command=open_alarm_window).place(x=450, y=200)
alarme = Label(root, text="", background="#04ed52", font=('arial', 70, 'bold'), fg="#646966")
alarme.place(x=100, y=250)


root.mainloop()
