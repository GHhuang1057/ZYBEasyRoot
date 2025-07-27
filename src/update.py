import requests
from packaging import version

CURRENT_VERSION = "1.0.0"
UPDATE_SERVER_URL = "http://api.zyb.unote.tbit.top/api/version"
GITHUB_RELEASE_URL = "https://github.com/GHhuang1057/ZYBEasyRoot/releases"

def check_for_updates():
    try:
        response = requests.get(UPDATE_SERVER_URL, timeout=5)
        response.raise_for_status()
        
        latest_version = response.text.strip()
        print(f"当前版本: {CURRENT_VERSION}")
        print(f"最新版本: {latest_version}")
        
        if version.parse(latest_version) > version.parse(CURRENT_VERSION):
            print("发现新版本!")
            print(f"请访问 {GITHUB_RELEASE_URL} 下载最新版本。")
            print("请退出程序并安装更新。")
            return True, latest_version
        else:
            print("当前已是最新版本")
            return False, None
    
    except requests.exceptions.RequestException as e:
        print(f"检查更新失败: {str(e)}")
        return False, None

if __name__ == "__main__":
    check_for_updates()
    print("发现新版本!")