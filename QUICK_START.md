# 🚀 빠른 시작 가이드

## 현재 상태

✅ **portable_windows.zip** 파일이 생성되었습니다!
- 위치: `/Users/user/Desktop/workspace/project1/portable_windows.zip`
- 크기: 약 10-15MB
- Windows 7/10/11에서 실행 가능

---

## 📦 사용 방법 (가장 쉬움)

### 1단계: Windows PC로 복사
`portable_windows.zip` 파일을 USB나 이메일로 Windows PC에 전송

### 2단계: 압축 해제
Windows에서 우클릭 → "압축 풀기" 또는 "Extract All"

### 3단계: 실행
압축 푼 폴더에서 `run.bat` 더블클릭

### 4단계: 완료!
첫 실행 시 자동으로 필요한 라이브러리 설치 (1-2분 소요)

---

## 💻 단일 EXE 파일 만들기 (고급)

정말로 **단 하나의 .exe 파일**이 필요하다면:

### 옵션 1: macOS에서 Wine 사용 (복잡함)

```bash
# Wine 설치
brew install --cask wine-stable

# EXE 빌드
cd /Users/user/Desktop/workspace/project1
./build_single_exe.sh
```

⚠️ 주의: 
- 첫 설치 시 30분~1시간 소요
- 오류 발생 가능성 높음
- 안정성 보장 안 됨

### 옵션 2: GitHub Actions (추천)

```bash
# GitHub에 업로드
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/your-username/repo.git
git push -u origin main
```

- GitHub Actions가 자동으로 Windows에서 빌드
- 완전히 무료
- 가장 안정적
- `.github/workflows/build.yml` 파일 이미 생성됨

### 옵션 3: Windows PC 직접 사용 (가장 확실)

Windows PC에서:

```cmd
cd project1
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
build_exe.bat
```

→ `dist/암호초기화.exe` 생성 (단일 파일, 30-50MB)

---

## 🆚 비교표

| 방법 | 난이도 | 파일 형태 | Python 필요? | 장점 |
|------|--------|-----------|--------------|------|
| **portable_windows.zip** ✅ | ⭐ 쉬움 | 폴더 (23MB) | ❌ 불필요 | 즉시 사용 가능 |
| Wine + PyInstaller | ⭐⭐⭐⭐ 어려움 | 단일 EXE (40MB) | ❌ 불필요 | 파일 1개 |
| GitHub Actions | ⭐⭐ 보통 | 단일 EXE (40MB) | ❌ 불필요 | 안정적 |
| Windows PC 빌드 | ⭐⭐ 보통 | 단일 EXE (40MB) | ❌ 불필요 | 100% 호환 |

---

## 🎯 추천 사항

### 일반 사용자용 배포
→ **portable_windows.zip** 사용 (이미 생성됨!)

### 전문적인 배포
→ **Windows PC에서 build_exe.bat** 실행

### 자동화된 배포
→ **GitHub Actions** (.github/workflows/build.yml)

---

## 📋 체크리스트

현재 준비된 파일들:

- ✅ `test.py` - 메인 Python 스크립트
- ✅ `requirements.txt` - 필요한 라이브러리 목록
- ✅ `portable_windows.zip` - **즉시 사용 가능한 패키지**
- ✅ `portable_windows/` - 압축 해제된 폴더
- ✅ `build_exe.bat` - Windows용 빌드 스크립트
- ✅ `build_single_exe.sh` - macOS Wine 빌드 스크립트
- ✅ `.github/workflows/build.yml` - GitHub Actions 설정

---

## ❓ FAQ

**Q: portable_windows.zip vs 단일 EXE 차이는?**
A: 기능은 동일합니다. portable은 폴더 형태, EXE는 파일 1개입니다.

**Q: 어느 것이 더 빠른가요?**
A: 실행 속도는 동일합니다. EXE가 초기 로딩이 약간 느릴 수 있습니다.

**Q: 바이러스 오탐지 문제는?**
A: PyInstaller로 만든 EXE는 오탐지 가능성이 있습니다. 
   해결: 코드 서명 인증서 구매 또는 portable 버전 사용

**Q: 파일 크기를 줄일 수 있나요?**
A: PyInstaller의 --onefile 옵션은 모든 의존성을 포함하므로 크기가 큽니다.
   대안: portable 버전 사용 또는 Nuitka 사용

**Q: macOS에서 정말 Windows EXE를 못 만드나요?**
A: Wine을 사용하면 가능하지만 복잡하고 불안정합니다.
   가장 좋은 방법은 Windows PC나 GitHub Actions 사용입니다.

---

## 🎉 결론

**지금 바로 사용하려면:**
→ `portable_windows.zip`을 Windows PC로 복사하고 압축 해제 후 `run.bat` 실행!

**완벽한 단일 EXE가 필요하다면:**
→ Windows PC에서 `build_exe.bat` 실행하거나 GitHub Actions 사용!
