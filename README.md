# 🔐 암호 초기화 프로그램

Windows Active Directory 사용자를 위한 OTP 기반 셀프 암호 초기화 도구

## ✨ 주요 기능

- 🔑 **OTP 이메일 인증**: 안전한 2단계 인증
- 📧 **Gmail SMTP 연동**: 자동 OTP 발송
- 🔌 **Active Directory 통합**: LDAP를 통한 암호 변경
- 🖥️ **GUI 인터페이스**: 사용하기 쉬운 Tkinter 기반 UI
- 🚀 **독립 실행**: Python 설치 불필요

## 📦 다운로드 및 설치

### 방법 1: Portable 패키지 (권장)

1. [Releases](../../releases)에서 `portable_windows.zip` 다운로드
2. Windows PC에 압축 해제
3. `run.bat` 실행
4. 완료!

### 방법 2: 단일 EXE 파일

1. Windows PC에서 빌드:
   ```cmd
   python -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt
   build_exe.bat
   ```
2. `dist/암호초기화.exe` 실행

## 🔧 기술 스택

- **언어**: Python 3.11
- **GUI**: Tkinter
- **이메일**: smtplib
- **LDAP**: ldap3
- **빌드**: PyInstaller

## 🖼️ 스크린샷

프로그램 실행 화면:
- Windows 계정 ID 입력
- 회사 이메일로 OTP 수신
- 새 암호 설정

## ⚙️ 설정

`test.py` 파일에서 다음 항목을 수정하세요:

```python
# 이메일 설정
MAIL_FROM = "your-email@gmail.com"
MAIL_PASSWORD = "your-app-password"
MAIL_TO = "recipient@example.com"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

# LDAP 설정
LDAP_SERVER = "192.168.0.231"
LDAP_DOMAIN = "yourdomain.local"
LDAP_USER = "domain\\administrator"
LDAP_PASSWORD = "your-password"
LDAP_BASE_DN = "dc=yourdomain,dc=local"
```

## 📋 시스템 요구사항

- Windows 7/8/10/11 (64bit)
- 인터넷 연결 (OTP 발송 시)
- Active Directory 접근 권한

## 🚀 빌드 방법

### Windows에서 EXE 빌드

```cmd
# 가상환경 생성
python -m venv .venv
.venv\Scripts\activate

# 패키지 설치
pip install -r requirements.txt

# 빌드 실행
build_exe.bat
```

### macOS에서 Portable 패키지 생성

```bash
./create_portable_windows.sh
```

## 📖 문서

- [QUICK_START.md](QUICK_START.md) - 빠른 시작 가이드
- [WINDOWS_BUILD_INSTRUCTIONS.md](WINDOWS_BUILD_INSTRUCTIONS.md) - Windows 빌드 상세 가이드
- [README_FINAL.md](README_FINAL.md) - 종합 가이드

## 🔒 보안

- 암호는 `*`로 마스킹되어 표시
- LDAP SSL/TLS 연결 지원
- Gmail SMTP SSL 사용
- 6자리 랜덤 OTP 생성

## ⚠️ 주의사항

- Gmail 앱 비밀번호 사용 필요 (2단계 인증 활성화 시)
- Active Directory 관리자 권한 필요
- 백신 프로그램이 EXE를 차단할 수 있음 (예외 처리 필요)

## 🤝 기여

버그 리포트 및 기능 제안은 [Issues](../../issues)에서 환영합니다!

## 📄 라이선스

MIT License

## 👨‍💻 개발

원본 PowerShell 스크립트를 Python으로 변환하여 크로스 플랫폼 지원

---

**Made with ❤️ for IT Admins**
