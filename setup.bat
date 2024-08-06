@echo off
setlocal

REM Check if Python is installed
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Python not found. Installing Python...
    
    REM Download Python installer
    set PYTHON_INSTALLER=python-3.10.7-amd64.exe
    curl -O https://www.python.org/ftp/python/3.10.7/%PYTHON_INSTALLER%
    
    REM Install Python silently
    %PYTHON_INSTALLER% /quiet InstallAllUsers=1 PrependPath=1
    
    REM Clean up installer
    del %PYTHON_INSTALLER%
)

REM Upgrade pip
python -m pip install --upgrade pip

REM Install required packages
python -m pip install pyinstaller discord discord.ext.platform os asyncio sys Pillow requests socket datetime

echo All packages installed successfully.

endlocal
pause
