def t20_main():
    print("T20菜单")
    print("1. 一键Root")
    print("请输入您的选择: ")
    choice = input()
    if choice == '1':
        print("一键Root")
    else:
        print("您输入的选择有误")
        t20_main()