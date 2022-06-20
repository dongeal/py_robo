import pyautogui

#마우스 이동
# pyautogui.moveTo(200,100)
# pyautogui.moveTo(200,100,duration=5)

# pyautogui.moveTo(100,100,duration=0.25)
# pyautogui.moveTo(200,200,duration=0.25)
# pyautogui.moveTo(300,300,duration=0.25)

# pyautogui.moveTo(100,100,duration=0.25) # 절대좌표
# pyautogui.move(100,100,duration=0.25) #상대 좌표
# pyautogui.move(100,100,duration=0.25)

# print(pyautogui.position()) # Point(x,y)

p=pyautogui.position()
print(p[0],p[1]) #x,y
print(p.x,p.y)  #x,y