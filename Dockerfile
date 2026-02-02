# Windows용 EXE 빌드를 위한 Dockerfile
FROM python:3.11-windowsservercore

WORKDIR /app

# 필요한 패키지 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 소스 코드 복사
COPY test.py .

# PyInstaller로 EXE 생성
RUN pyinstaller --onefile --windowed --name "암호초기화" test.py

# 빌드된 파일을 출력 디렉토리로 복사
CMD ["cmd", "/c", "echo Build completed && dir dist"]
