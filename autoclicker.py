import pyautogui
import keyboard
import time

clicking = False

def toggle_clicking():
    global clicking
    clicking = not clicking
    print("Clicking:", clicking)

# Press "F6" to start/stop clicking
keyboard.add_hotkey("F6", toggle_clicking)

print("Press F6 to start/stop auto-clicking. Press ESC to quit.")

while True:
    if clicking:
        pyautogui.click()
        time.sleep(0.1)  # Adjust speed (lower = faster)
    
    if keyboard.is_pressed("esc"):
        print("Exiting...")
        break
