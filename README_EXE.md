# Windows용 EXE 파일 생성 가이드

## 방법 1: Windows에서 직접 빌드 (권장)

### 1단계: 필요한 프로그램 설치
Windows 컴퓨터에서 Python을 설치합니다.
- Python 다운로드: https://www.python.org/downloads/

### 2단계: 프로젝트 폴더로 이동
```cmd
cd C:\path\to\project1
```

### 3단계: 가상환경 생성 및 활성화
```cmd
python -m venv .venv
.venv\Scripts\activate
```

### 4단계: 필요한 라이브러리 설치
```cmd
pip install -r requirements.txt
```

### 5단계: EXE 파일 생성
```cmd
build_exe.bat
```

또는 수동으로:
```cmd
pyinstaller --onefile --windowed --name "암호초기화" test.py
```

### 6단계: 완성!
생성된 파일 위치: `dist\암호초기화.exe`

---

## 방법 2: 수동 PyInstaller 명령어

더 많은 옵션을 사용하려면:

```cmd
pyinstaller --onefile ^
    --windowed ^
    --name "암호초기화" ^
    --icon=icon.ico ^
    --add-data "config.ini;." ^
    test.py
```

### PyInstaller 옵션 설명:
- `--onefile`: 단일 exe 파일로 생성
- `--windowed`: 콘솔 창 숨김 (GUI 앱용)
- `--name`: exe 파일 이름 지정
- `--icon`: 아이콘 파일 지정 (.ico 파일)
- `--add-data`: 추가 데이터 파일 포함

---

## 방법 3: macOS/Linux에서 Windows용 빌드

macOS나 Linux에서 Windows용 exe를 만들려면 Wine을 사용해야 하지만,
**Windows 환경에서 직접 빌드하는 것을 강력히 권장합니다.**

macOS에서 시도하는 경우:
```bash
# Wine 설치 (Homebrew 필요)
brew install --cask wine-stable

# Windows Python 설치 (복잡함)
# 권장하지 않음 - Windows에서 빌드하세요!
```

---

## 배포 시 주의사항

1. **백신 프로그램**: PyInstaller로 만든 exe는 일부 백신에서 오탐지될 수 있습니다.
   - 해결: 코드 서명 인증서 구매 및 서명

2. **파일 크기**: exe 파일이 50-100MB 정도로 클 수 있습니다.
   - 이유: Python 인터프리터와 모든 라이브러리가 포함됨

3. **배포**: 생성된 exe 파일만 배포하면 됩니다.
   - Python 설치 불필요
   - 다른 라이브러리 설치 불필요

---

## 문제 해결

### "PyInstaller를 찾을 수 없음" 오류
```cmd
pip install pyinstaller
```

### "모듈을 찾을 수 없음" 오류
requirements.txt의 모든 라이브러리가 설치되었는지 확인:
```cmd
pip install -r requirements.txt
```

### exe 실행 시 "DLL 오류"
```cmd
pyinstaller --onefile --windowed --hidden-import=ldap3 test.py
```

---

## 고급: spec 파일 사용

더 세밀한 제어가 필요한 경우:

1. spec 파일 생성:
```cmd
pyinstaller --name "암호초기화" test.py
```

2. `암호초기화.spec` 파일 편집

3. spec 파일로 빌드:
```cmd
pyinstaller 암호초기화.spec
```

---

## 최종 결과

빌드가 완료되면 다음 구조가 생성됩니다:

```
project1/
├── dist/
│   └── 암호초기화.exe    ← 이 파일을 배포하세요!
├── build/              (임시 파일, 삭제 가능)
└── 암호초기화.spec      (빌드 설정 파일)
```

**`dist/암호초기화.exe`** 파일만 Windows 컴퓨터로 복사하여 사용하면 됩니다!
