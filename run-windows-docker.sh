#!/bin/bash
# Wine이 설치된 Docker 컨테이너를 대화형으로 실행

echo "🐳 Wine Docker 컨테이너 시작..."
echo ""
echo "사용 가능한 명령어:"
echo "  - wine64 [프로그램.exe]    : Windows 프로그램 실행"
echo "  - python3                  : Python 실행"
echo "  - exit                     : 컨테이너 종료"
echo ""

docker run --rm -it \
    -v "$(pwd):/workspace" \
    -w /workspace \
    windows-wine \
    /bin/bash
