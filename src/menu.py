import pyfiglet
from packaging import version
from .update import check_for_updates, CURRENT_VERSION
from .t20.t20_menu import t20_main
from .t20pplus.t20pplus_menu import t20pplus_main
from .t20pro.t20pro_menu import t20pro_main
 
def main():
    create_menu()

def create_menu():
    text = "ZYBEasyRoot"
    result = pyfiglet.figlet_format(text)
    print(result)
    print("正在检查更新.....")
    update_available, latest_version = check_for_updates()
    if update_available:
        print(f"发现新版本: {latest_version}")
    else:
        print("当前已是最新版本")
    eula()

def eula():
    print("用户协议")
    print("1. 本软件仅用于学习交流，不得用于任何商业用途。")
    print("2. 本软件不提供任何形式的技术支持或保证。")
    print("3. 用户需自行承担因使用本软件而产生的任何损失或损害。")
    print("4. 本软件的使用可能会违反相关的法律或法规，用户需自行承担法律风险。")
    print("5. 本软件的开发者不对用户的任何损失或损害承担责任。")
    eula_input = input("是否同意用户协议？(y/n): ")
    if eula_input.lower() == 'y':
        list_menu()
    else:
        print("您未同意用户协议，程序将退出。")
        input("请按回车键退出...")
        exit()

def list_menu():
    print("选择您的机型")
    print("1.T20")
    print("2.T20 Pro")
    print("3.T20 Pro+")
    print("0.退出")
    choice = input("请输入您的机型: ")
    if choice == '1':
        print("您选择了T20")
        t20_main()
    elif choice == '2':
        print("您选择了T20 Pro")
    elif choice == '3': 
        print("您选择了T20 Pro+")
        t20pplus_main()
    elif choice == '0':
        print("退出程序")
        exit()
    else:
        print("您输入的机型有误")
    list_menu()