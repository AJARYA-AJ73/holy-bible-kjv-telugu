@echo off
cd /d "%~dp0"
set "PATH=%PATH%;%LOCALAPPDATA%\Programs\Git\cmd"
title Push Bible Web App to GitHub (AJARYA-AJ73)
cls
echo ====================================================================
echo        PUSH TO GITHUB REPOSITORY: AJARYA-AJ73
echo ====================================================================
echo.
git remote remove origin >nul 2>nul
git remote add origin https://github.com/AJARYA-AJ73/holy-bible-kjv-telugu.git
git branch -M main

echo.
echo Pushing code to https://github.com/AJARYA-AJ73/holy-bible-kjv-telugu ...
echo (A browser popup may ask you to sign in to GitHub to authorize)
echo.
git push -u origin main

if %ERRORLEVEL% equ 0 (
    echo.
    echo ====================================================================
    echo   SUCCESS! All project files pushed to your GitHub!
    echo   View your repository at:
    echo   https://github.com/AJARYA-AJ73/holy-bible-kjv-telugu
    echo ====================================================================
) else (
    echo.
    echo [NOTE] If this is the first time:
    echo 1. Make sure you created the repo at https://github.com/new
    echo    named "holy-bible-kjv-telugu"
    echo 2. Run this file again!
)
echo.
pause
