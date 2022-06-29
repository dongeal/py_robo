#파일 기본
import os
# print(os.getcwd()) # current working directory
# os.chdir("2_desktop")
# print(os.getcwd())
# os.chdir("..") # 부모 폴더로.
# print(os.getcwd())
# os.chdir("../..") # 조부모 폴더로.  ../../../
# print(os.getcwd())
# os.chdir("c:/") # 절대경로
# print(os.getcwd())

# # 파일 경로 포함 만들기
# file_path= os.path.join(os.getcwd(),"my_file.txt") 
# print (file_path)

# 파일 경로에서 폴더정보 가져오기
# print(os.path.dirname(r"C:\Users\ilheu\Desktop\py_rpa\my_file.txt"))

# # 파일 정보 가져오기
# import time
# import datetime

# #파일 생성 날짜
# ctime = os.path.getctime("run_icon.png")
# print(ctime) # 1655866424.2441707
# print(datetime.datetime.fromtimestamp(ctime))  # 2022-06-22 11:53:44.244171
# print(datetime.datetime.fromtimestamp(ctime).strftime("%Y%m%d %H:%M:%S"))
#    # 20220622 11:53:44
# #파일 수정 날짜
# mtime = os.path.getmtime("run_icon.png")
# print(datetime.datetime.fromtimestamp(mtime).strftime("%Y%m%d %H:%M:%S"))
# # 파일 접근 날짜
# atime = os.path.getatime("run_icon.png")
# print(datetime.datetime.fromtimestamp(atime).strftime("%Y%m%d %H:%M:%S"))

# #파일 크기
# file_path="2_desktop/11_file_system.py"
# size = os.path.getsize(file_path)
# print(size) #바이트 단위

# 파일 목록 가져오기

# print(os.listdir())
# print(os.listdir("2_desktop"))

# result = os.walk(".")
# for root, dirs, files in result:
#     print(root, dirs, files)

#만일 폴더내에서 특정파일 찾으려면?
# name = "11_file_system.py"
# result =[]
# for root, dirs, files in os.walk(os.getcwd()):
#     if name in files:
#         result.append(os.path.join(root,name))
# print(result)        

# # 폴더내에서 특정 패턴가진 파일
# # *.xlsx  *.txt   자동화*.png ....

# import fnmatch
# pattern = "*.py"

# result=[]
# for root,dirs,files in os.walk("."):
#     for name in files:
#         if fnmatch.fnmatch(name,pattern): 
#             result.append(os.path.join(root,name))
# print(result)            

# # 주어진 경로가 파일인지 폴더인지?
# print(os.path.isdir("2_desktop"))
# print(os.path.isfile("2_desktop"))

# print(os.path.isdir("file_menu.png"))
# print(os.path.isfile("file_menu.png"))

# 주어진 폴더 파일이 존재 하는지?
# if os.path.exists(r"2_desktop\11_file_system.py"):
#     print("폴더 또는 파일이 존재합니다.")
# else:
#     print("폴더 또는 파일이 없습니다.")

# 파일 만들기
# open("new_file.txt","a").close() # 빈파일 생성

# # # 파일명 변경하기
# # os.rename("new_file.txt","new_file_rename.txt")

# # 파일 삭제하기
# os.remove("new_file_rename.txt")

# 폴더 만들기
# os.mkdir("new_folder")
# os.makedirs("folders/a/b")# 하위폴더 가진 폴더 만들기
# 폴더 이름 변경
# os.rename("new_folder","new_folder_rename")

# #폴더 지우기
# os.rmdir("new_folder_rename") # 폴더가 비었을때만 가능

import shutil  # shell utilities
# shutil.rmtree("folders") # 폴더가 비워있지않아도 삭제가능
# # 모든 파일 지워지므로 주의!!!!!

# # 파일 복사하기
# shutil.copy("run_icon.png","test_folder")
# # shutil.copy("run_icon.png","test_folder/copied_run_icon.png")
# shutil.copyfile("run_icon.png","test_folder/copied_run_icon.png")#항상 파일명 까지 다넣어야됨
# shutil.copy2("run_icon.png","test_folder")

# copy copyfile  메타정보 x
# copy2          메타정보 o

# 폴더복사
# shutil.copytree("test_folder","test_folder2")

#폴더이동
# shutil.move("test_folder","test_folder2")







                              