import pyautogui
w=pyautogui.getWindowsWithTitle("제목 없음 - 메모장")[0] 
        # 메모장 1개 띠운상태에서 가져옴
w.activate()

pyautogui.write("12345")
pyautogui.write("Nadocoding", interval= 0.25)
# pyautogui.write("나도코딩") # 한글 안됨
# pyautogui.write(["t","e","s","t","left","left","right","1","a","enter"],interval=0.25)

# 특수문자
# shift 4 --- $
# pyautogui.keyDown("shift")
# pyautogui.press("4")
# pyautogui.keyUp("shift")

# # 조합키
# pyautogui.keyDown("ctrl")
# pyautogui.keyDown("a")
# pyautogui.keyUp("a")
# pyautogui.keyUp("ctrl")  # Ctrl+A

# 간편한 조합키
# pyautogui.hotkey("ctrl","alt","shift","a")
# pyautogui.hotkey("ctrl","a")


# 한글 입력
# pip install pyperclip
# import pyperclip

# # pyperclip.copy("나도코딩") # 나도코딩 글자를 클립보드에저장
# # pyautogui.hotkey("ctrl","v")

# def my_write(text):
#     pyperclip.copy(text)
#     pyautogui.hotkey("ctrl","v")

# my_write("함수만들어 입력")

# # 자동화 프로그램 종료
# # win : ctrl + alt + del
# # mac : cmd + shift + option + q
