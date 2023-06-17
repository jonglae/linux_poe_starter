import pyautogui
import time

# print(pyautogui.position())

pyautogui.moveTo(2637, 501, 0.2) #2초 동안 이동
time.sleep(0.2) 
pyautogui.click()
time.sleep(0.3) 
pyautogui.hotkey('ctrl', 'q')  # ctrl-q to copy
time.sleep(0.2) 
pyautogui.hotkey('ctrl', 'w')  # ctrl-w to paste
time.sleep(0.5) 
pyautogui.hotkey('ctrl', 'e')  # ctrl-e to paste
time.sleep(0.3) 
pyautogui.hotkey('ctrl', 'r')  # ctrl-r to paste
time.sleep(0.3) 
pyautogui.hotkey('ctrl', 'd')  # ctrl-d to paste
time.sleep(0.2) 
pyautogui.hotkey('d')  # t
time.sleep(0.2) 
