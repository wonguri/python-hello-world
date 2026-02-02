#!/bin/bash
# GitHub에 코드를 push하는 스크립트
# 사용법: ./push-to-github.sh https://github.com/사용자명/저장소명.git

if [ -z "$1" ]; then
    echo "❌ 사용법: ./push-to-github.sh https://github.com/사용자명/저장소명.git"
    exit 1
fi

REPO_URL=$1

echo "🚀 GitHub 저장소에 코드를 push합니다..."
echo "저장소: $REPO_URL"
echo ""

# remote 추가
git remote add origin "$REPO_URL" 2>/dev/null || git remote set-url origin "$REPO_URL"

# main 브랜치로 변경
git branch -M main

# push
git push -u origin main

echo ""
echo "✅ Push 완료!"
echo ""
echo "📍 다음 단계:"
echo "1. GitHub 저장소 페이지로 이동하세요"
echo "2. 'Actions' 탭을 클릭하세요"
echo "3. 'Build Windows EXE' 워크플로우가 자동으로 실행됩니다"
echo "4. 완료되면 (약 2-3분 소요) Artifacts에서 'test-windows-exe'를 다운로드하세요"
echo ""
echo "🎉 Windows용 test.exe 파일을 얻을 수 있습니다!"
