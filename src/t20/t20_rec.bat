cd ..
cd ..
set thisdir=%cd%
:: 激活虚拟环境
%thisdir%res/mtkclient/.venv/Scripts/Activate.ps1
:: 恢复
echo 恢复
python %thisdir%res/mtkclient/mtk.py wf backup.bin
:: 重启
echo 重启
python %thisdir%res/mtkclient/mtk.py reset