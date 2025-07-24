import os
from .src.menu import list_menu

thisdir = os.path.dirname(os.path.abspath(__file__))

def t20pro_main():
    print("T20 Pro菜单")
    print("1. 一键Root")
    print("请输入您的选择: ")
    choice = input()
    if choice == '1':
        print("一键Root")
        t20pro_easyroot()
    else:
        print("您输入的选择有误")
        t20pro_main()

def t20pro_easyroot():
    print("T20 Pro一键Root")
    os.system(f"{thisdir}/t20pro_easyroot.sh")