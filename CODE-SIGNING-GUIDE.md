# 🛡️ Windows 보안 경고 해결 가이드

## 문제점
PyInstaller로 만든 `.exe` 파일이 Windows에서 실행 시:
```
"Windows의 PC 보호"
"알 수 없는 게시자"
```
경고 메시지가 나타남

---

## ⚡ 빠른 해결 (사용자용)

### 방법 A: SmartScreen 우회
1. 경고 창에서 **"추가 정보"** 클릭
2. **"실행"** 버튼 클릭

### 방법 B: 파일 속성에서 차단 해제
1. `.exe` 파일 우클릭 → **속성**
2. **일반** 탭 → 하단의 **차단 해제** 체크
3. **확인** 클릭 후 실행

---

## 🔐 영구적 해결 방법

### 1. 코드 서명 인증서 (Code Signing Certificate)

**추천 인증서 제공업체:**
- Sectigo (구 Comodo) - 약 $200/년
- DigiCert - 약 $300/년
- GlobalSign - 약 $250/년

**단계:**

#### 1단계: 인증서 구매
- 위 업체 중 선택하여 "Code Signing Certificate" 구매
- EV (Extended Validation) 인증서 권장 (더 신뢰도 높음)

#### 2단계: 인증서 설치
Windows에서 제공받은 인증서 설치

#### 3단계: 실행 파일 서명

**수동 서명 (Windows SDK 필요):**
```cmd
signtool sign /f "인증서파일.pfx" /p "비밀번호" /t http://timestamp.digicert.com HelloWorldGUI.exe
```

**GitHub Actions에서 자동 서명:**
아래 워크플로우 참고

---

### 2. PyInstaller 빌드 최적화

일부 안티바이러스가 오탐지하는 것을 줄이는 방법:

```bash
# UPX 압축 비활성화 (오탐지 감소)
pyinstaller --onefile --windowed --noupx --name "HelloWorldGUI" gui_app.py

# 관리자 권한 요구하지 않음
# spec 파일에 uac_admin=False 설정
```

---

### 3. VirusTotal 평판 쌓기

**방법:**
1. https://www.virustotal.com 접속
2. `.exe` 파일 업로드
3. 여러 안티바이러스 엔진에서 검사
4. 시간이 지나면서 평판 쌓임

**효과:**
- Windows Defender가 파일 해시를 학습
- 반복 사용 시 경고 빈도 감소

---

## 📝 사용자 안내문 예시

프로그램 배포 시 README에 포함:

```
## Windows 보안 경고 안내

이 프로그램은 개인 개발자가 만든 무료 프로그램입니다.
코드 서명 인증서가 없어 Windows에서 보안 경고가 표시될 수 있습니다.

### 실행 방법:
1. 경고 창에서 "추가 정보"를 클릭하세요
2. "실행" 버튼을 클릭하세요

또는

1. 파일을 우클릭 → 속성
2. "차단 해제" 체크 → 확인
3. 프로그램 실행

이 프로그램은 악성코드가 아니며, 소스 코드는 GitHub에서 확인할 수 있습니다:
https://github.com/wonguri/python-hello-world
```

---

## 💰 비용 비교

| 방법 | 비용 | 효과 | 추천도 |
|------|------|------|--------|
| 사용자 우회 안내 | 무료 | ⭐⭐ | 개인/소규모 |
| 코드 서명 (일반) | ~$200/년 | ⭐⭐⭐⭐ | 상용 |
| 코드 서명 (EV) | ~$300/년 | ⭐⭐⭐⭐⭐ | 기업 |
| VirusTotal | 무료 | ⭐⭐⭐ | 무료 배포 |

---

## 🎯 권장 사항

**개인 프로젝트:**
- 사용자 안내문 제공
- VirusTotal 평판 쌓기
- GitHub에 소스 코드 공개

**상용 제품:**
- 코드 서명 인증서 구매 필수
- EV 인증서 권장

**오픈소스:**
- README에 우회 방법 명시
- 소스 코드 공개로 신뢰도 확보
