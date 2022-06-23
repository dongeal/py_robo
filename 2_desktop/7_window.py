import pyautogui

# fw = pyautogui.getActiveWindow() # 현대 활성창
# print(fw.title)
# print(fw.size)
# print(fw.left, fw.top, fw.right,fw.bottom)
# pyautogui.click(fw.left+50,fw.top+10)

# for w in pyautogui.getAllWindows():
#     print(w) # 모든 윈도우  정보

# for w in pyautogui.getWindowsWithTitle("제목 없음"):
#     print(w)
# <Win32Window left="191", top="107", width="1536", height="864", title="제목 없음 - 그림판">
# <Win32Window left="1034", top="491", width="478", height="336", title="제목 없음 - Windows 메모장">

w = pyautogui.getWindowsWithTitle("제목 없음")[0]
print(w)

if w.isActive == False:
    w.activate() # 활성화( 맨앞으로 가져오기)
if w.isMaximized ==False:
    w.maximize() # 최대창

# if w.isMinimized ==False:
#     w.minimized
pyautogui.sleep(1)
w.restore() # 화면 복구
w.close()