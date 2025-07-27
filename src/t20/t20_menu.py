import subprocess
import os

thisdir = os.path.dirname(os.path.abspath(__file__))

def t20_main():
    print("T20菜单")
    print("1. 一键Root")
    print("2. 备份")
    print("3. 恢复")
    print("0. 退出")
    print("请输入您的选择: ")
    choice = input()
    if choice == '1':
        print("一键Root")
        t20_easyroot()
    elif choice == '2':
        print("备份")
        t20_bak()
    elif choice == '3':
        print("恢复")
        t20_rec()
    elif choice == '0':
        print("退出")
        exit()
    else:
        print("您输入的选择有误")
        t20_main()

def t20_easyroot():
    subprocess.run(thisdir + "/t20_easyroot.bat", shell=True)

def t20_bak():
    subprocess.run(thisdir + "/t20_bak.bat", shell=True)

def t20_rec():
    subprocess.run(thisdir + "/t20_rec.bat", shell=True)
