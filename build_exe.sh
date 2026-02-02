#!/bin/bash
# Windows용 EXE 빌드 스크립트

echo "=== Windows용 EXE 파일 생성 ==="
echo ""

# 가상환경 활성화
source .venv/bin/activate

# PyInstaller로 EXE 생성
pyinstaller --onefile \
    --windowed \
    --name "암호초기화" \
    --icon=NONE \
    --add-data "requirements.txt:." \
    test.py

echo ""
echo "=== 빌드 완료! ==="
echo "생성된 파일 위치: dist/암호초기화.exe"
