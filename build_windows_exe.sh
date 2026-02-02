#!/bin/bash
# macOS에서 Windows용 EXE를 빌드하는 스크립트 (Docker 사용)

echo "=== macOS에서 Windows용 EXE 파일 생성 ==="
echo ""

# Docker가 설치되어 있는지 확인
if ! command -v docker &> /dev/null
then
    echo "❌ Docker가 설치되어 있지 않습니다."
    echo "Docker Desktop을 설치해주세요: https://www.docker.com/products/docker-desktop"
    exit 1
fi

echo "✓ Docker 확인 완료"
echo ""

# Docker 이미지 빌드
echo "📦 Windows 빌드 환경 생성 중..."
docker build -t windows-exe-builder .

if [ $? -ne 0 ]; then
    echo "❌ Docker 빌드 실패"
    exit 1
fi

echo ""
echo "🔨 EXE 파일 생성 중..."

# 컨테이너 실행 및 빌드된 파일 추출
docker run --name temp-builder windows-exe-builder

# dist 디렉토리가 없으면 생성
mkdir -p dist

# 컨테이너에서 EXE 파일 복사
docker cp temp-builder:/app/dist/암호초기화.exe ./dist/

# 임시 컨테이너 제거
docker rm temp-builder

echo ""
echo "=== 빌드 완료! ==="
echo "✓ 생성된 파일: dist/암호초기화.exe"
echo ""
echo "이 파일은 Windows에서 독립적으로 실행 가능합니다!"
