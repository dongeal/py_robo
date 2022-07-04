# Quiz) 아래 동작을 자동 수횅하는 프로그램 만드시오

# 1. 그림판 실행 (단축키 : win + r, 입력값 mspaint) 및 최대화

# 2. 상단의 텍스트 기능 이용하여 흰영역 아무곳에다 글자 입력
#  - 입력 글자 "참 잘 했어요"

#  3. 5초 대기 후 그림판 종료
#  이때 저장하지 안음을 자동으로 선택되도록함.

import pyautogui
import pyperclip

pyautogui.hotkey("win","r")
pyautogui.sleep(0.2)
pyautogui.write("mspaint")
pyautogui.hotkey("enter")
pyautogui.sleep(1)
window=pyautogui.getWindowsWithTitle("제목 없음 - 그림판")[0]
if window.isMaximized == False:
    window.maximize()

brush_btn= pyautogui.locateOnScreen("btn_brush.png")
pyautogui.click(brush_btn,duration=0.2)

pyautogui.click(200,200, duration=0.2)

def my_write(text):
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl","v")

my_write("참 잘 했어요.")

pyautogui.sleep(5)
window.close()
pyautogui.sleep(0.5)
pyautogui.hotkey("n")