@echo off
title Start EVE - Evercrew Local AI Operating System
color 0B

echo =====================================================
echo           Starting EVE v0.1 Alpha
echo     Evercrew Local AI Operating System
echo =====================================================
echo.

echo Checking Ollama...

ollama --version >nul 2>&1
if errorlevel 1 (
echo.
echo ERROR: Ollama is not installed or not running.
echo.
echo Please install Ollama:
echo https://ollama.com/download
echo.
pause
exit /b 1
)

echo Ollama detected.
echo.

echo Checking AI model...

ollama list | findstr /I "llama3.2:3b" >nul

if errorlevel 1 (
echo.
echo The recommended AI model is not installed.
echo.
echo Please open Command Prompt and run:
echo.
echo     ollama pull llama3.2:3b
echo.
echo After downloading the model,
echo run Start EVE.bat again.
echo.
pause
exit /b 1
)

echo AI model found.
echo.

echo =====================================================
echo.
echo EVE is starting...
echo.
echo Do NOT close this window while EVE is running.
echo.
echo =====================================================
echo.

python app\main.py

echo.
echo =====================================================
echo EVE has stopped.
echo.
echo If this was unexpected,
echo please read the error message above.
echo =====================================================
echo.

pause
