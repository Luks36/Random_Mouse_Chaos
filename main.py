import FreeSimpleGUI as sg
import threading
import random
import time
import pyautogui as pygui
import keyboard

running = False

buchstaben = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

layout = [
    [sg.Checkbox("Maus bewegen",  default=True, key="-MOVE-")],
    [sg.Checkbox("Linksklick",    default=True, key="-LCLICK-")],
    [sg.Checkbox("Rechtsklick",   default=True, key="-RCLICK-")],
    [sg.Checkbox("Doppelklick",   default=True, key="-DCLICK-")],
    [sg.Checkbox("Mausradklick",  default=True, key="-MCLICK-")],
    [sg.Checkbox("Windows-Key",   default=True, key="-WINDOWS-")],
    [sg.Checkbox("Alt + F4",      default=False, key="-ALT4-")],
    [sg.Button("Starten", key="-TOGGLE-")],
]

window = sg.Window("Mouse Chaos", layout)

def run_loop(values):
    global running
    while running:
        if keyboard.is_pressed("q"):
                    running = False
                    window["-TOGGLE-"].update("Starten")
                    pygui.alert("Session Terminated")
                    break
        active = [k for k in values if values[k]]
        if active:
            key = random.choice(active)
            if key == "-MOVE-":
                w, h = pygui.size()
                pygui.moveTo(random.randint(0, w), random.randint(0, h), 1)
            elif key == "-LCLICK-":
                pygui.click()
            elif key == "-RCLICK-":
                pygui.click(button="right")
            elif key == "-DCLICK-":
                pygui.doubleClick()
            elif key == "-MCLICK-":
                pygui.click(button="middle")
            elif key == "-WINDOWS-":
                pygui.press("win")
            elif key == "-ALT4-":
                pygui.hotkey("alt", "f4")
        time.sleep(1)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        running = False
        break

    if event == "-TOGGLE-":
        if not running:
            running = True
            window["-TOGGLE-"].update("Stoppen")
            threading.Thread(target=run_loop, args=(values,), daemon=True).start()
        else:
            running = False
            window["-TOGGLE-"].update("Starten")

window.close()