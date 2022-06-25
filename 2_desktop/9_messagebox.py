import pyautogui
# print("곧 시작합니다.")
# pyautogui.countdown(3)
# print("자동화 시작")

#pyautogui.alert("자동화 수행에 실패.", "경고") # 확인버튼만 있는팝업
# result = pyautogui.confirm("계속 진행하시겠?","확인") # 확인 , 취소 버튼
# print(result) # OK , Cancel  리턴
# result = pyautogui.prompt("파일명은 무엇으로?", "입력") # 사용자입력
# print(result) # 입력한것, None 리턴
result = pyautogui.password("암호를 입력", "암호입력")
print (result)




