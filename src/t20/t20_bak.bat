cd ..
cd ..
set thisdir=%cd%
:: 激活虚拟环境
%thisdir%res/mtkclient/.venv/Scripts/Activate.ps1
:: 备份
echo 备份
python %thisdir%res/mtkclient/mtk.py rf backup.bin
:: 重启
echo 重启
python %thisdir%res/mtkclient/mtk.py reset
