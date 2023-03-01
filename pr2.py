from tkinter import *
from tkinter import messagebox
import time
from playsound import playsound
import datetime
import pyttsx3

root = Tk()
root.geometry("1500x1200")
root.title('DIGITAL CLOCK WITH ALARM SYSTEM')
root.config(bg='yellow')

def time_():
    curr_hour = time.strftime('%I')
    curr_min = time.strftime('%M')
    curr_sec = time.strftime('%S')
    curr_ampm = time.strftime('%p')
    curr_date = time.strftime('%d')
    curr_month = time.strftime('%m')
    curr_year = time.strftime('%Y')
    curr_day = time.strftime('%A')

    l1_h.config(text=curr_hour)
    l2_m.config(text=curr_min)
    l3_s.config(text=curr_sec)
    l4_ampm.config(text=curr_ampm)
    l1_date.config(text=curr_date)
    l2_month.config(text=curr_month)
    l3_year.config(text=curr_year)
    l4_day.config(text=curr_day)
    l1_h.after(200, time_)

txt1 = Label(root, text='TIME :', font='comicsansns 30 bold', bg='yellow', fg='black')
txt1.place(x=0, y=0)

l1_h = Label(root, font='comicsansns 55 bold', bg='green', fg='red', borderwidth=17, relief=SUNKEN)
l1_h.place(x=0, y=50, width=150, height=150)

l1 = Label(root, text=":", font='comicsansns 55 bold', bg='yellow', fg='red')
l1.place(x=170, y=50, width=20, height=150)

l2_m = Label(root, font='comicsansns 55 bold', bg='green', fg='red', borderwidth=17, relief=SUNKEN)
l2_m.place(x=210, y=50, width=150, height=150)

l2 = Label(root, text=":", font='comicsansns 55 bold', bg='yellow', fg='red')
l2.place(x=380, y=50, width=20, height=150)

l3_s = Label(root, font='comicsansns 55 bold', bg='green', fg='red', borderwidth=17, relief=SUNKEN)
l3_s.place(x=420, y=50, width=150, height=150)

l4_ampm = Label(root, font='comicsansns 55 bold', bg='green', fg='red', borderwidth=17, relief=SUNKEN)
l4_ampm.place(x=630, y=50, width=200, height=150)

txt2 = Label(root, text='DATE :', font='comicsansns 30 bold', bg='yellow', fg='black')
txt2.place(x=0, y=230)

l1_date = Label(root, font='comicsansns 55 bold', bg='green', fg='red', borderwidth=17, relief=SUNKEN)
l1_date.place(x=0, y=280, width=150, height=150)

l11 = Label(root, text="-", font='comicsansns 55 bold', bg='yellow', fg='red')
l11.place(x=170, y=280, width=20, height=150)

l2_month = Label(root, font='comicsansns 55 bold', bg='green', fg='red', borderwidth=17, relief=SUNKEN)
l2_month.place(x=210, y=280, width=150, height=150)

l22 = Label(root, text="-", font='comicsansns 55 bold', bg='yellow', fg='red')
l22.place(x=380, y=280, width=20, height=150)

l3_year = Label(root, font='comicsansns 55 bold', bg='green', fg='red', borderwidth=17, relief=SUNKEN)
l3_year.place(x=420, y=280, width=250, height=150)

txt3 = Label(root, text='DAY :', font='comicsansns 30 bold', bg='yellow', fg='black')
txt3.place(x=0, y=460)

l4_day = Label(root, font='comicsansns 55 bold', bg='green', fg='red', borderwidth=17, relief=SUNKEN)
l4_day.place(x=0, y=510, width=450, height=150)

txt3 = Label(root, text='ALARM SYSTEM :', font='comicsansns 30 bold', bg='yellow', fg='black')
txt3.place(x=900, y=0)

l4 = Label(root, font='comicsansns 55 bold', bg='white', borderwidth=17, relief=SUNKEN)
l4.place(x=850, y=50, width=450, height=300)


