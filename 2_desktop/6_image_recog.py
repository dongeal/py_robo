from tkinter import N
import pyautogui

# file_menu = pyautogui.locateOnScreen("file_menu.png")
# print(file_menu)
# pyautogui.click(file_menu)

# trash_icon= pyautogui.locateOnScreen("trash_icon.png")
# pyautogui.moveTo(trash_icon)

# screen=pyautogui.locateOnScreen("screenshot.png")
# print(screen)   # None 출력

# for i in pyautogui.locateAllOnScreen("checkbox.png"):
#     print(i)
#     pyautogui.click(i,duration=0.25)

# 속도개선
# 1. GrayScale
# trash_icon= pyautogui.locateOnScreen("trash_icon.png",grayscale=True)
# pyautogui.moveTo(trash_icon)

# # 2. 범위지정
# trash_icon= pyautogui.locateOnScreen("trash_icon.png", region=(1400,1800,500,500))
# pyautogui.moveTo(trash_icon)

# 3. 정확도 조정
# pip install opencv-python

# run_btn= pyautogui.locateOnScreen("run_icon.png", confidence=0.7)
# pyautogui.moveTo(run_btn)

# 자동화 대상이 바로 보여지지 않는 경우
# 1. 계속 기다리기
# file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
# # if file_menu_notepad:   
# #     pyautogui.click(file_menu_notepad)
# # else:
# #     print("발견 실패")
# while file_menu_notepad is None:
#     file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
#     print("발견 실패")
# pyautogui.click(file_menu_notepad)

# #2. 일정시간 기다리기(TimeOut)
import time
import sys

# timeout= 10
# start= time.time() # 시작시간설정
# file_menu_notepad = None
# while file_menu_notepad is None:
#     file_menu_notepad= pyautogui.locateOnScreen("file_menu_notepad.png")
#     end = time.time() # 종료시간
#     if end - start >10 :
#         print("시간 종료")
#         sys.exit()
# pyautogui.click(file_menu_notepad)

def find_target (img_file, timeout=30):
    start= time.time()
    target=None
    while target is None:
        target =pyautogui.locateOnScreen(img_file)
        end = time.time()
        if end - start > timeout:
            break
    return target

def my_click(img_file, timeout=30):
    target = find_target(img_file, timeout)
    if target:
        pyautogui.click(target)
    else:
        print(f"[Timeout {timeout}s] Target not found({img_file}). Terminate")
        sys.exit()
my_click("file_menu_notepad.png",10)