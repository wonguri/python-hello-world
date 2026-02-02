# Windows .exe 파일 빌드 가이드

`test.py`를 Windows 실행 파일(`.exe`)로 변환하는 방법입니다.

## 방법 1: GitHub Actions 사용 (가장 간단 ✨ 추천)

### 단계:
1. GitHub에 저장소 만들기
2. 이 프로젝트를 GitHub에 push
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/사용자명/저장소명.git
   git push -u origin main
   ```
3. GitHub 저장소의 **Actions** 탭에서 자동으로 빌드됨
4. 완료되면 **Artifacts**에서 `test-windows-exe.zip` 다운로드

### 장점:
- ✅ 추가 소프트웨어 설치 불필요
- ✅ 무료
- ✅ 자동화 가능

---

## 방법 2: Docker 사용

### 필요사항:
- Docker Desktop 설치 필요

### 단계:
1. [Docker Desktop](https://www.docker.com/products/docker-desktop/) 다운로드 및 설치
2. 빌드 스크립트 실행:
   ```bash
   ./build-windows.sh
   ```
3. `dist/test.exe` 파일 생성됨

---

## 방법 3: Windows 컴퓨터에서 직접 빌드

### 단계:
1. Windows 컴퓨터에서 Python 설치
2. PyInstaller 설치:
   ```cmd
   pip install pyinstaller
   ```
3. 실행 파일 빌드:
   ```cmd
   pyinstaller --onefile test.py
   ```
4. `dist\test.exe` 파일 생성됨

---

## 현재 상태
- ✅ macOS 실행 파일: `dist/test` (이미 빌드됨)
- ⏳ Windows 실행 파일: 위 방법 중 하나 선택

## 추천
**간단한 프로젝트**라면 → **방법 1 (GitHub Actions)** 사용
**Docker 있다면** → **방법 2** 사용
**Windows PC 있다면** → **방법 3** 사용
