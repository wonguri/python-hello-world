#!/bin/bash
# Windows용 .exe 파일을 빌드하는 스크립트

echo "Building Windows .exe file using Docker..."

# Docker 이미지 빌드
docker build -f Dockerfile.windows -t test-windows-builder .

# 컨테이너 실행 및 dist 폴더 복사
docker run --name temp-builder test-windows-builder
docker cp temp-builder:/app/dist/test.exe ./dist/test.exe
docker rm temp-builder

echo "Build complete! Windows executable: dist/test.exe"
