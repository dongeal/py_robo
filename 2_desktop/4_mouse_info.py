from imp import PY_CODERESOURCE
import pyautogui
pyautogui.FAILSAFE = False
# pyautogui.mouseInfo()

pyautogui.PAUSE=1 # 모든 동장에 1초 sleep

for i in range(5):
    pyautogui.move(100,100)