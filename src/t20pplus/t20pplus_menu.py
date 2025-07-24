

def t20pplus_main():
    print("T20 Pro+菜单")
    print("1. 一键Root")
    print("请输入您的选择: ")
    choice = input()
    if choice == '1':
        print("一键Root")
        t20pplus_easyroot()
    else:
        print("您输入的选择有误")
        t20pplus_main()

def t20pplus_easyroot():
    print("T20 Pro+一键Root")
