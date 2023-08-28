# 기반 이미지 설정
FROM python:3.9

# 작업 디렉토리 설정
WORKDIR /app

# 호스트의 현재 디렉토리의 requirements.txt 파일을 컨테이너의 /app 디렉토리로 복사
COPY requirements.txt .

# 필요한 패키지 설치
RUN apt-get update && apt-get install libgl1 -y
RUN pip install -r requirements.txt

# 호스트의 현재 디렉토리의 전체 내용을 컨테이너의 /app 디렉토리로 복사
COPY . .