# 🐍 Python Hello World - GUI & Console Applications

Python으로 만든 간단한 애플리케이션 모음입니다.

## 📦 포함된 프로그램

### 1. **test.py** - 콘솔 프로그램
간단한 "Hello, World!" 출력 프로그램

### 2. **gui_app.py** - GUI 프로그램
Tkinter로 만든 대화형 GUI 애플리케이션
- 이름 입력 및 인사 기능
- 모던한 버튼 디자인
- Windows/macOS/Linux 호환

---

## 🚀 실행 방법

### Python으로 직접 실행
```bash
# 가상환경 활성화
source .venv/bin/activate

# 콘솔 프로그램
python test.py

# GUI 프로그램
python gui_app.py
```

### 실행 파일 다운로드 (Windows)
GitHub의 [Actions](https://github.com/wonguri/python-hello-world/actions) 탭에서:
- `console-windows-exe.zip` - 콘솔 버전
- `gui-windows-exe.zip` - GUI 버전

---

## ⚠️ Windows 보안 경고 해결

Windows에서 실행 시 "Windows의 PC 보호" 경고가 나타날 수 있습니다.

### 안전하게 실행하는 방법:

**방법 1:**
1. 경고 창에서 **"추가 정보"** 클릭
2. **"실행"** 버튼 클릭

**방법 2:**
1. `.exe` 파일 우클릭 → **속성**
2. **일반** 탭 → **차단 해제** 체크
3. **확인** 클릭 후 실행

### 왜 이런 경고가 나타나나요?

이 프로그램은 개인 개발자가 만든 무료 오픈소스 프로그램입니다.
코드 서명 인증서($200~300/년)가 없어 Windows에서 자동으로 경고를 표시합니다.

**이 프로그램은 100% 안전합니다:**
- ✅ 모든 소스 코드가 GitHub에 공개되어 있습니다
- ✅ 악성코드나 바이러스가 없습니다
- ✅ 개인정보를 수집하지 않습니다
- ✅ 인터넷 연결이 필요하지 않습니다

더 자세한 내용은 [CODE-SIGNING-GUIDE.md](CODE-SIGNING-GUIDE.md)를 참고하세요.

---

## 🛠️ 개발 환경

- **Python**: 3.11+
- **GUI Framework**: Tkinter (Python 기본 내장)
- **Build Tool**: PyInstaller
- **CI/CD**: GitHub Actions

---

## 📁 프로젝트 구조

```
project1/
├── test.py              # 콘솔 프로그램
├── gui_app.py           # GUI 프로그램
├── .venv/               # Python 가상환경
├── dist/                # 빌드된 실행 파일
├── .github/workflows/   # GitHub Actions 자동 빌드
├── README.md            # 이 파일
└── CODE-SIGNING-GUIDE.md # 보안 경고 해결 가이드
```

---

## 🌐 크로스 플랫폼 지원

| 플랫폼 | 콘솔 | GUI | 실행 파일 |
|--------|------|-----|----------|
| Windows | ✅ | ✅ | ✅ .exe |
| macOS | ✅ | ✅ | ✅ .app |
| Linux | ✅ | ✅ | ✅ binary |

---

## 📄 라이선스

MIT License - 자유롭게 사용, 수정, 배포 가능합니다.

---

## 🤝 기여하기

이슈나 Pull Request는 언제나 환영합니다!

1. Fork this repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

---

## 📞 문의

- GitHub: [@wonguri](https://github.com/wonguri)
- Repository: [python-hello-world](https://github.com/wonguri/python-hello-world)
