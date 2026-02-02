# Windows에서 단일 EXE 빌드하기

## 🎯 목표
단 하나의 `.exe` 파일로 Windows에서 독립 실행

---

## 📋 준비물 (Windows PC에서)

1. Python 3.11 설치
   - https://www.python.org/downloads/
   - 설치 시 "Add Python to PATH" 체크 필수!

---

## 🚀 빌드 방법

### 방법 1: 자동 빌드 스크립트 (권장)

Windows PC에서 PowerShell 열고:

```powershell
cd project1

# 가상환경 생성
python -m venv .venv

# 가상환경 활성화
.venv\Scripts\Activate.ps1

# 패키지 설치
pip install -r requirements.txt

# 빌드 실행 (.bat 파일 더블클릭 또는 명령어로 실행)
.\build_exe.bat
```

→ `dist\암호초기화.exe` 생성됨 (약 40MB, 단일 파일)

---

### 방법 2: spec 파일 사용 (더 많은 제어)

```powershell
cd project1
.venv\Scripts\Activate.ps1

# spec 파일로 빌드
pyinstaller 암호초기화.spec
```

→ `dist\암호초기화.exe` 생성됨

---

### 방법 3: 수동 명령어

```powershell
pyinstaller --onefile --windowed --name "암호초기화" test.py
```

---

## 🎨 아이콘 추가하기 (선택사항)

1. `.ico` 파일 준비 (예: `icon.ico`)
2. `build_exe.bat` 수정:

```bat
pyinstaller --onefile ^
    --windowed ^
    --name "암호초기화" ^
    --icon=icon.ico ^
    test.py
```

또는 `암호초기화.spec` 파일의 `icon=None`을 `icon='icon.ico'`로 변경

---

## ✅ 빌드 성공 확인

빌드가 완료되면:

```
project1/
├── dist/
│   └── 암호초기화.exe    ← 이것이 최종 파일!
├── build/              (임시 파일, 삭제 가능)
└── 암호초기화.spec
```

**`dist/암호초기화.exe`를 다른 Windows PC로 복사해서 바로 실행 가능!**

---

## 🐛 문제 해결

### 1. "python을 찾을 수 없습니다" 오류

**원인:** Python이 PATH에 없음

**해결:**
- Python 재설치 시 "Add Python to PATH" 체크
- 또는 수동으로 PATH 추가

---

### 2. "pyinstaller를 찾을 수 없습니다" 오류

**원인:** PyInstaller 미설치

**해결:**
```powershell
pip install pyinstaller
```

---

### 3. 실행 시 "DLL 로드 실패" 오류

**원인:** 숨겨진 import가 포함되지 않음

**해결:** `암호초기화.spec` 파일 수정
```python
hiddenimports=['ldap3', 'ldap3.utils', 'tkinter', '_tkinter'],
```

그리고 다시 빌드:
```powershell
pyinstaller 암호초기화.spec
```

---

### 4. 백신 프로그램이 차단함

**원인:** PyInstaller로 만든 EXE는 오탐지 가능

**해결:**
- 백신 예외 처리 추가
- 또는 코드 서명 인증서 구매 (전문 배포용)

---

### 5. 파일 크기가 너무 큼 (50MB+)

**원인:** Python과 모든 라이브러리가 포함됨

**해결 (파일 크기 줄이기):**

```powershell
# UPX 압축 사용
pip install pyinstaller[encryption]
pyinstaller --onefile --windowed --upx-dir=.\upx test.py
```

또는 불필요한 라이브러리 제외:
```python
# spec 파일에서
excludes=['matplotlib', 'numpy', 'pandas'],  # 사용하지 않는 것들
```

---

### 6. 실행 시 콘솔 창이 보임

**원인:** `--windowed` 옵션 누락

**해결:**
```powershell
pyinstaller --onefile --windowed test.py
```

---

## 📊 빌드 옵션 설명

| 옵션 | 설명 |
|------|------|
| `--onefile` | 단일 EXE 파일로 생성 |
| `--windowed` | 콘솔 창 숨김 (GUI 앱용) |
| `--name` | EXE 파일 이름 지정 |
| `--icon` | 아이콘 파일 (.ico) 지정 |
| `--clean` | 이전 빌드 캐시 삭제 |
| `--upx-dir` | UPX로 압축 (파일 크기 감소) |
| `--add-data` | 추가 데이터 파일 포함 |
| `--hidden-import` | 자동 감지 안 되는 모듈 명시 |

---

## 🎯 최종 체크리스트

빌드 전:
- [ ] Python 3.11 설치됨
- [ ] 가상환경 활성화됨
- [ ] requirements.txt의 모든 패키지 설치됨
- [ ] test.py가 정상 실행됨

빌드 후:
- [ ] dist/암호초기화.exe 파일 존재
- [ ] 다른 PC에서 테스트 완료
- [ ] 백신 검사 통과
- [ ] 모든 기능 정상 작동

---

## 💡 추가 팁

### 빌드 시간 단축
첫 빌드: 5-10분
이후 빌드: 1-2분

### 배포
- EXE 파일만 배포하면 됨
- Python 설치 불필요
- 인터넷 연결 불필요 (실행 시)
- 다른 라이브러리 불필요

### 버전 관리
EXE 파일 이름에 버전 포함:
```powershell
pyinstaller --name "암호초기화_v1.0" test.py
```

---

## 🌟 성공!

빌드가 완료되면 `dist/암호초기화.exe` 파일을:
- USB에 복사
- 이메일로 전송
- 네트워크 공유
- 클라우드 업로드

어떤 방법으로든 다른 Windows PC로 전달하여 **바로 실행** 가능합니다!

Python이나 다른 프로그램 설치 없이 독립 실행됩니다! 🎉
