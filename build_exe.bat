@echo off
setlocal

REM Build freezer-1.3.exe with PyInstaller (run on Windows)
REM 1) pip install pyinstaller
REM 2) run this bat in repository root

pyinstaller --noconfirm --clean --onefile --windowed ^
  --name freezer-1.3 ^
  --add-data "freezer-1.3.html;." ^
  --add-data "index.html;." ^
  freezer_1_3_launcher.py

if %errorlevel% neq 0 (
  echo Build failed.
  exit /b %errorlevel%
)

echo.
echo Build complete: dist\freezer-1.3.exe
