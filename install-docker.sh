#!/bin/bash
# Docker Desktop 설치 스크립트

echo "🐋 Docker Desktop 다운로드 중..."

# Apple Silicon (M1/M2) 또는 Intel 확인
ARCH=$(uname -m)

if [ "$ARCH" = "arm64" ]; then
    echo "Apple Silicon Mac 감지됨"
    DOCKER_URL="https://desktop.docker.com/mac/main/arm64/Docker.dmg"
else
    echo "Intel Mac 감지됨"
    DOCKER_URL="https://desktop.docker.com/mac/main/amd64/Docker.dmg"
fi

# DMG 파일 다운로드
curl -L -o ~/Downloads/Docker.dmg "$DOCKER_URL"

echo ""
echo "✅ Docker Desktop 다운로드 완료!"
echo ""
echo "📍 위치: ~/Downloads/Docker.dmg"
echo ""
echo "다음 단계:"
echo "1. Finder에서 Downloads 폴더를 엽니다"
echo "2. Docker.dmg 파일을 더블클릭합니다"
echo "3. Docker 아이콘을 Applications 폴더로 드래그합니다"
echo "4. Applications 폴더에서 Docker를 실행합니다"
echo ""
echo "설치 후 터미널에서 'docker --version'으로 확인하세요!"
