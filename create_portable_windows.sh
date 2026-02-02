#!/bin/bash
# macOS에서 Windows용 포터블 패키지 생성 (Python 포함)

echo "=== Windows용 포터블 실행 패키지 생성 ==="
echo ""

PACKAGE_DIR="portable_windows"
PYTHON_VERSION="3.11.7"
PYTHON_EMBED_URL="https://www.python.org/ftp/python/${PYTHON_VERSION}/python-${PYTHON_VERSION}-embed-amd64.zip"

# 패키지 디렉토리 생성
mkdir -p "$PACKAGE_DIR"

echo "📥 Windows용 Python 임베디드 버전 다운로드 중..."
curl -L -o "${PACKAGE_DIR}/python-embed.zip" "$PYTHON_EMBED_URL"

echo "📦 압축 해제 중..."
cd "$PACKAGE_DIR"
unzip -q python-embed.zip
rm python-embed.zip

# get-pip.py 다운로드
echo "📥 pip 설치 파일 다운로드 중..."
curl -o get-pip.py https://bootstrap.pypa.io/get-pip.py

# 필요한 파일 복사
echo "📄 프로젝트 파일 복사 중..."
cp ../test.py .
cp ../requirements.txt .

# 실행 배치 파일 생성
cat > run.bat << 'EOF'
@echo off
echo === 암호 초기화 프로그램 ===
echo.

REM 첫 실행 시 pip 설치
if not exist Lib\site-packages\pip (
    echo 초기 설정 중... 잠시만 기다려주세요...
    python.exe get-pip.py --no-warn-script-location
    
    REM python311._pth 파일 수정하여 site-packages 활성화
    echo python311.zip > python311._pth
    echo . >> python311._pth
    echo Lib\site-packages >> python311._pth
)

REM 필요한 패키지 설치 확인
if not exist Lib\site-packages\ldap3 (
    echo 필요한 라이브러리 설치 중...
    python.exe -m pip install -r requirements.txt --no-warn-script-location
)

REM 프로그램 실행
echo 프로그램 실행 중...
python.exe test.py

pause
EOF

# 설치 안내 파일 생성
cat > README.txt << 'EOF'
=== 암호 초기화 프로그램 - Windows 포터블 버전 ===

[ 사용 방법 ]

1. 이 폴더를 Windows PC로 복사하세요
2. run.bat 파일을 더블클릭하세요
3. 첫 실행 시 자동으로 필요한 라이브러리를 설치합니다 (인터넷 연결 필요)
4. 이후 실행할 때는 즉시 프로그램이 실행됩니다

[ 시스템 요구사항 ]

- Windows 10 이상 (64bit)
- 인터넷 연결 (첫 실행 시에만)
- 약 100MB의 디스크 공간

[ 주의사항 ]

- Python이 설치되어 있지 않아도 실행 가능합니다
- 이 폴더 전체를 USB에 복사하여 다른 PC에서도 사용 가능합니다
- 백신 프로그램이 차단하면 예외 처리하세요

[ 문제 해결 ]

Q: "python.exe를 찾을 수 없습니다" 오류
A: 폴더 내의 모든 파일이 그대로 있는지 확인하세요

Q: 라이브러리 설치 실패
A: 인터넷 연결을 확인하고 다시 실행하세요

Q: 프로그램이 실행되지 않음
A: Windows Defender나 백신 프로그램을 확인하세요
EOF

cd ..

echo ""
echo "=== 생성 완료! ==="
echo ""
echo "✓ 패키지 위치: ${PACKAGE_DIR}/"
echo ""
echo "📦 이 폴더를 Windows PC로 복사하고 run.bat를 실행하세요!"
echo ""
echo "파일 크기: $(du -sh ${PACKAGE_DIR} | cut -f1)"
echo ""
echo "💡 팁: 이 폴더를 ZIP으로 압축하여 배포하세요:"
echo "   zip -r portable_windows.zip ${PACKAGE_DIR}/"
