#!/bin/bash
# macOS에서 단일 EXE 파일 생성 (Wine + PyInstaller)

echo "=== 단일 EXE 파일 생성 ==="
echo ""

# Wine 확인
if ! command -v wine &> /dev/null; then
    echo "❌ Wine이 설치되어 있지 않습니다."
    echo ""
    echo "Homebrew로 Wine 설치:"
    echo "  brew tap homebrew/cask-versions"
    echo "  brew install --cask wine-stable"
    echo ""
    echo "또는 Crossover를 사용할 수도 있습니다."
    echo ""
    read -p "지금 Wine을 설치하시겠습니까? (y/n): " install_wine
    
    if [ "$install_wine" = "y" ]; then
        echo "Wine 설치 중..."
        brew install --cask wine-stable
    else
        echo "Wine이 필요합니다. 설치 후 다시 실행하세요."
        exit 1
    fi
fi

echo "✓ Wine 확인 완료"
echo ""

# Wine 환경 초기화
export WINEARCH=win64
export WINEPREFIX="$HOME/.wine"

# Python 설치 확인
PYTHON_DIR="$WINEPREFIX/drive_c/Python311"

if [ ! -d "$PYTHON_DIR" ]; then
    echo "📥 Windows용 Python 다운로드 중..."
    PYTHON_INSTALLER="python-3.11.7-amd64.exe"
    
    if [ ! -f "$PYTHON_INSTALLER" ]; then
        curl -L -o "$PYTHON_INSTALLER" "https://www.python.org/ftp/python/3.11.7/$PYTHON_INSTALLER"
    fi
    
    echo "🔧 Python 설치 중 (시간이 걸릴 수 있습니다)..."
    wine "$PYTHON_INSTALLER" /quiet InstallAllUsers=1 PrependPath=1 Include_pip=1
    
    # 설치 완료 대기
    sleep 10
fi

echo "✓ Python 설치 확인 완료"
echo ""

# pip 업그레이드
echo "📦 pip 업그레이드..."
wine python -m pip install --upgrade pip

# 필요한 패키지 설치
echo "📦 필요한 패키지 설치 중..."
wine python -m pip install ldap3 pyinstaller

echo ""
echo "🔨 단일 EXE 파일 생성 중..."
echo ""

# PyInstaller로 단일 EXE 생성
wine python -m PyInstaller \
    --onefile \
    --windowed \
    --name "암호초기화" \
    --clean \
    test.py

if [ $? -eq 0 ]; then
    echo ""
    echo "=== ✅ 빌드 완료! ==="
    echo ""
    echo "생성된 파일: dist/암호초기화.exe"
    
    if [ -f "dist/암호초기화.exe" ]; then
        SIZE=$(ls -lh "dist/암호초기화.exe" | awk '{print $5}')
        echo "파일 크기: $SIZE"
        echo ""
        echo "이 파일은 Windows에서 독립적으로 실행 가능한 단일 EXE입니다!"
        echo "Python이나 다른 라이브러리 설치 없이 바로 실행됩니다."
    fi
else
    echo ""
    echo "❌ 빌드 실패"
    echo ""
    echo "대안으로 portable_windows.zip을 사용하세요:"
    echo "  - Windows에서 압축 해제 후 run.bat 실행"
    echo "  - 완전히 독립 실행 가능"
fi
