#!/usr/local/bin/python3
grade = input("请输入成绩:")
if int(grade) > 90:
    print("优秀")
elif int(grade) > 80:
    print("好")
elif int(grade) > 70:
    print("良")
elif int(grade) > 60:
    print("及格")
else: 
    print("你要努力了")
