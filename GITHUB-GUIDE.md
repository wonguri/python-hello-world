# 🚀 GitHub Actions로 Windows .exe 빌드하기

## 빠른 시작 (3단계!)

### 1️⃣ GitHub 저장소 만들기

브라우저에서 **https://github.com/new** 접속하고:

- **Repository name**: `python-hello-world` (또는 원하는 이름)
- **Public** 또는 **Private** 선택
- **"Create repository"** 클릭

✅ 저장소 URL 복사하기 (예: `https://github.com/username/python-hello-world.git`)

---

### 2️⃣ 코드 Push하기

터미널에서 다음 명령어 실행:

```bash
cd /Users/user/Desktop/workspace/project1
./push-to-github.sh https://github.com/사용자명/저장소명.git
```

> **중요**: `https://github.com/사용자명/저장소명.git` 부분을 1단계에서 복사한 URL로 바꾸세요!

**예시:**
```bash
./push-to-github.sh https://github.com/john/python-hello-world.git
```

---

### 3️⃣ Windows .exe 다운로드

1. GitHub 저장소 페이지에서 **"Actions"** 탭 클릭
2. **"Build Windows EXE"** 워크플로우 클릭
3. 빌드 완료 대기 (약 2-3분) ⏱️
4. 하단 **"Artifacts"** 섹션에서 **"test-windows-exe"** 클릭하여 다운로드
5. 압축 풀면 **`test.exe`** 파일 완성! 🎉

---

## 📁 프로젝트 구조

```
project1/
├── test.py                          # 원본 Python 스크립트
├── .github/workflows/build-exe.yml  # GitHub Actions 자동 빌드 설정
├── push-to-github.sh                # GitHub push 헬퍼 스크립트
└── dist/test                        # macOS 실행 파일 (이미 완료)
```

---

## 💡 팁

### GitHub 로그인이 필요한 경우

Push 시 사용자명과 비밀번호를 물어보면:
- **Username**: GitHub 사용자명
- **Password**: ❌ GitHub 비밀번호 대신 **Personal Access Token** 사용

#### Personal Access Token 만들기:
1. https://github.com/settings/tokens
2. **"Generate new token (classic)"** 클릭
3. **Scopes**: `repo` 체크
4. **"Generate token"** 클릭
5. 생성된 토큰 복사 (한 번만 표시됨!)
6. Password 입력란에 토큰 붙여넣기

---

## ✅ 성공 확인

GitHub Actions에서 다음과 같은 메시지를 보면 성공:

```
✓ Set up Python
✓ Install dependencies  
✓ Build EXE
✓ Upload EXE
```

Artifacts에서 `test-windows-exe.zip`을 다운로드하면 됩니다!

---

## 🆘 문제 해결

### 문제: "remote origin already exists"
```bash
git remote remove origin
./push-to-github.sh https://github.com/사용자명/저장소명.git
```

### 문제: "authentication failed"
Personal Access Token을 사용하세요 (위 팁 참조)

### 문제: Actions 탭이 안 보여요
저장소 설정에서 Actions가 활성화되어 있는지 확인하세요
(Settings → Actions → General → Allow all actions)

---

## 📞 준비 완료!

모든 파일이 준비되었습니다. 위 3단계만 따라하시면 Windows `.exe` 파일을 얻으실 수 있습니다! 🎊
