import pyautogui
import time
from sys import argv

coordinates = {
    "x": 1448,
    "y": 440
}

# coordinates = [1448, 440]

frequency = int(argv[1])

try:
    interval = int(argv[2])
except:
    interval = 1


pyautogui.moveTo(**coordinates)


for click_times in range(frequency):
    pyautogui.click()
    time.sleep(interval)


