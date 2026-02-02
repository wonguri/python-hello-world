#!/bin/bash
# macOS에서 Windows용 EXE를 빌드하는 가장 간단한 방법

echo "=== macOS에서 Windows용 EXE 파일 생성 ==="
echo ""
echo "⚠️  중요: macOS에서 Windows용 .exe를 직접 빌드하는 것은 제한적입니다."
echo ""
echo "다음 3가지 방법 중 하나를 선택하세요:"
echo ""
echo "1. ✅ GitHub Actions (권장) - 자동 빌드"
echo "   - GitHub에 코드를 푸시하면 자동으로 Windows에서 빌드"
echo "   - .github/workflows/build.yml 파일이 생성되었습니다"
echo "   - 완전히 무료이고 가장 안정적입니다"
echo ""
echo "2. 🍷 Wine 사용 (중급)"
echo "   - brew install --cask wine-stable"
echo "   - ./build_windows_exe_wine.sh 실행"
echo "   - 설정이 복잡하고 오류가 발생할 수 있습니다"
echo ""
echo "3. 💻 Windows 컴퓨터 사용 (가장 확실)"
echo "   - Windows PC나 가상머신에서 build_exe.bat 실행"
echo "   - 100% 호환성 보장"
echo ""
echo "---"
echo ""

read -p "어떤 방법을 사용하시겠습니까? (1/2/3): " choice

case $choice in
    1)
        echo ""
        echo "📝 GitHub Actions 설정 방법:"
        echo ""
        echo "1. 이 프로젝트를 GitHub에 업로드:"
        echo "   git init"
        echo "   git add ."
        echo "   git commit -m 'Initial commit'"
        echo "   git remote add origin https://github.com/your-username/your-repo.git"
        echo "   git push -u origin main"
        echo ""
        echo "2. GitHub에서 Actions 탭 확인"
        echo "3. 빌드가 완료되면 Artifacts에서 EXE 다운로드"
        echo ""
        ;;
    2)
        echo ""
        echo "🍷 Wine 방법을 선택하셨습니다."
        echo ""
        if command -v wine &> /dev/null; then
            echo "✓ Wine이 설치되어 있습니다."
            ./build_windows_exe_wine.sh
        else
            echo "Wine을 먼저 설치해주세요:"
            echo "  brew install --cask wine-stable"
            echo ""
            echo "설치 후 다시 이 스크립트를 실행하세요."
        fi
        ;;
    3)
        echo ""
        echo "💻 Windows 컴퓨터에서 실행:"
        echo ""
        echo "1. 이 폴더를 Windows PC로 복사"
        echo "2. Windows에서 build_exe.bat 더블클릭"
        echo "3. dist 폴더에 EXE 파일 생성 완료!"
        echo ""
        ;;
    *)
        echo "잘못된 선택입니다."
        ;;
esac
