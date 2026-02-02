#!/bin/bash
# macOS에서 Wine을 사용하여 Windows용 EXE 빌드

echo "=== macOS에서 Windows용 EXE 파일 생성 (Wine 사용) ==="
echo ""

# Wine 설치 확인
if ! command -v wine &> /dev/null
then
    echo "❌ Wine이 설치되어 있지 않습니다."
    echo ""
    echo "Homebrew로 Wine 설치:"
    echo "  brew install --cask wine-stable"
    echo ""
    echo "또는:"
    echo "  brew install wine-stable"
    echo ""
    exit 1
fi

echo "✓ Wine 확인 완료"
echo ""

# Windows Python 다운로드 및 설치
PYTHON_INSTALLER="python-3.11.0-amd64.exe"
PYTHON_URL="https://www.python.org/ftp/python/3.11.0/${PYTHON_INSTALLER}"

if [ ! -f "$PYTHON_INSTALLER" ]; then
    echo "📥 Windows용 Python 다운로드 중..."
    curl -o "$PYTHON_INSTALLER" "$PYTHON_URL"
fi

# Wine 환경에서 Python 설치
if [ ! -d "$HOME/.wine/drive_c/Python311" ]; then
    echo "🔧 Wine 환경에 Python 설치 중..."
    wine "$PYTHON_INSTALLER" /quiet InstallAllUsers=1 PrependPath=1
    sleep 5
fi

echo "✓ Python 설치 확인 완료"
echo ""

# Wine Python으로 패키지 설치
echo "📦 필요한 패키지 설치 중..."
wine python -m pip install --upgrade pip
wine python -m pip install -r requirements.txt

echo ""
echo "🔨 EXE 파일 생성 중..."

# PyInstaller로 EXE 생성
wine python -m PyInstaller --onefile --windowed --name "암호초기화" test.py

echo ""
echo "=== 빌드 완료! ==="
echo "✓ 생성된 파일: dist/암호초기화.exe"
echo ""
echo "이 파일은 Windows에서 독립적으로 실행 가능합니다!"
