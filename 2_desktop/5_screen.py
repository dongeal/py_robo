import pyautogui
# 스크린샷 찍기
img= pyautogui.screenshot()
# img.save("screenshot.png") # 파이로 저장

# pyautogui.mouseInfo()
# 45,50 74,175,243 #4AAFF3 

pixel =pyautogui.pixel(45,50)
print(pixel) # 74,175,243

# print (pyautogui.pixelMatchesColor(45,50,(74,175,243))) # True
print(pyautogui.pixelMatchesColor(45,50,pixel)) # True
print(pyautogui.pixelMatchesColor(45,50,(74,175,244))) #False