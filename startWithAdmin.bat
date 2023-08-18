
@echo off
cd %~dp0
powershell -Command "Start-Process py '.\main.py' -Verb RunAs"