def alarm():
    global e1, e2
    window = Toplevel()
    window.geometry("530x500")

    t = Label(window, font='comicsansns 20 bold', text='Enter the time in military time format')
    t.place(x=30, y=0)

    hour1 = Label(window, text="SET HOUR", font=('comicsansns', 12, "bold"))
    hour1.place(x=30, y=50)

    e1 = Entry(window, relief=SUNKEN)
    e1.place(x=30,y=80)

    minute1 = Label(window, text="SET MINUTE", font=('comicsansns', 12, "bold"))
    minute1.place(x=200, y=50)

    e2 = Entry(window, relief=SUNKEN)
    e2.place(x=200,y=80)

    begin = Button(window, text="START", font=('comicsansns', 12, "bold"), relief=SUNKEN)
    begin.place(x=250, y=400)
    begin.bind("<Button-1>", alarm_begin)

def alarm_begin(event):
    global e1, e2
    h1 = e1.get()
    m1 = e2.get()

    while (1):
        if int(h1) == datetime.datetime.now().hour and int(m1) == datetime.datetime.now().minute:
            playsound("extreme_clock_alarm.mp3")
            messagebox.showinfo('WAKE UP!!!!!')
            break
def alarm():
    global e1, e2
    window = Toplevel()
    window.geometry("530x500")

    t = Label(window, font='comicsansns 20 bold', text='Enter the time in military time format')
    t.place(x=30, y=0)

    hour1 = Label(window, text="SET HOUR", font=('comicsansns', 12, "bold"))
    hour1.place(x=30, y=50)

    e1 = Entry(window, relief=SUNKEN)
    e1.place(x=30,y=80)

    minute1 = Label(window, text="SET MINUTE", font=('comicsansns', 12, "bold"))
    minute1.place(x=200, y=50)

    e2 = Entry(window, relief=SUNKEN)
    e2.place(x=200,y=80)

    begin = Button(window, text="START", font=('comicsansns', 12, "bold"), relief=SUNKEN)
    begin.place(x=250, y=400)
    begin.bind("<Button-1>", alarm_begin)

def alarm_begin(event):
    global e1, e2
    h1 = e1.get()
    m1 = e2.get()

    while (1):
        if int(h1) == datetime.datetime.now().hour and int(m1) == datetime.datetime.now().minute:
            playsound("extreme_clock_alarm.mp3")
            messagebox.showinfo('WAKE UP!!!!!')
            break

tx = Label(root, text='SET ALARM HERE :', font='comicsansns 20 bold', fg='green', bg='white')
tx.place(x=950, y=100)

btn = Button(root, borderwidth=17, bg='red', font='comicsansns 20 bold', command=alarm, text='CLICK').place(anchor=SW,x=1000,y=250)

txt4 = Label(root, text='AUDIO TIME :', font='comicsansns 30 bold', bg='yellow', fg='black')
txt4.place(x=930, y=370)

l5 = Label(root, font='comicsansns 55 bold', bg='white', borderwidth=17, relief=SUNKEN)
l5.place(x=850, y=420, width=450, height=270)

txx = Label(root, text='TELL US CURRENT TIME :', font='comicsansns 20 bold', fg='green', bg='white')
txx.place(x=910, y=450)

def audio_time():
    curr_ho = time.strftime('%H')
    curr_mi = time.strftime('%M')
    curr_se = time.strftime('%S')
    curr_ap = time.strftime('%p')

    if int(curr_ho) > 12:
        curr_ho = str(int(curr_ho) - 12)

    def audio():
        speak = pyttsx3.init()
        speak.say("the time is {} {} {}".format(curr_ho, curr_mi, curr_ap))
        speak.runAndWait()

    l1_h.config(text=curr_ho)
    l2_m.config(text=curr_mi)
    l3_s.config(text=curr_se)
    l4_ampm.config(text=curr_ap)

    l1_h.after(200, time_)

    btnn = Button(root, borderwidth=17, bg='red', font='comicsansns 20 bold', command=audio, text='CLICK').place(
        anchor=SW, x=1000, y=600)

time_()
audio_time()
root.mainloop()


