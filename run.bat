@echo off
cd /d "%~dp0"
title Holy Bible (KJV & Telugu) Web Platform
cls
echo ====================================================================
echo             HOLY BIBLE WEB PLATFORM (KJV ^& TELUGU)
echo ====================================================================
echo.
echo   * Laptop Browser : http://localhost:8000
echo   * Mobile Phone   : http://192.168.31.180:8000
echo                      (Connect phone to the same Wi-Fi)
echo.
echo   Opening website in your browser...
echo   Keep this black window open while reading.
echo ====================================================================
echo.

start http://localhost:8000
python backend\main.py
pause
