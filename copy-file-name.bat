@echo off
set arg1=%1
set arg2=%2
set arg3=%3 
echo %arg1%
echo %arg2%
echo %arg3%
echo FIN
%~dp0\copy-file-name\copy-file-name.py  %arg1%  %arg2%  %arg3%
rem pause