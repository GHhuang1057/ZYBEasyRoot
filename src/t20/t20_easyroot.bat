cd ..
cd ..
set thisdir=%cd%
:: 激活虚拟环境
%thisdir%ZYBEasyRoot\res\mtkclient\.venv\Scripts\Activate.ps1
::unlock bootloader
echo 解锁bootloader
python %thisdir%ZYBEasyRoot\res\mtkclient\mtk.py e metadata,userdata,md_udc
python %thisdir%ZYBEasyRoot\res\mtkclient\mtk.py da seccfg unlock
::提取boot
echo 提取boot
python %thisdir%ZYBEasyRoot\res\mtkclient\mtk.py r boot boot.bin
ren boot.bin boot.img
echo 请手动修补boot镜像,并保存到项目res/mtkclient目录下,教程在README(貌似还没开始写)
%thisdir%ZYBEasyRoot\res\Magiskpatcher.exe
echo 修补完成
ren boot.img boot_patched.bin
python %thisdir%ZYBEasyRoot\res\mtkclient\mtk.py w boot boot_patched.bin
echo 重启
python %thisdir%ZYBEasyRoot\res\mtkclient\mtk.py reset
echo 1分钟之内如果没有启动,请手动重启.....
pause
