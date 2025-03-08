FROM python:3.11-slim

WORKDIR /chatbot

# ติดตั้ง dependencies ที่จำเป็นสำหรับ numpy และอื่นๆ
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    libffi-dev \
    && rm -rf /var/lib/apt/lists/*

COPY . /chatbot

RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

EXPOSE 3000

# ENV OPENROUTER_API_KEY = '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'

CMD ["python", "./app.py"]