import random 
import os
import datetime
script_dir = os.path.dirname(os.path.abspath(__file__))
options_path = os.path.join(script_dir, "options.txt")
with open(options_path, "r")as file:
    lines = file.readlines()
pick = random.choice(lines).strip()
print(pick)
print(str(datetime.datetime.now()))


history = os.path.join(script_dir, "history.txt")
timestamp = str(datetime.datetime.now())
with open(history, "a") as file:
    file.write(f"{timestamp} — {pick}\n")