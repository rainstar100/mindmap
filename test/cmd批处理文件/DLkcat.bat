@echo off

:: 设置要进入的目录路径
set "targetDir=D:\mindmap\DLKcatReproduce\DeeplearningApproach"

:: 设置要激活的Conda环境名称
set "condaEnvName=DLKcat"

:: 进入目标目录
cd /d "%targetDir%"

:: 激活Conda环境
conda activate "%condaEnvName%"


echo Conda环境 %condaEnvName% 已激活。

:: 保持命令行窗口打开，等待用户按键（可选）
pause