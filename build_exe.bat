@echo off
REM Windows용 EXE 빌드 스크립트

echo === Windows용 EXE 파일 생성 ===
echo.

REM 가상환경 활성화
call .venv\Scripts\activate.bat

REM PyInstaller로 EXE 생성
pyinstaller --onefile ^
    --windowed ^
    --name "암호초기화" ^
    --icon=NONE ^
    test.py

echo.
echo === 빌드 완료! ===
echo 생성된 파일 위치: dist\암호초기화.exe
pause
